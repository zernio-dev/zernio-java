

# GetEventsAccuracy200ResponseDestinationsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ruleId** | **String** | The forwarding rule. |  [optional] |
|**profileId** | **String** |  |  [optional] |
|**accountId** | **String** |  |  [optional] |
|**platform** | **String** | Ad platform, such as &#x60;metaads&#x60; or &#x60;googleads&#x60;. |  [optional] |
|**accountName** | **String** |  |  [optional] |
|**destinationId** | **String** |  |  [optional] |
|**sales** | **Integer** | Real sales in the period from the sources the rule takes. |  [optional] |
|**sent** | **Integer** | Sales a send was tried for. |  [optional] |
|**accepted** | **Integer** | Sales the platform accepted, by the latest attempt. |  [optional] |
|**failed** | **Integer** |  |  [optional] |
|**retrying** | **Integer** |  |  [optional] |
|**notSent** | **Integer** | Sales never sent: no ad consent, no identifier the platform matches on, or left out by the rule&#39;s event names. |  [optional] |
|**accuracy** | **BigDecimal** | &#x60;accepted / sent&#x60;, from 0 to 1. &#x60;null&#x60; with no sale sent. |  [optional] |
|**deliveries** | [**GetEventsAccuracy200ResponseDestinationsInnerDeliveries**](GetEventsAccuracy200ResponseDestinationsInnerDeliveries.md) |  |  [optional] |
|**match** | [**GetEventsAccuracy200ResponseDestinationsInnerMatch**](GetEventsAccuracy200ResponseDestinationsInnerMatch.md) |  |  [optional] |
|**matchRate** | **BigDecimal** | &#x60;match.identified / match.events&#x60;. &#x60;null&#x60; with nothing sent. |  [optional] |



