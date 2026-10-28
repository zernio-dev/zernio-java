

# OAuthAppWebhook

Facebook and Instagram only: Meta delivers comments and messages to your app's own webhook, so set it to this callback URL and verify token on the app's webhook product (Page for Facebook, Instagram for Instagram) and subscribe the listed fields. Zernio checks each delivery against your app secret. Null on platforms with nothing to set up.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callbackUrl** | **URI** |  |  |
|**verifyToken** | **String** |  |  |
|**_object** | **OAuthAppWebhookObject** |  |  |
|**fields** | **List&lt;String&gt;** | Subscribe the app to these fields. |  |



