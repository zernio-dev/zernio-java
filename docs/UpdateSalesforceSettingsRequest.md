

# UpdateSalesforceSettingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**syncContacts** | **Boolean** | Create a Lead or Contact for an inbox contact that matches nobody by phone (any phone field) or email. A match is linked as it is and never updated. |  [optional] |
|**logMessages** | **Boolean** | Log inbound and outbound inbox messages as one conversation Task per person, channel and day. |  [optional] |
|**createAs** | [**CreateAsEnum**](#CreateAsEnum) | What a person new to Salesforce is created as. Leads get Company &#x60;[not provided]&#x60;. |  [optional] |
|**logDeliveryStatus** | **Boolean** | Mark sent messages in the transcript as delivered, read or failed. |  [optional] |



## Enum: CreateAsEnum

| Name | Value |
|---- | -----|
| LEAD | &quot;lead&quot; |
| CONTACT | &quot;contact&quot; |



