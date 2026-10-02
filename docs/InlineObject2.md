

# InlineObject2


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | **String** |  |  [optional] |
|**code** | [**CodeEnum**](#CodeEnum) |  |  [optional] |
|**requiredGroup** | [**RequiredGroupEnum**](#RequiredGroupEnum) | The resource group the key needs for this operation. Absent on admin-plane and unclassified-path denials. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| INSUFFICIENT_PERMISSIONS | &quot;insufficient_permissions&quot; |
| UNCLASSIFIED_RESOURCE | &quot;unclassified_resource&quot; |



## Enum: RequiredGroupEnum

| Name | Value |
|---- | -----|
| PUBLISHING | &quot;publishing&quot; |
| ENGAGEMENT | &quot;engagement&quot; |
| MESSAGES | &quot;messages&quot; |
| CONTACTS | &quot;contacts&quot; |
| ANALYTICS | &quot;analytics&quot; |
| ADS | &quot;ads&quot; |
| TELEPHONY | &quot;telephony&quot; |
| ACCOUNTS | &quot;accounts&quot; |
| BILLING | &quot;billing&quot; |
| WEBHOOKS | &quot;webhooks&quot; |



