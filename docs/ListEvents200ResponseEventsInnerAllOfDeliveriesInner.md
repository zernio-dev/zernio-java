

# ListEvents200ResponseEventsInnerAllOfDeliveriesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | **String** | Ad platform of the destination, such as &#x60;metaads&#x60;; empty when the send failed before the platform was known. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SENT | &quot;sent&quot; |
| RETRYING | &quot;retrying&quot; |
| FAILED | &quot;failed&quot; |



