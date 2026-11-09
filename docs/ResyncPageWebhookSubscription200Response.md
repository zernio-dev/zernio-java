

# ResyncPageWebhookSubscription200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**resubscribed** | **Boolean** |  |  [optional] |
|**pageId** | **String** |  |  [optional] |
|**appSubscribed** | **Boolean** |  |  [optional] |
|**leadgen** | **Boolean** |  |  [optional] |
|**subscribedFields** | **List&lt;String&gt;** |  |  [optional] |
|**warning** | **String** |  |  [optional] |
|**instagramUserId** | **String** | Instagram accounts only. |  [optional] |
|**subscriptionId** | **String** | Instagram accounts only. Id of the subscription record after the repair. |  [optional] |
|**previousSubscriptionId** | **String** | Instagram accounts only. Id of the record before the repair; null when there was none. |  [optional] |
|**recreated** | **Boolean** | Instagram accounts only. True when the subscription record id changed. |  [optional] |
|**missingFields** | **List&lt;String&gt;** | Instagram accounts only. Webhook fields Zernio expects that Meta did not subscribe. |  [optional] |



