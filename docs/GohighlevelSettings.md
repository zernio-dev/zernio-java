

# GohighlevelSettings


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**locationId** | **String** | The GoHighLevel sub-account (location) id. |  |
|**companyId** | **String** | The agency that owns the sub-account, null for a sub-account under no agency. |  |
|**locationName** | **String** |  |  |
|**installedBy** | **String** | The GoHighLevel user who installed the app. |  |
|**relayConversions** | **Boolean** | CRM events are relayed as conversions. Default true. |  |
|**writeBackAttribution** | **Boolean** | Relayed conversions are written back onto the GoHighLevel contact. Default true. |  |
|**reportToAds** | **Boolean** | Relayed conversions are forwarded to the profile&#39;s ad platforms. Default false. |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| GOHIGHLEVEL | &quot;gohighlevel&quot; |



