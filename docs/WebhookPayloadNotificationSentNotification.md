

# WebhookPayloadNotificationSentNotification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) | The email notification preference this notification belongs to. securityAlerts has no preference: it is always sent. |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**subject** | **String** | The email subject. |  |
|**text** | **String** | The email body as plain text, without the greeting. |  |
|**url** | **URI** | Dashboard link for the notification. |  |
|**refs** | [**WebhookPayloadNotificationSentNotificationRefs**](WebhookPayloadNotificationSentNotificationRefs.md) |  |  |
|**reason** | **String** | Why the account was disconnected. Only on account_disconnected. |  [optional] |
|**actions** | [**List&lt;WebhookPayloadNotificationSentNotificationActionsInner&gt;**](WebhookPayloadNotificationSentNotificationActionsInner.md) | API calls that act on the notification, with the ids already in the path. |  |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| POST_FAILURES | &quot;postFailures&quot; |
| ACCOUNT_ISSUES | &quot;accountIssues&quot; |
| SECURITY_ALERTS | &quot;securityAlerts&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| POST_FAILED | &quot;post_failed&quot; |
| ACCOUNT_DISCONNECTED | &quot;account_disconnected&quot; |
| API_KEY_HANDED_OVER | &quot;api_key_handed_over&quot; |



