

# PostAuthenticity


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**postId** | **String** | The external post the score belongs to |  |
|**score** | **Integer** | Higher means the view pattern looks more organic |  |
|**confidence** | **BigDecimal** | How much data the score rests on |  |
|**reasons** | [**List&lt;PostAuthenticityReasonsInner&gt;**](PostAuthenticityReasonsInner.md) | Each factor that lowered the score, with its weight in points |  |
|**version** | **String** | Scoring model version |  |
|**computedAt** | **OffsetDateTime** |  |  |
|**sampleCount** | **Integer** | Number of samples the score was computed from |  |



