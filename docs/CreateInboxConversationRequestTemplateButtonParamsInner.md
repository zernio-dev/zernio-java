

# CreateInboxConversationRequestTemplateButtonParamsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**index** | **Integer** | Zero-based position of the button in the approved template&#39;s buttons. |  |
|**subType** | [**SubTypeEnum**](#SubTypeEnum) | The button kind, which decides how the value is sent: copy_code sends it as the coupon_code payload, flow as the flow token, url as the dynamic suffix appended to the button&#39;s base URL. |  |
|**value** | **String** | The value to send (e.g. the Pix copy-and-paste code for a copy_code button). |  |



## Enum: SubTypeEnum

| Name | Value |
|---- | -----|
| URL | &quot;url&quot; |
| COPY_CODE | &quot;copy_code&quot; |
| FLOW | &quot;flow&quot; |



