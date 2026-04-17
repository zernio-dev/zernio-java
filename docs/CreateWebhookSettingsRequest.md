

# CreateWebhookSettingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Webhook name (1-50 characters) |  |
|**url** | **URI** | Webhook endpoint URL (must be a valid URL, whitespace trimmed) |  |
|**secret** | **String** | Secret key for HMAC-SHA256 signature verification |  [optional] |
|**events** | [**List&lt;EventsEnum&gt;**](#List&lt;EventsEnum&gt;) | Events to subscribe to (at least one required) |  |
|**isActive** | **Boolean** | Enable or disable webhook delivery. Defaults to &#x60;true&#x60; when omitted. |  [optional] |
|**customHeaders** | **Map&lt;String, String&gt;** | Custom headers to include in webhook requests |  [optional] |



## Enum: List&lt;EventsEnum&gt;

| Name | Value |
|---- | -----|
| POST_SCHEDULED | &quot;post.scheduled&quot; |
| POST_PUBLISHED | &quot;post.published&quot; |
| POST_FAILED | &quot;post.failed&quot; |
| POST_PARTIAL | &quot;post.partial&quot; |
| POST_CANCELLED | &quot;post.cancelled&quot; |
| POST_RECYCLED | &quot;post.recycled&quot; |
| ACCOUNT_CONNECTED | &quot;account.connected&quot; |
| ACCOUNT_DISCONNECTED | &quot;account.disconnected&quot; |
| MESSAGE_RECEIVED | &quot;message.received&quot; |
| COMMENT_RECEIVED | &quot;comment.received&quot; |
| REVIEW_NEW | &quot;review.new&quot; |
| REVIEW_UPDATED | &quot;review.updated&quot; |



