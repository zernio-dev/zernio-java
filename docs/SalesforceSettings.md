

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
|**logDeliveryStatus** | **Boolean** | Whether sent WhatsApp, SMS and RCS messages in the transcript are marked sent, delivered, read, played or failed. |  |
|**syncIssue** | [**SalesforceSettingsSyncIssue**](SalesforceSettingsSyncIssue.md) |  |  |
|**useOpportunitiesInResults** | **Boolean** | Whether closed-won Opportunities count as sales (Amount, in the Opportunity&#39;s or the org&#39;s currency) on the ad campaign named by their Primary Campaign Source, in campaign results and ad rules. Lost or reopened Opportunities stop counting. |  |
|**reportOpportunitiesToAds** | **Boolean** | Whether Zernio sends newly closed-won Opportunities as Purchase events (source &#x60;salesforce&#x60;) to the profile&#39;s event destinations. |  |



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



