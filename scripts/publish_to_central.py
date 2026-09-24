import base64
import json
import os
import re
import subprocess
import time
import urllib.error
import urllib.request
import uuid


UUID_PATTERN = r'[0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}'


def upload():
    process = subprocess.Popen(
        ['mvn', '--batch-mode', '--no-transfer-progress', '-P', 'sign-artifacts',
         '-Dmaven.test.skip=true', 'deploy'],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
    )
    deployment_id = None
    timed_out_id = None
    for line in process.stdout:
        print(line, end='', flush=True)
        uploaded = re.search(r'Uploaded bundle successfully,.*deploymentId: (' + UUID_PATTERN + ')', line)
        timed_out = re.search(r'Polling for (' + UUID_PATTERN + r') timed out', line)
        if uploaded:
            deployment_id = uploaded.group(1)
        if timed_out:
            timed_out_id = timed_out.group(1)
    code = process.wait()
    if code == 0:
        return None
    # A polling timeout does not cancel Central's already accepted upload.
    if deployment_id and timed_out_id == deployment_id:
        print(f'Resuming publication status for existing deployment {deployment_id}', flush=True)
        return deployment_id
    raise SystemExit(code)


def get_status(deployment_id):
    credentials = f"{os.environ['MAVEN_CENTRAL_USERNAME']}:{os.environ['MAVEN_CENTRAL_PASSWORD']}"
    token = base64.b64encode(credentials.encode()).decode()
    request = urllib.request.Request(
        f'https://central.sonatype.com/api/v1/publisher/status?id={deployment_id}',
        method='POST', headers={'Authorization': f'Bearer {token}'},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def wait_for_publication(deployment_id):
    deployment_id = str(uuid.UUID(deployment_id))
    deadline = time.monotonic() + 7200
    while time.monotonic() < deadline:
        try:
            result = get_status(deployment_id)
        except urllib.error.HTTPError as error:
            if error.code != 429 and error.code < 500:
                raise
            print(f'Central status returned HTTP {error.code}; retrying', flush=True)
        except (urllib.error.URLError, TimeoutError):
            print('Central status request failed; retrying', flush=True)
        else:
            state = result.get('deploymentState')
            print(f'Central deployment {deployment_id}: {state}', flush=True)
            if state == 'PUBLISHED':
                return
            if state == 'FAILED':
                raise RuntimeError(f"Central validation/publishing failed: {json.dumps(result.get('errors'))}")
            if state not in {'PENDING', 'VALIDATING', 'VALIDATED', 'PUBLISHING'}:
                raise RuntimeError(f'Unexpected Central deployment state: {state}')
        time.sleep(30)
    raise RuntimeError(f'Timed out waiting for {deployment_id}; resume with the deployment_id workflow input')


def main():
    deployment_id = os.environ.get('CENTRAL_DEPLOYMENT_ID') or upload()
    if deployment_id:
        wait_for_publication(deployment_id)


if __name__ == '__main__':
    main()
