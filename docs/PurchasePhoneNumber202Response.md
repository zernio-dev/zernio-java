

# PurchasePhoneNumber202Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**country** | **String** |  |  [optional] |
|**numberType** | **String** | The type that will be ordered after KYC approval. |  [optional] |
|**purchaseIntentId** | **String** | Echo of the purchaseIntentId you sent. Pass it to the KYC submission (or the KYC share link) so the resulting numbers and their whatsapp.number.* webhooks carry it. |  [optional] |
|**kycUrl** | **String** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| KYC_REQUIRED | &quot;kyc_required&quot; |



