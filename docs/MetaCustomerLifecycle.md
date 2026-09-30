

# MetaCustomerLifecycle

Meta's Customer Lifecycle Strategy on a Sales ad set (Meta `ad_set_goal`). Rejected with 400 in adSetId attach mode: use PUT /v1/ads/ad-sets/{adSetId} for an ad set that already exists. Read it back with `GET /v1/ads/ad-sets/{adSetId}?fields=ad_set_goal` (type 0 all customers, 1 new excluding engaged, 2 new customers). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**strategy** | [**StrategyEnum**](#StrategyEnum) | &#x60;all_customers&#x60; is \&quot;Maximize conversions from all customers\&quot;. &#x60;new_customers&#x60; is \&quot;Acquire new customers\&quot; (excludes existing customers). &#x60;new_customers_excluding_engaged&#x60; also excludes people who engaged with you but have not bought yet.  |  |
|**existingCustomerAudienceIds** | **List&lt;String&gt;** | Custom audience ids that define your existing customers. Required with both new_customers strategies (Meta answers 400 subcode 1870251 without them); not allowed with all_customers. |  [optional] |
|**engagedAudienceIds** | **List&lt;String&gt;** | Custom audience ids of people who engaged but have not bought. Required with new_customers_excluding_engaged, not allowed with the other strategies. |  [optional] |



## Enum: StrategyEnum

| Name | Value |
|---- | -----|
| ALL_CUSTOMERS | &quot;all_customers&quot; |
| NEW_CUSTOMERS | &quot;new_customers&quot; |
| NEW_CUSTOMERS_EXCLUDING_ENGAGED | &quot;new_customers_excluding_engaged&quot; |



