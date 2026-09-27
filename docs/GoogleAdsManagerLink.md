

# GoogleAdsManagerLink


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**managerCustomerId** | **String** |  |  [optional] |
|**clientCustomerId** | **String** |  |  [optional] |
|**managerLinkId** | **String** | Null on a validateOnly invitation, where Google creates nothing. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status the link has after this call. |  [optional] |
|**validateOnly** | **Boolean** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| REFUSED | &quot;REFUSED&quot; |
| CANCELED | &quot;CANCELED&quot; |
| INACTIVE | &quot;INACTIVE&quot; |



