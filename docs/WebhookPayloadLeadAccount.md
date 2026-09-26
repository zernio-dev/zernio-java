

# WebhookPayloadLeadAccount


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Account ID (the facebook account owning the Page) |  |
|**accountId** | **String** | Account ID (same as id); canonical field for account filtering. |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**profileId** | **String** | Profile ID of the account that received the lead. Null when the lead has no profile on record. |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |



