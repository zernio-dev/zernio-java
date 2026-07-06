

# CreatePhoneNumberPortIn201Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Porting order ID. |  [optional] |
|**telnyxPortingOrderId** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**phoneNumbers** | **List&lt;String&gt;** |  |  [optional] |
|**orders** | [**List&lt;CreatePhoneNumberPortIn201ResponseOrdersInner&gt;**](CreatePhoneNumberPortIn201ResponseOrdersInner.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DRAFT | &quot;draft&quot; |
| PENDING | &quot;pending&quot; |
| FOC_CONFIRMED | &quot;foc_confirmed&quot; |
| PORTED | &quot;ported&quot; |
| EXCEPTION | &quot;exception&quot; |
| CANCELLED | &quot;cancelled&quot; |



