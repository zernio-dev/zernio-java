

# GetAdAccountHealth200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adAccountId** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**ready** | **Boolean** | False when a create or boost on this ad account would be refused; &#x60;blockers&#x60; says why. |  [optional] |
|**blockers** | [**List&lt;GetAdAccountHealth200ResponseBlockersInner&gt;**](GetAdAccountHealth200ResponseBlockersInner.md) |  |  [optional] |
|**checkedAt** | **OffsetDateTime** |  |  [optional] |
|**checks** | [**List&lt;GetAdAccountHealth200ResponseChecksInner&gt;**](GetAdAccountHealth200ResponseChecksInner.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;ok&quot; |
| ATTENTION | &quot;attention&quot; |
| BLOCKED | &quot;blocked&quot; |



