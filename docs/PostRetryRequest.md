

# PostRetryRequest

Optional. Omit the body to retry every failed or pending platform of the post.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platforms** | [**List&lt;PostRetryRequestPlatformsInner&gt;**](PostRetryRequestPlatformsInner.md) | Retry only these platforms. Platforms not listed are left as they are, so a platform that already published is never posted twice. Each entry matches the post platforms with that &#x60;platform&#x60; and, when given, that &#x60;accountId&#x60;. |  [optional] |



