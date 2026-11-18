

# GetEventsOverviewDaily200ResponseTotals

The period's figures, shaped like the overview's `today`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conversions** | **Integer** | Stored events that occurred in the period, retracted ones excluded. |  [optional] |
|**value** | **BigDecimal** | Value of those events in &#x60;currency&#x60;. Events in other currencies are left out. |  [optional] |
|**valueSent** | **BigDecimal** | Value in &#x60;currency&#x60; of those events at least one platform accepted. |  [optional] |
|**currency** | **String** | The currency most of the period&#39;s events use; &#x60;null&#x60; when none carried a value. |  [optional] |
|**sent** | **Integer** | Events first sent to a destination in the period, one per event and destination. |  [optional] |
|**accepted** | **Integer** | Those whose latest send the platform accepted. |  [optional] |
|**matched** | **Integer** | The period&#39;s events matched to an ad campaign. |  [optional] |
|**counted** | **Integer** | The period&#39;s events that count as campaign results, the ones looked up for a campaign. |  [optional] |



