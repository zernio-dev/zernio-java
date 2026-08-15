

# GetAccountHealth200ResponsePlatformConnection

WhatsApp accounts only. Live probe of the Meta link behind the channel, performed at request time (the same read as GET /v1/whatsapp/number-info).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;connected&#x60; &#x3D; Meta served the channel object. &#x60;disconnected&#x60; &#x3D; Meta refused to serve it (Graph error 100, subcode 33), which is how a phone-side coexistence disconnect surfaces. &#x60;unknown&#x60; &#x3D; the live read failed for another reason (timeout, transient Meta error), not evidence either way. |  [optional] |
|**checkedAt** | **OffsetDateTime** | When this live probe ran (always the current request; never cached) |  [optional] |
|**phoneStatus** | **String** | Meta&#39;s own &#x60;status&#x60; field from the phone-number node (for example CONNECTED), when the object was readable |  [optional] |
|**metaError** | [**GetAccountHealth200ResponsePlatformConnectionMetaError**](GetAccountHealth200ResponsePlatformConnectionMetaError.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CONNECTED | &quot;connected&quot; |
| DISCONNECTED | &quot;disconnected&quot; |
| UNKNOWN | &quot;unknown&quot; |



