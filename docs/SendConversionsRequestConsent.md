

# SendConversionsRequestConsent

Batch-level user consent. Required by Google for EEA/UK events under the Feb 2026 restrictions. On Meta, any DENIED flag enables Limited Data Use on every event in the batch (data_processing_options [\"LDU\"] with geolocation, country 0 / state 0); GRANTED or absent consent sends events with Meta's default processing. Ignored by LinkedIn. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adUserData** | [**AdUserDataEnum**](#AdUserDataEnum) |  |  [optional] |
|**adPersonalization** | [**AdPersonalizationEnum**](#AdPersonalizationEnum) |  |  [optional] |



## Enum: AdUserDataEnum

| Name | Value |
|---- | -----|
| GRANTED | &quot;GRANTED&quot; |
| DENIED | &quot;DENIED&quot; |



## Enum: AdPersonalizationEnum

| Name | Value |
|---- | -----|
| GRANTED | &quot;GRANTED&quot; |
| DENIED | &quot;DENIED&quot; |



