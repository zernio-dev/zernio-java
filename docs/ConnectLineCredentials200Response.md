

# ConnectLineCredentials200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** |  |  [optional] |
|**account** | [**ConnectedMessagingAccount**](ConnectedMessagingAccount.md) |  |  [optional] |
|**webhook** | [**ConnectLineCredentials200ResponseWebhook**](ConnectLineCredentials200ResponseWebhook.md) |  |  [optional] |
|**nextSteps** | **List&lt;String&gt;** | Settings the account owner still has to change in LINE Official Account Manager. Led by the turn-on-Webhooks step when &#x60;webhook.active&#x60; is &#x60;false&#x60;, then by a warning when &#x60;webhook.previousUrl&#x60; is set. The turn-on-Webhooks step is left out when &#x60;webhook.active&#x60; is &#x60;true&#x60;. |  [optional] |
|**redirectUrl** | **String** |  |  [optional] |



