

# EventConsent

Google Consent Mode's four signals as the visitor gave them. Leave a signal out when the visitor was never asked or never answered.  For a visitor in the EEA, the UK or Switzerland (from `user.country`), a signal left out counts as `DENIED`. See \"Consent\" on `POST /v1/events`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adStorage** | [**AdStorageEnum**](#AdStorageEnum) | Ad cookies and click ids (&#x60;ad_storage&#x60;). |  [optional] |
|**adUserData** | [**AdUserDataEnum**](#AdUserDataEnum) | Sending personal data to ad platforms (&#x60;ad_user_data&#x60;). |  [optional] |
|**adPersonalization** | [**AdPersonalizationEnum**](#AdPersonalizationEnum) | Personalized advertising and remarketing (&#x60;ad_personalization&#x60;). |  [optional] |
|**analyticsStorage** | [**AnalyticsStorageEnum**](#AnalyticsStorageEnum) | Analytics cookies (&#x60;analytics_storage&#x60;): Google Analytics only. |  [optional] |



## Enum: AdStorageEnum

| Name | Value |
|---- | -----|
| GRANTED | &quot;GRANTED&quot; |
| DENIED | &quot;DENIED&quot; |



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



## Enum: AnalyticsStorageEnum

| Name | Value |
|---- | -----|
| GRANTED | &quot;GRANTED&quot; |
| DENIED | &quot;DENIED&quot; |



