

# ConversionDestination

A discoverable conversion destination on an ad platform — a Meta pixel, Google conversion action, or LinkedIn conversion rule. Returned by `listConversionDestinations`, `getConversionDestination`, `createConversionDestination`, and `updateConversionDestination`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform-native identifier. Pass back as &#x60;destinationId&#x60; on event send and as the path segment on CRUD endpoints.  |  |
|**name** | **String** |  |  |
|**type** | **String** | Present when the platform locks the event type/category to the destination (Google conversion actions, LinkedIn conversion rules). Absent for Meta pixels (which accept any event name per request).  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | For LinkedIn, &#x60;inactive&#x60; means the rule is soft-deleted (&#x60;enabled: false&#x60;).  |  [optional] |
|**adAccountId** | **String** | Set by adapters whose destinations are scoped to a specific ad account (LinkedIn). Pass back on subsequent CRUD calls to identify the parent ad account.  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



