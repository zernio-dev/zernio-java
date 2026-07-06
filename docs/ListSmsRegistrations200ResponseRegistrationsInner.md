

# ListSmsRegistrations200ResponseRegistrationsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**registrationType** | [**RegistrationTypeEnum**](#RegistrationTypeEnum) |  |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**brandStatus** | **String** | Carrier-registry brand status (e.g. VERIFIED). |  [optional] |
|**campaignStatus** | **String** |  |  [optional] |
|**brandId** | **String** | TCR brand id, useful when referencing the brand in carrier support threads. |  [optional] |
|**campaignId** | **String** | TCR campaign id. |  [optional] |
|**declineReason** | **String** |  |  [optional] |
|**phoneNumbers** | **List&lt;String&gt;** |  |  [optional] |
|**awaitingOtp** | **Boolean** | Sole-prop 10DLC only; the OTP step is still pending. |  [optional] |
|**trustScore** | **BigDecimal** | Carrier-assigned brand trust score; drives throughput. |  [optional] |
|**throughput** | [**ListSmsRegistrations200ResponseRegistrationsInnerThroughput**](ListSmsRegistrations200ResponseRegistrationsInnerThroughput.md) |  |  [optional] |



## Enum: RegistrationTypeEnum

| Name | Value |
|---- | -----|
| STANDARD_10DLC | &quot;standard_10dlc&quot; |
| SOLE_PROP_10DLC | &quot;sole_prop_10dlc&quot; |
| TOLL_FREE | &quot;toll_free&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| APPROVED | &quot;approved&quot; |
| REJECTED | &quot;rejected&quot; |



