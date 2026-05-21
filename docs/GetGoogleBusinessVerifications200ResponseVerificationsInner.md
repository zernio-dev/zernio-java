

# GetGoogleBusinessVerifications200ResponseVerificationsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Resource name, e.g. \&quot;locations/123/verifications/0T1776879124712\&quot;. The last segment is the verificationId. |  [optional] |
|**method** | [**MethodEnum**](#MethodEnum) | Method used (omitted on some entries). |  [optional] |
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



