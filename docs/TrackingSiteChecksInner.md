

# TrackingSiteChecksInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**detail** | **String** | What to do when the check has not passed. |  [optional] |
|**checkedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| PASSED | &quot;passed&quot; |
| FAILED | &quot;failed&quot; |



