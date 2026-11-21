

# CrmDeal

A HubSpot deal, a Salesforce Opportunity or a GoHighLevel opportunity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**objectType** | [**ObjectTypeEnum**](#ObjectTypeEnum) |  |  |
|**name** | **String** |  |  |
|**stage** | **String** | HubSpot stage id (&#x60;closedwon&#x60;), Salesforce &#x60;StageName&#x60; (&#x60;Closed Won&#x60;) or GoHighLevel pipeline stage id. A GoHighLevel opportunity&#39;s won or lost &#x60;status&#x60; is a native field (&#x60;properties&#x3D;status&#x60;). |  |
|**amount** | **BigDecimal** |  |  |
|**currency** | **String** | ISO 4217. HubSpot sets it on multi-currency portals only. Salesforce gives the Opportunity&#39;s currency on multi-currency orgs, else the org currency read from its Currency Locale. Null on GoHighLevel. |  |
|**closeDate** | **LocalDate** | Null on GoHighLevel, whose opportunities have no close date. |  |
|**ownerId** | **String** |  |  |
|**contactIds** | **List&lt;String&gt;** | Associated HubSpot contacts, the Opportunity&#39;s contact roles (primary first), or the GoHighLevel opportunity&#39;s contact. |  |
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



