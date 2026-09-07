

# CreateConversionActionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | SocialAccount ID. Must be a &#x60;googleads&#x60; account. |  |
|**customerId** | **String** | Google Ads customer id (digits only). Resolved automatically when the connection has exactly one accessible customer. |  [optional] |
|**name** | **String** |  |  |
|**type** | [**TypeEnum**](#TypeEnum) | Only WEBPAGE is supported for creation today. |  |
|**defaultValue** | **BigDecimal** | Default conversion value used when an event doesn&#39;t carry its own value. |  [optional] |
|**alwaysUseDefaultValue** | **Boolean** | When true, always use defaultValue and ignore any value sent with the event. Defaults to true when defaultValue is set. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| WEBPAGE | &quot;WEBPAGE&quot; |



