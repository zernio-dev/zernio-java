

# UpdateBroadcastRequestMessage

Generic message payload (used for non-WhatsApp platforms).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**text** | **String** |  |  [optional] |
|**attachments** | [**List&lt;CreateBroadcastRequestMessageAttachmentsInner&gt;**](CreateBroadcastRequestMessageAttachmentsInner.md) | SMS only: sent as MMS media. |  [optional] |
|**messageTag** | [**MessageTagEnum**](#MessageTagEnum) | Instagram and Facebook only. See createBroadcast. |  [optional] |



## Enum: MessageTagEnum

| Name | Value |
|---- | -----|
| CONFIRMED_EVENT_UPDATE | &quot;CONFIRMED_EVENT_UPDATE&quot; |
| POST_PURCHASE_UPDATE | &quot;POST_PURCHASE_UPDATE&quot; |
| ACCOUNT_UPDATE | &quot;ACCOUNT_UPDATE&quot; |
| HUMAN_AGENT | &quot;HUMAN_AGENT&quot; |



