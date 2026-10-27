

# GetAdAccountHealth200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adAccountId** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**checkedAt** | **OffsetDateTime** |  |  [optional] |
|**checks** | [**List&lt;GetAdAccountHealth200ResponseChecksInner&gt;**](GetAdAccountHealth200ResponseChecksInner.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;ok&quot; |
| ATTENTION | &quot;attention&quot; |
| BLOCKED | &quot;blocked&quot; |



