

# UpdateAdRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**budget** | [**UpdateAdRequestBudget**](UpdateAdRequestBudget.md) |  |  [optional] |
|**targeting** | [**UpdateAdRequestTargeting**](UpdateAdRequestTargeting.md) |  |  [optional] |
|**creative** | [**UpdateAdRequestCreative**](UpdateAdRequestCreative.md) |  |  [optional] |
|**name** | **String** | Rename the ad. Now propagated to Meta (POST /{ad-id}); non-Meta platforms return 501. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PAUSED | &quot;paused&quot; |



