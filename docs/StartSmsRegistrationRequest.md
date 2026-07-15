

# StartSmsRegistrationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**registrationType** | [**RegistrationTypeEnum**](#RegistrationTypeEnum) |  |  |
|**phoneNumbers** | **List&lt;String&gt;** | Your numbers this registration covers. |  |
|**brand** | [**StartSmsRegistrationRequestBrand**](StartSmsRegistrationRequestBrand.md) |  |  [optional] |
|**campaign** | [**StartSmsRegistrationRequestCampaign**](StartSmsRegistrationRequestCampaign.md) |  |  [optional] |
|**wizardValues** | **Map&lt;String, String&gt;** | Raw dashboard-wizard answers, stored only to prefill edit-and-resubmit. API integrators can omit. |  [optional] |
|**resubmitRequestId** | **String** | Resubmit a registration that was returned for changes — updates it in place instead of creating a new one. |  [optional] |
|**tollFree** | [**StartSmsRegistrationRequestTollFree**](StartSmsRegistrationRequestTollFree.md) |  |  [optional] |



## Enum: RegistrationTypeEnum

| Name | Value |
|---- | -----|
| STANDARD_10DLC | &quot;standard_10dlc&quot; |
| SOLE_PROP_10DLC | &quot;sole_prop_10dlc&quot; |
| TOLL_FREE | &quot;toll_free&quot; |



