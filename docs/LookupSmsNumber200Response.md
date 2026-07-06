

# LookupSmsNumber200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**phoneNumber** | **String** |  |  [optional] |
|**carrierName** | **String** |  |  [optional] |
|**lineType** | [**LineTypeEnum**](#LineTypeEnum) |  |  [optional] |
|**smsReachable** | **Boolean** | True when the line type can receive SMS (not a landline). |  [optional] |



## Enum: LineTypeEnum

| Name | Value |
|---- | -----|
| MOBILE | &quot;mobile&quot; |
| LANDLINE | &quot;landline&quot; |
| VOIP | &quot;voip&quot; |
| TOLL_FREE | &quot;toll-free&quot; |
| UNKNOWN | &quot;unknown&quot; |



