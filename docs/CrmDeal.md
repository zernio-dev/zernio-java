

# CrmDeal

A HubSpot deal or a Salesforce Opportunity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**objectType** | [**ObjectTypeEnum**](#ObjectTypeEnum) |  |  |
|**name** | **String** |  |  |
|**stage** | **String** | HubSpot stage id (&#x60;closedwon&#x60;) or Salesforce &#x60;StageName&#x60; (&#x60;Closed Won&#x60;). |  |
|**amount** | **BigDecimal** |  |  |
|**currency** | **String** | ISO 4217. HubSpot sets it on multi-currency portals only. Salesforce gives the Opportunity&#39;s currency on multi-currency orgs, else the org currency read from its Currency Locale. |  |
|**closeDate** | **LocalDate** |  |  |
|**ownerId** | **String** |  |  |
|**contactIds** | **List&lt;String&gt;** | Associated HubSpot contacts, or the Opportunity&#39;s contact roles (primary first). |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**url** | **URI** |  |  |
|**properties** | **Map&lt;String, Object&gt;** |  |  |
|**raw** | **Map&lt;String, Object&gt;** |  |  [optional] |



## Enum: ObjectTypeEnum

| Name | Value |
|---- | -----|
| DEAL | &quot;deal&quot; |
| OPPORTUNITY | &quot;opportunity&quot; |



