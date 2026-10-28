

# OpenTrackingWindowRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**postId** | **String** | Id of an external post. Required unless &#x60;accountId&#x60; and &#x60;url&#x60; are both sent. |  [optional] |
|**accountId** | **String** | Connected account the post belongs to. Send together with &#x60;url&#x60;. |  [optional] |
|**url** | **String** | Public URL of the post on the platform. Send together with &#x60;accountId&#x60;. |  [optional] |
|**trackingDays** | **Integer** | How many days the window stays open. |  [optional] |
|**requestedBy** | **String** | Free-form label for who asked for the window. It is stored and returned as given. |  [optional] |



