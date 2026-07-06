

# GetSmsRegistration200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**registrationType** | [**RegistrationTypeEnum**](#RegistrationTypeEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**brandStatus** | **String** |  |  [optional] |
|**campaignStatus** | **String** |  |  [optional] |
|**declineReason** | **String** |  |  [optional] |
|**phoneNumbers** | **List&lt;String&gt;** |  |  [optional] |
|**awaitingOtp** | **Boolean** |  |  [optional] |



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



