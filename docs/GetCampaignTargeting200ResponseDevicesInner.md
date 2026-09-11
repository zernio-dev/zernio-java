

# GetCampaignTargeting200ResponseDevicesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**device** | [**DeviceEnum**](#DeviceEnum) |  |  [optional] |
|**included** | **Boolean** |  |  [optional] |
|**bidModifier** | **BigDecimal** | Google&#39;s bid adjustment for this device: null when it has none, 0 when the device is switched off, otherwise 0.1 to 10. |  [optional] |



## Enum: DeviceEnum

| Name | Value |
|---- | -----|
| MOBILE | &quot;MOBILE&quot; |
| DESKTOP | &quot;DESKTOP&quot; |
| TABLET | &quot;TABLET&quot; |
| CONNECTED_TV | &quot;CONNECTED_TV&quot; |



