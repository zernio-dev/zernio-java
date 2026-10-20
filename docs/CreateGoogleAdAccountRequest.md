

# CreateGoogleAdAccountRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**accountId** | **String** | Zernio googleads SocialAccount ID whose Google user reaches the manager. |  |
|**managerCustomerId** | **String** | Manager (MCC) customer id without dashes. The new account is created under it. List reachable managers with GET /v1/ads/accounts/hierarchy. |  |
|**name** | **String** | Account name. Whitespace is trimmed. |  |
|**currency** | **String** | Uppercase ISO 4217 currency. Cannot be changed after creation. |  |
|**timeZone** | **String** | IANA time zone name, for example Europe/Madrid. Cannot be changed after creation. |  |
|**validateOnly** | **Boolean** | Ask Google to validate the request without creating the account. |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| GOOGLE | &quot;google&quot; |



