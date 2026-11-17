

# SalesforceSettings


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Zernio account ID of the Salesforce connection. |  |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  |
|**orgId** | **String** | 18-character Salesforce organization ID. |  |
|**orgName** | **String** | The org&#39;s name, when the connected user can read it. |  |
|**environment** | [**EnvironmentEnum**](#EnvironmentEnum) | Whether the org was connected through login.salesforce.com or test.salesforce.com. |  |
|**instanceUrl** | **URI** | The org&#39;s API host, for example &#x60;https://acme.my.salesforce.com&#x60;. |  |
|**installedBy** | **String** | Email or username of the Salesforce user who connected the org. |  |
|**syncContacts** | **Boolean** | Whether Zernio creates a Lead or Contact (per &#x60;createAs&#x60;) for an inbox contact that matches nobody by phone or email. |  |
|**logMessages** | **Boolean** | Whether Zernio logs inbox messages. Each person, channel and UTC day gets one completed Task (subject &#x60;WhatsApp conversation · 2026-11-17&#x60;) whose Description holds the transcript; a day past 32,000 characters continues in a Task marked \&quot;(part 2)\&quot;. |  |
|**createAs** | [**CreateAsEnum**](#CreateAsEnum) | What a person new to Salesforce is created as. |  |
|**logDeliveryStatus** | **Boolean** | Whether sent messages in the transcript are marked delivered, read or failed. |  |
|**syncIssue** | [**SalesforceSettingsSyncIssue**](SalesforceSettingsSyncIssue.md) |  |  |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| SALESFORCE | &quot;salesforce&quot; |



## Enum: EnvironmentEnum

| Name | Value |
|---- | -----|
| PRODUCTION | &quot;production&quot; |
| SANDBOX | &quot;sandbox&quot; |



## Enum: CreateAsEnum

| Name | Value |
|---- | -----|
| LEAD | &quot;lead&quot; |
| CONTACT | &quot;contact&quot; |



