

# UpdateGoogleBusinessPlaceActionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Resource name of the place action link (e.g. locations/123/placeActionLinks/456) |  |
|**uri** | **URI** | New action URL. At least one of uri or placeActionType is required (enforced server-side; not modeled as anyOf because required-only anyOf branches break SDK generators). |  [optional] |
|**placeActionType** | [**PlaceActionTypeEnum**](#PlaceActionTypeEnum) | New action type |  [optional] |



## Enum: PlaceActionTypeEnum

| Name | Value |
|---- | -----|
| APPOINTMENT | &quot;APPOINTMENT&quot; |
| ONLINE_APPOINTMENT | &quot;ONLINE_APPOINTMENT&quot; |
| DINING_RESERVATION | &quot;DINING_RESERVATION&quot; |
| FOOD_ORDERING | &quot;FOOD_ORDERING&quot; |
| FOOD_DELIVERY | &quot;FOOD_DELIVERY&quot; |
| FOOD_TAKEOUT | &quot;FOOD_TAKEOUT&quot; |
| SHOP_ONLINE | &quot;SHOP_ONLINE&quot; |



