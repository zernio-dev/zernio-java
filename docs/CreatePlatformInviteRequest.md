

# CreatePlatformInviteRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**profileId** | **String** | The profile the account is connected to. |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**accountId** | **String** | Reconnect this existing account instead of adding a new one. It must belong to the profile and platform. |  [optional] |
|**loginMethod** | [**LoginMethodEnum**](#LoginMethodEnum) | Instagram only. instagram_login (the default) uses Instagram Login, facebook_login uses Facebook Login. A reconnect link keeps the method the account was connected with. |  [optional] |
|**expiresInDays** | **Integer** | Days until the link expires. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| LINKEDIN | &quot;linkedin&quot; |
| TWITTER | &quot;twitter&quot; |
| THREADS | &quot;threads&quot; |
| TIKTOK | &quot;tiktok&quot; |
| YOUTUBE | &quot;youtube&quot; |
| PINTEREST | &quot;pinterest&quot; |
| REDDIT | &quot;reddit&quot; |
| BLUESKY | &quot;bluesky&quot; |
| SNAPCHAT | &quot;snapchat&quot; |
| GOOGLEBUSINESS | &quot;googlebusiness&quot; |



## Enum: LoginMethodEnum

| Name | Value |
|---- | -----|
| INSTAGRAM_LOGIN | &quot;instagram_login&quot; |
| FACEBOOK_LOGIN | &quot;facebook_login&quot; |



