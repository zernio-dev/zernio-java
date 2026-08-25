

# SendInboxMessageRequestInteractiveActionOneOf10Parameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | **String** | ISO 3166-1 alpha-2 country code Meta should localize the address form for (e.g. IN). Required: Meta rejects the send without it. |  |
|**values** | **Map&lt;String, Object&gt;** | Optional pre-filled address field values. |  [optional] |
|**savedAddresses** | **List&lt;Map&lt;String, Object&gt;&gt;** | Optional list of the recipient&#39;s previously saved addresses to offer as quick picks. |  [optional] |
|**validationErrors** | **Map&lt;String, String&gt;** | Optional per-field error messages to show when re-prompting after a failed validation. |  [optional] |



