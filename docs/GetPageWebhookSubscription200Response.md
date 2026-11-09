

# GetPageWebhookSubscription200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pageId** | **String** |  |  [optional] |
|**appSubscribed** | **Boolean** | False when the Page carries no subscription for our app at all. |  [optional] |
|**leadgen** | **Boolean** | Whether lead ads submitted on this Page reach Zernio in real time. |  [optional] |
|**subscribedFields** | **List&lt;String&gt;** |  |  [optional] |
|**warning** | **String** | Present only when leadgen is missing. |  [optional] |
|**instagramUserId** | **String** | Instagram accounts only. |  [optional] |
|**subscriptionId** | **String** | Instagram accounts only. Id of the subscription record on Meta; null when there is none. |  [optional] |
|**missingFields** | **List&lt;String&gt;** | Instagram accounts only. Webhook fields Zernio expects that Meta did not subscribe. |  [optional] |



