

# WhatsAppTemplateButton


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**text** | **String** | Visible button label. Required for all types except copy_code (whose label is fixed by WhatsApp). |  [optional] |
|**url** | **URI** | Required when type is URL |  [optional] |
|**example** | **Object** |  |  [optional] |
|**phoneNumber** | **String** | Required when type is phone_number |  [optional] |
|**otpType** | [**OtpTypeEnum**](#OtpTypeEnum) | Required when type is otp |  [optional] |
|**autofillText** | **String** |  |  [optional] |
|**packageName** | **String** |  |  [optional] |
|**signatureHash** | **String** |  |  [optional] |
|**flowId** | **String** |  |  [optional] |
|**flowName** | **String** |  |  [optional] |
|**flowJson** | **String** |  |  [optional] |
|**flowAction** | **String** |  |  [optional] |
|**navigateScreen** | **String** |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| QUICK_REPLY | &quot;quick_reply&quot; |
| URL | &quot;url&quot; |
| PHONE_NUMBER | &quot;phone_number&quot; |
| OTP | &quot;otp&quot; |
| COPY_CODE | &quot;copy_code&quot; |
| FLOW | &quot;flow&quot; |
| MPM | &quot;mpm&quot; |
| CATALOG | &quot;catalog&quot; |



## Enum: OtpTypeEnum

| Name | Value |
|---- | -----|
| COPY_CODE | &quot;copy_code&quot; |
| ONE_TAP | &quot;one_tap&quot; |
| ZERO_TAP | &quot;zero_tap&quot; |



