

# LookupSmsNumber200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phoneNumber** | **String** |  |  [optional] |
|**carrierName** | **String** |  |  [optional] |
|**lineType** | [**LineTypeEnum**](#LineTypeEnum) |  |  [optional] |
|**smsReachable** | **Boolean** | False for landlines, toll-free numbers, ambiguous fixed-or-mobile lines and carriers whose numbers are not SMS-routable. True is a best guess, not a delivery guarantee. |  [optional] |



## Enum: LineTypeEnum

| Name | Value |
|---- | -----|
| MOBILE | &quot;mobile&quot; |
| LANDLINE | &quot;landline&quot; |
| VOIP | &quot;voip&quot; |
| TOLL_FREE | &quot;toll-free&quot; |
| UNKNOWN | &quot;unknown&quot; |



