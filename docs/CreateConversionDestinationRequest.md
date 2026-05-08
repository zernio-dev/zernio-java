

# CreateConversionDestinationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adAccountId** | **String** | Sponsored ad account ID. Numeric (e.g. \&quot;5123456\&quot;) or full &#x60;urn:li:sponsoredAccount:{id}&#x60; URN.  |  |
|**name** | **String** |  |  |
|**type** | **String** | Either a unified standard event name (e.g. \&quot;Purchase\&quot;, \&quot;Lead\&quot;, \&quot;AddToCart\&quot;) or a LinkedIn rule type enum value (e.g. \&quot;PURCHASE\&quot;, \&quot;QUALIFIED_LEAD\&quot;). The API maps standard names to LinkedIn enum values automatically.  |  |
|**attributionType** | [**AttributionTypeEnum**](#AttributionTypeEnum) |  |  [optional] |
|**postClickAttributionWindowSize** | [**PostClickAttributionWindowSizeEnum**](#PostClickAttributionWindowSizeEnum) | Default 30. 365 only allowed for LEAD, PURCHASE, ADD_TO_CART, QUALIFIED_LEAD, SUBMIT_APPLICATION rule types — the API rejects other combinations locally.  |  [optional] |
|**viewThroughAttributionWindowSize** | [**ViewThroughAttributionWindowSizeEnum**](#ViewThroughAttributionWindowSizeEnum) | Default 7. Same 365-day-window type restriction applies as &#x60;postClickAttributionWindowSize&#x60;.  |  [optional] |
|**valueType** | [**ValueTypeEnum**](#ValueTypeEnum) | DYNAMIC (default) uses the per-event &#x60;value&#x60; from &#x60;sendConversions&#x60;. FIXED uses the rule&#39;s &#x60;value&#x60; field. NO_VALUE drops monetary value entirely.  |  [optional] |
|**value** | [**CreateConversionDestinationRequestValue**](CreateConversionDestinationRequestValue.md) |  |  [optional] |
|**autoAssociationType** | [**AutoAssociationTypeEnum**](#AutoAssociationTypeEnum) | Controls campaign association at rule-creation time: - ALL_CAMPAIGNS: associate the rule with every active,   paused, and draft campaign in the ad account - OBJECTIVE_BASED: associate only campaigns whose   objective matches the rule&#39;s type - NONE: don&#39;t auto-associate. Manage associations via   the &#x60;/associations&#x60; endpoints below. Note: auto-association runs once at create time; new campaigns added after the rule still need explicit association.  |  [optional] |



## Enum: AttributionTypeEnum

| Name | Value |
|---- | -----|
| LAST_TOUCH_BY_CAMPAIGN | &quot;LAST_TOUCH_BY_CAMPAIGN&quot; |
| LAST_TOUCH_BY_CONVERSION | &quot;LAST_TOUCH_BY_CONVERSION&quot; |



## Enum: PostClickAttributionWindowSizeEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_7 | 7 |
| NUMBER_30 | 30 |
| NUMBER_90 | 90 |
| NUMBER_365 | 365 |



## Enum: ViewThroughAttributionWindowSizeEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_7 | 7 |
| NUMBER_30 | 30 |
| NUMBER_90 | 90 |
| NUMBER_365 | 365 |



## Enum: ValueTypeEnum

| Name | Value |
|---- | -----|
| DYNAMIC | &quot;DYNAMIC&quot; |
| FIXED | &quot;FIXED&quot; |
| NO_VALUE | &quot;NO_VALUE&quot; |



## Enum: AutoAssociationTypeEnum

| Name | Value |
|---- | -----|
| ALL_CAMPAIGNS | &quot;ALL_CAMPAIGNS&quot; |
| OBJECTIVE_BASED | &quot;OBJECTIVE_BASED&quot; |
| NONE | &quot;NONE&quot; |



