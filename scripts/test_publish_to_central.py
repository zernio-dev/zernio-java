import io
import os
import unittest
from unittest.mock import Mock, patch
from urllib.error import HTTPError

import publish_to_central as publish

DEPLOYMENT = '83840d9c-55bc-4b81-94d4-3feefc561787'


class PublishTests(unittest.TestCase):
    def run_maven(self, output, code):
        process = Mock(stdout=io.StringIO(output))
        process.wait.return_value = code
        with patch.object(publish.subprocess, 'Popen', return_value=process):
            return publish.upload()

    def test_success_does_not_upload_or_poll_again(self):
        self.assertIsNone(self.run_maven('BUILD SUCCESS\n', 0))

    def test_timeout_resumes_the_uploaded_deployment(self):
        output = (f'Uploaded bundle successfully, deploymentId: {DEPLOYMENT}.\n'
                  f'Polling for {DEPLOYMENT} timed out before the deployment completed.\n')
        self.assertEqual(self.run_maven(output, 1), DEPLOYMENT)

    def test_build_failure_is_not_hidden(self):
        with self.assertRaises(SystemExit):
            self.run_maven('Compilation failure\n', 1)

    def test_timeout_without_matching_upload_is_not_hidden(self):
        with self.assertRaises(SystemExit):
            self.run_maven(f'Polling for {DEPLOYMENT} timed out\n', 1)

    def test_manual_resume_never_calls_maven(self):
        with patch.dict(os.environ, {'CENTRAL_DEPLOYMENT_ID': DEPLOYMENT}), \
             patch.object(publish, 'upload') as upload, \
             patch.object(publish, 'wait_for_publication') as wait:
            publish.main()
        upload.assert_not_called()
        wait.assert_called_once_with(DEPLOYMENT)

    @patch.object(publish.time, 'sleep')
    def test_poll_waits_for_published(self, sleep):
        with patch.object(publish, 'get_status', side_effect=[
            {'deploymentState': 'PUBLISHING'}, {'deploymentState': 'PUBLISHED'}
        ]):
            publish.wait_for_publication(DEPLOYMENT)
        sleep.assert_called_once()

    def test_validation_failure_is_not_hidden(self):
        with patch.object(publish, 'get_status', return_value={
            'deploymentState': 'FAILED', 'errors': {'artifact': ['invalid signature']}
        }), self.assertRaisesRegex(RuntimeError, 'invalid signature'):
            publish.wait_for_publication(DEPLOYMENT)

    @patch.object(publish.time, 'sleep')
    def test_transient_status_error_is_retried(self, sleep):
        with patch.object(publish, 'get_status', side_effect=[
            HTTPError('https://central.sonatype.com', 503, 'unavailable', {}, None),
            {'deploymentState': 'PUBLISHED'}
        ]):
            publish.wait_for_publication(DEPLOYMENT)
        sleep.assert_called_once()

    def test_auth_failure_is_not_retried(self):
        with patch.object(publish, 'get_status', side_effect=HTTPError(
            'https://central.sonatype.com', 401, 'unauthorized', {}, None
        )), self.assertRaises(HTTPError):
            publish.wait_for_publication(DEPLOYMENT)

    def test_timeout_does_not_report_success(self):
        with patch.object(publish.time, 'monotonic', side_effect=[0, 7201]), \
             self.assertRaisesRegex(RuntimeError, 'Timed out'):
            publish.wait_for_publication(DEPLOYMENT)


if __name__ == '__main__':
    unittest.main()
