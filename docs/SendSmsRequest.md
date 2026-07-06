

# SendSmsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**from** | **String** | One of your SMS-enabled numbers (E.164; formatting is normalized). |  |
|**to** | **String** | Recipient number (E.164). |  |
|**text** | **String** | Message body. Required unless &#x60;mediaUrls&#x60; is set. Max 10 SMS segments (1530 GSM-7 or 670 unicode characters). |  [optional] |
|**mediaUrls** | **List&lt;URI&gt;** | Public media URLs to attach (sends as MMS). Max 10. |  [optional] |



