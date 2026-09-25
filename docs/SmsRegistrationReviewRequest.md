

# SmsRegistrationReviewRequest

An open change request written as points. Answer each point with POST /v1/sms/registrations/{id}/respond: `answer` says what each point needs (text, a link, a hosted document, or a link or a document).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Changes with every request. Send it back as &#x60;requestId&#x60; when answering, so a reply to a replaced request is refused (409) instead of filed under the new points. |  [optional] |
|**intro** | **String** | Context from the reviewer, e.g. what was already fixed on our side. |  [optional] |
|**points** | [**List&lt;SmsRegistrationReviewRequestPointsInner&gt;**](SmsRegistrationReviewRequestPointsInner.md) |  |  [optional] |



