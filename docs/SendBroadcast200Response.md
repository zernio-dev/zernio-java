

# SendBroadcast200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**success** | **Boolean** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Current broadcast status after processing first batch |  [optional] |
|**sent** | **Integer** | Recipients sent in this batch |  [optional] |
|**failed** | **Integer** | Recipients failed in this batch |  [optional] |
|**recipientCount** | **Integer** | Total recipient count |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SENDING | &quot;sending&quot; |
| COMPLETED | &quot;completed&quot; |
| FAILED | &quot;failed&quot; |



