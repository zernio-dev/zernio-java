

# RfPrediction

A Meta Reach & Frequency prediction. Money values in whole units of the ad account currency.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**predictionId** | **String** |  |  [optional] |
|**status** | **String** | ready | pending | failed:&lt;meta code&gt; |  [optional] |
|**budget** | **BigDecimal** | Quoted (or provided) lifetime budget for the window. |  [optional] |
|**reach** | **Integer** | Predicted (or requested) unique reach. |  [optional] |
|**impressions** | **Integer** |  |  [optional] |
|**minBudget** | **BigDecimal** | Meta&#39;s allowed lower bound for this spec. |  [optional] |
|**maxBudget** | **BigDecimal** |  |  [optional] |
|**minReach** | **Integer** |  |  [optional] |
|**maxReach** | **Integer** |  |  [optional] |
|**frequencyCap** | **Integer** |  |  [optional] |
|**startTime** | **Integer** | Unix seconds; the reserved window the R&amp;F ad set will run on. |  [optional] |
|**stopTime** | **Integer** |  |  [optional] |
|**expiresAt** | **String** | When the reservation&#39;s locked price expires (set after reserving). |  [optional] |



