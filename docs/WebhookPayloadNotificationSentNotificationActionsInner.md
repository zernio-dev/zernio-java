

# WebhookPayloadNotificationSentNotificationActionsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**operationId** | [**OperationIdEnum**](#OperationIdEnum) | The operationId of the public API call. |  |
|**method** | [**MethodEnum**](#MethodEnum) |  |  |
|**path** | **String** | The request path. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| RETRY_POST | &quot;retry_post&quot; |
| RECONNECT_ACCOUNT | &quot;reconnect_account&quot; |
| CHECK_ACCOUNT | &quot;check_account&quot; |



## Enum: OperationIdEnum

| Name | Value |
|---- | -----|
| RETRY_POST | &quot;retryPost&quot; |
| GET_CONNECT_URL | &quot;getConnectUrl&quot; |
| GET_ACCOUNT_HEALTH | &quot;getAccountHealth&quot; |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |



