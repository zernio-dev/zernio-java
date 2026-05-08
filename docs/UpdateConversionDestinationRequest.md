

# UpdateConversionDestinationRequest

At least one mutable field beyond `adAccountId` is required; the route returns 400 if no patch fields are provided. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adAccountId** | **String** |  |  |
|**name** | **String** |  |  [optional] |
|**enabled** | **Boolean** | Setting &#x60;false&#x60; is equivalent to calling DELETE — the rule will appear as &#x60;inactive&#x60; afterwards.  |  [optional] |
|**attributionType** | [**AttributionTypeEnum**](#AttributionTypeEnum) |  |  [optional] |
|**postClickAttributionWindowSize** | [**PostClickAttributionWindowSizeEnum**](#PostClickAttributionWindowSizeEnum) | 365 only allowed for LEAD, PURCHASE, ADD_TO_CART, QUALIFIED_LEAD, SUBMIT_APPLICATION rule types.  |  [optional] |
|**viewThroughAttributionWindowSize** | [**ViewThroughAttributionWindowSizeEnum**](#ViewThroughAttributionWindowSizeEnum) | 365 only allowed for LEAD, PURCHASE, ADD_TO_CART, QUALIFIED_LEAD, SUBMIT_APPLICATION rule types.  |  [optional] |
|**valueType** | [**ValueTypeEnum**](#ValueTypeEnum) |  |  [optional] |
|**value** | [**UpdateConversionDestinationRequestValue**](UpdateConversionDestinationRequestValue.md) |  |  [optional] |



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



