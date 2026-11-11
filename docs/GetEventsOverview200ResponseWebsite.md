

# GetEventsOverview200ResponseWebsite

`null` when the profile has no tracking site. Hit counts are approximate distinct counts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**steps** | [**List&lt;GetEventsOverview200ResponseWebsiteStepsInner&gt;**](GetEventsOverview200ResponseWebsiteStepsInner.md) | The funnel: page views, product views, add to cart, checkouts and purchases today. |  [optional] |
|**recovered** | **Integer** | Purchases with ad consent for which no browser pixel fired, so only the server reported them. |  [optional] |
|**conversions** | **Integer** | Purchases today. |  [optional] |
|**consented** | **Integer** | Page views with ad storage consent. |  [optional] |
|**visits** | **Integer** | Page views today. |  [optional] |
|**bots** | **Integer** | Page views from bots. |  [optional] |
|**serverPlatforms** | **List&lt;String&gt;** | Platforms of the forwarding rules that receive website events. |  [optional] |



