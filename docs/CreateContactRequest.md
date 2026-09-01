

# CreateContactRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** |  |  |
|**name** | **String** |  |  |
|**email** | **String** |  |  [optional] |
|**company** | **String** |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**isSubscribed** | **Boolean** |  |  [optional] |
|**notes** | **String** |  |  [optional] |
|**accountId** | **String** | Optional. Creates a channel if provided with platform + platformIdentifier |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) | Channel platform. Only the enum values support contact channels; any other platform is rejected with code platform_not_supported. |  [optional] |
|**platformIdentifier** | **String** |  |  [optional] |
|**displayIdentifier** | **String** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| INSTAGRAM | &quot;instagram&quot; |
| FACEBOOK | &quot;facebook&quot; |
| TELEGRAM | &quot;telegram&quot; |
| TWITTER | &quot;twitter&quot; |
| BLUESKY | &quot;bluesky&quot; |
| REDDIT | &quot;reddit&quot; |
| WHATSAPP | &quot;whatsapp&quot; |
| SLACK | &quot;slack&quot; |



