

# GetCallsUsage200ResponseGroupsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | The group key: a &#x60;YYYY-MM-DD&#x60; UTC day, one of your numbers, a channel, or a profile id. |  [optional] |
|**profileId** | **String** | With &#x60;groupBy&#x3D;profile&#x60; only: the profile id (same as &#x60;key&#x60;). |  [optional] |
|**externalId** | **String** | With &#x60;groupBy&#x3D;profile&#x60; only: the externalId set on the profile, null when it has none. |  [optional] |
|**calls** | **Integer** |  |  [optional] |
|**answered** | **Integer** |  |  [optional] |
|**minutes** | **BigDecimal** |  |  [optional] |
|**billableUSD** | **BigDecimal** |  |  [optional] |
|**metaUSD** | **BigDecimal** |  |  [optional] |
|**brandedCalls** | **Integer** |  |  [optional] |
|**brandedCallUSD** | **BigDecimal** |  |  [optional] |



