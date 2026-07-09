

# UsageMeteringPeriod


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**start** | **OffsetDateTime** |  |  [optional] |
|**end** | **OffsetDateTime** |  |  [optional] |
|**source** | [**SourceEnum**](#SourceEnum) | &#x60;cycle&#x60; &#x3D; a real billing period resolved; &#x60;window&#x60; &#x3D; trailing/custom window (or cycle fallback). |  [optional] |



## Enum: SourceEnum

| Name | Value |
|---- | -----|
| CYCLE | &quot;cycle&quot; |
| WINDOW | &quot;window&quot; |



