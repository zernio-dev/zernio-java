

# WhatsAppTemplateButton


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**text** | **String** |  |  |
|**url** | **URI** | Required when type is URL |  [optional] |
|**example** | **List&lt;String&gt;** | Example values for URL suffix variables |  [optional] |
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
| FLOW | &quot;flow&quot; |
| MPM | &quot;mpm&quot; |
| CATALOG | &quot;catalog&quot; |



## Enum: OtpTypeEnum

| Name | Value |
|---- | -----|
| COPY_CODE | &quot;copy_code&quot; |
| ONE_TAP | &quot;one_tap&quot; |
| ZERO_TAP | &quot;zero_tap&quot; |



