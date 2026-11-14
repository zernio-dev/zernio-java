

# ConnectLineCredentials200ResponseWebhook


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**url** | **URI** | The webhook URL Zernio set on the channel. |  [optional] |
|**configured** | **Boolean** | Whether LINE accepted the webhook URL. When false, paste &#x60;url&#x60; into the LINE Developers Console &gt; Messaging API &gt; Webhook URL yourself. |  [optional] |
|**testSucceeded** | **Boolean** | Whether LINE&#39;s webhook test call reached Zernio. It does not show whether Webhooks is turned on; read &#x60;active&#x60; for that. |  [optional] |
|**active** | **Boolean** | Whether Webhooks (LINE Developers Console: Use webhook) is turned on for the channel, read after Zernio set its URL.  &#x60;false&#x60; means LINE sends no events until the account owner turns it on in LINE Official Account Manager &gt; Settings &gt; Response settings. &#x60;null&#x60; when LINE did not answer the read, and always when &#x60;configured&#x60; is &#x60;false&#x60;.  |  [optional] |
|**detail** | **String** | What LINE answered when the setup or the test did not succeed. |  [optional] |
|**previousUrl** | **String** | Present when the channel pointed at another webhook URL before this connect. LINE allows one webhook URL per channel, so that URL stopped receiving events once Zernio set its own; &#x60;nextSteps&#x60; says so too. |  [optional] |



