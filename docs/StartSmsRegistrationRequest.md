

# StartSmsRegistrationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**registrationType** | [**RegistrationTypeEnum**](#RegistrationTypeEnum) |  |  |
|**phoneNumbers** | **List&lt;String&gt;** | Your numbers this registration covers. |  |
|**brand** | [**StartSmsRegistrationRequestBrand**](StartSmsRegistrationRequestBrand.md) |  |  [optional] |
|**campaign** | [**StartSmsRegistrationRequestCampaign**](StartSmsRegistrationRequestCampaign.md) |  |  [optional] |
|**tollFree** | [**StartSmsRegistrationRequestTollFree**](StartSmsRegistrationRequestTollFree.md) |  |  [optional] |



## Enum: RegistrationTypeEnum

| Name | Value |
|---- | -----|
| STANDARD_10DLC | &quot;standard_10dlc&quot; |
| SOLE_PROP_10DLC | &quot;sole_prop_10dlc&quot; |
| TOLL_FREE | &quot;toll_free&quot; |



