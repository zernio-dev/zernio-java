

# StartGoogleBusinessVerification200ResponseVerification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) |  |  [optional] |
|**createTime** | **OffsetDateTime** |  |  [optional] |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| ADDRESS | &quot;ADDRESS&quot; |
| EMAIL | &quot;EMAIL&quot; |
| PHONE_CALL | &quot;PHONE_CALL&quot; |
| SMS | &quot;SMS&quot; |
| AUTO | &quot;AUTO&quot; |
| VETTED_PARTNER | &quot;VETTED_PARTNER&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| COMPLETED | &quot;COMPLETED&quot; |
| FAILED | &quot;FAILED&quot; |



