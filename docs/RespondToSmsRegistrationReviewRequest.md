

# RespondToSmsRegistrationReviewRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**note** | **String** | Answer for the reviewer. Required when no files are sent. |  [optional] |
|**files** | **List&lt;String&gt;** | Hosted document URLs returned by POST /v1/sms/opt-in-proof. |  [optional] |
|**requestId** | **String** | The &#x60;reviewRequest.id&#x60; you are answering. When it no longer matches the open request the reply is refused with 409. |  [optional] |
|**answers** | [**List&lt;RespondToSmsRegistrationReviewRequestAnswersInner&gt;**](RespondToSmsRegistrationReviewRequestAnswersInner.md) | One answer per point of the open &#x60;reviewRequest&#x60;, each point at most once. Required (every point) when the request has points; a missing, repeated or unknown point is a 400 naming the point ids. At most 10 files per reply. |  [optional] |



