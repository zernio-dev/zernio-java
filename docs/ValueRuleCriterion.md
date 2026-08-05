

# ValueRuleCriterion

One matching condition inside a value rule. `criteriaValues` and `criteriaValueTypes` are POSITIONALLY paired: same length, same order. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform criterion id. Echo it on &#x60;PUT&#x60; to KEEP this criterion, omit it to CREATE a new one. A criterion left out of the array entirely is DELETED.  |  [optional] |
|**criteriaType** | [**CriteriaTypeEnum**](#CriteriaTypeEnum) | The dimension being matched. &#x60;OMNI_CHANNEL&#x60; (conversion location: APP, INSTANT_FORM, PHONE_CALL, WEBSITE) is accepted even though Meta&#39;s own enum table omits it.  |  |
|**operator** | [**OperatorEnum**](#OperatorEnum) | Required on every criterion. &#x60;CONTAINS&#x60; is currently the only value Meta supports. |  |
|**criteriaValues** | **List&lt;String&gt;** | The values to match. &#x60;AGE&#x60; takes ranges such as &#x60;18-24&#x60;, &#x60;18+&#x60; or a custom &#x60;18-26&#x60;; a range whose upper bound is 65 is NOT allowed (use &#x60;18+&#x60; instead of &#x60;18-65&#x60;). &#x60;LOCATION&#x60; takes Targeting-Search keys: a two-letter country code for &#x60;LOCATION_COUNTRY&#x60;, a numeric key for region / city / comScore market. &#x60;AUDIENCE_LABEL&#x60; takes labels such as &#x60;HIGH_VALUE&#x60;, which are applied to a Custom Audience in Ads Manager: there is no API to provision them, so they are passed through unvalidated.  |  |
|**criteriaValueTypes** | **List&lt;String&gt;** | One entry per &#x60;criteriaValues&#x60; entry, in the same order. The literal &#x60;\&quot;NONE\&quot;&#x60; for every criteriaType except &#x60;LOCATION&#x60;, which uses &#x60;LOCATION_COUNTRY&#x60;, &#x60;LOCATION_REGION&#x60;, &#x60;LOCATION_CITY&#x60; or &#x60;LOCATION_COMSCORE_MARKET&#x60; and MAY mix them within one criterion. &#x60;LOCATION_DMA&#x60; was replaced by &#x60;LOCATION_COMSCORE_MARKET&#x60; on 2026-06-22 and is rejected by this API.  |  |



## Enum: CriteriaTypeEnum

| Name | Value |
|---- | -----|
| AGE | &quot;AGE&quot; |
| GENDER | &quot;GENDER&quot; |
| OS_TYPE | &quot;OS_TYPE&quot; |
| DEVICE_PLATFORM | &quot;DEVICE_PLATFORM&quot; |
| LOCATION | &quot;LOCATION&quot; |
| PLACEMENT | &quot;PLACEMENT&quot; |
| OMNI_CHANNEL | &quot;OMNI_CHANNEL&quot; |
| AUDIENCE_LABEL | &quot;AUDIENCE_LABEL&quot; |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| CONTAINS | &quot;CONTAINS&quot; |



