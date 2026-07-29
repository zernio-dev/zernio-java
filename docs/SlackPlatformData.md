

# SlackPlatformData

Slack message settings. Posts mrkdwn text (up to 40,000 chars; Slack truncates beyond that) to the channel fixed by the connected account, with up to 10 media files per post uploaded via Slack's file API (the text becomes the caption). The target channel is chosen at connect time — one connected account per channel — so channelId is NOT accepted here (a 400 is returned); connect the desired channel via /v1/connect/slack and target its accountId. Messages over 4,000 characters cannot be edited later (Slack's edit limit is stricter than its post limit). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**threadTs** | **String** | Parent message ts to post this message as a thread reply (e.g. \&quot;1503435956.000247\&quot;). |  [optional] |
|**unfurlLinks** | **Boolean** | Expand links in the message into preview cards. Default true. |  [optional] |
|**unfurlMedia** | **Boolean** | Expand media links into inline previews. Default true. |  [optional] |
|**username** | **String** | Override the bot display name for this message only (requires no setup; shown with an APP badge). Does not change the app identity in the sidebar. |  [optional] |
|**iconUrl** | **String** | Override the bot avatar image URL for this message only. |  [optional] |



