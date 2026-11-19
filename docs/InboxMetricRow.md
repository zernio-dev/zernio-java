

# InboxMetricRow


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**date** | **String** | Start of the period: the day or the Monday of the week, never before fromDate. With granularity&#x3D;total, fromDate. |  |
|**accountId** | **String** | With groupBy&#x3D;account. |  [optional] |
|**platform** | **String** | With groupBy&#x3D;account or groupBy&#x3D;platform. |  [optional] |
|**source** | **String** | With groupBy&#x3D;source; null for messages with no source recorded, such as messages received. |  [optional] |
|**dayOfWeek** | **Integer** | With groupBy&#x3D;hourOfWeek: 1 is Monday, 7 is Sunday, in UTC. |  [optional] |
|**hour** | **Integer** | With groupBy&#x3D;hourOfWeek: 0 to 23, in UTC. |  [optional] |
|**responseTimeBucket** | [**ResponseTimeBucket**](ResponseTimeBucket.md) | With groupBy&#x3D;responseTimeBucket. |  [optional] |
|**account** | [**InboxMetricRowAccount**](InboxMetricRowAccount.md) |  |  [optional] |
|**conversationId** | **String** | With groupBy&#x3D;conversation or conversationId: the Zernio conversation id, or the id logged with the messages when the conversation no longer exists. |  [optional] |
|**firstMessageAt** | **String** | With conversation rows: first message, read receipt or failure in the period, UTC. null for a conversation read by id with no activity in the period. |  [optional] |
|**lastMessageAt** | **String** | With conversation rows: last message, read receipt or failure in the period, UTC. |  [optional] |
|**conversation** | [**InboxMetricRowConversation**](InboxMetricRowConversation.md) |  |  [optional] |
|**metrics** | **Map&lt;String, BigDecimal&gt;** | Each metric asked; response times are null when no message received got a reply. |  |



