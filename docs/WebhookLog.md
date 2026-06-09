

# WebhookLog

A single webhook delivery attempt recorded by Zernio (30-day retention).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**userId** | **String** | ID of the account owner the webhook belongs to |  [optional] |
|**webhookId** | **String** | ID of the webhook configuration that produced this delivery |  [optional] |
|**webhookName** | **String** | Name of the webhook configuration at delivery time |  [optional] |
|**eventId** | **String** | Stable webhook event ID (correlates to the delivered payload) |  [optional] |
|**event** | **String** | Event type that triggered the delivery (e.g. post.published) |  [optional] |
|**url** | **URI** | Destination URL the webhook was delivered to |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Delivery outcome |  [optional] |
|**statusCode** | **Integer** | HTTP status code returned by the destination endpoint |  [optional] |
|**requestPayload** | **Map&lt;String, Object&gt;** | The JSON payload sent to the destination endpoint |  [optional] |
|**responseBody** | **String** | Response body returned by the destination endpoint |  [optional] |
|**errorMessage** | **String** | Error message when delivery failed |  [optional] |
|**attemptNumber** | **Integer** | Delivery attempt number (increments on retries) |  [optional] |
|**responseTime** | **Integer** | Time taken by the destination endpoint to respond, in milliseconds |  [optional] |
|**createdAt** | **OffsetDateTime** | Timestamp the delivery was attempted |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| FAILED | &quot;failed&quot; |



