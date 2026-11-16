

# TrackingSitePeriodTotals

A tracking site's page views over a period, as approximate distinct counts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**visits** | **Integer** | Page views without bots. |  [optional] |
|**bots** | **Integer** | Page views from bots. |  [optional] |
|**consented** | **Integer** | Page views with ad storage consent, at most &#x60;visits&#x60;. |  [optional] |
|**purchases** | **Integer** | Purchases recorded on the site. |  [optional] |
|**recovered** | **Integer** | Purchases with ad consent for which no browser pixel fired, so only the server reported them. |  [optional] |



