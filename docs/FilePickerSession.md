

# FilePickerSession


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Public session id, echoed as &#x60;pickerSessionId&#x60; on the redirect and as &#x60;picker.sessionId&#x60; on the webhook. |  |
|**url** | **URI** | The hosted picker page. Open it in the end user&#39;s browser (redirect or new tab, not an iframe). It is a credential: single-use and valid until &#x60;expiresAt&#x60;. |  |
|**expiresAt** | **OffsetDateTime** | 30 minutes after creation. |  |



