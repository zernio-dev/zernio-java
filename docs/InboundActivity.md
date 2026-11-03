

# InboundActivity

When inbound messages and comments were first and last seen for the account. Only events matched to this account count. WhatsApp delivery statuses for outbound messages do not count, so the stamps of a number that only sends stay null. The stamps reset on every connect.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firstMessageAt** | **OffsetDateTime** | First inbound message since the latest connect, or since tracking began for an account connected before it. Null when none yet. |  |
|**lastMessageAt** | **OffsetDateTime** | Latest inbound message, precise to about one hour. Null when none yet. |  |
|**firstCommentAt** | **OffsetDateTime** | First inbound comment since the latest connect, or since tracking began for an account connected before it. Null when none yet. |  |
|**lastCommentAt** | **OffsetDateTime** | Latest inbound comment, precise to about one hour. Null when none yet. |  |



