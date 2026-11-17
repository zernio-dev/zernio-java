

# UpdateSalesforceSettingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**syncContacts** | **Boolean** | Create a Lead or Contact for an inbox contact that matches nobody by phone (any phone field) or email. A match is linked as it is and never updated. |  [optional] |
|**logMessages** | **Boolean** | Log inbound and outbound inbox messages as one conversation Task per person, channel and day. |  [optional] |
|**createAs** | [**CreateAsEnum**](#CreateAsEnum) | What a person new to Salesforce is created as. Leads get Company &#x60;[not provided]&#x60;. |  [optional] |
|**logDeliveryStatus** | **Boolean** | Mark sent messages in the transcript as delivered, read or failed. |  [optional] |
|**useOpportunitiesInResults** | **Boolean** | Count closed-won Opportunities as sales on the ad campaign named by their Primary Campaign Source, in campaign results and ad rules. Turning it on also fills in the Opportunities won in the last 90 days. Lost or reopened Opportunities stop counting. |  [optional] |
|**reportOpportunitiesToAds** | **Boolean** | Send each newly closed-won Opportunity once as a Purchase event (source &#x60;salesforce&#x60;, event id &#x60;salesforce_opp_{orgId}_{opportunityId}&#x60;) to the profile&#39;s event destinations, with the email and phone of its primary contact role, else the first Contact of its Account. Opportunities won before it was turned on are not sent. |  [optional] |



## Enum: CreateAsEnum

| Name | Value |
|---- | -----|
| LEAD | &quot;lead&quot; |
| CONTACT | &quot;contact&quot; |



