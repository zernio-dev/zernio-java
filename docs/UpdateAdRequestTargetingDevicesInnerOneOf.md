

# UpdateAdRequestTargetingDevicesInnerOneOf


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**device** | [**DeviceEnum**](#DeviceEnum) |  |  |
|**bidModifier** | **BigDecimal** | Google device bid modifier. 0 switches the device off (minus 100%); otherwise 0.1 to 10 (minus 90% to plus 900%). Google rejects any value between 0 and 0.1. |  [optional] |



## Enum: DeviceEnum

| Name | Value |
|---- | -----|
| MOBILE | &quot;MOBILE&quot; |
| DESKTOP | &quot;DESKTOP&quot; |
| TABLET | &quot;TABLET&quot; |
| CONNECTED_TV | &quot;CONNECTED_TV&quot; |



