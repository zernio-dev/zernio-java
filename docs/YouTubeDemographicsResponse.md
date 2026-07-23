

# YouTubeDemographicsResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**success** | **Boolean** |  |  [optional] |
|**accountId** | **String** | The Zernio SocialAccount ID |  [optional] |
|**platform** | **String** |  |  [optional] |
|**videoId** | **String** | Present only when demographics are scoped to a single video |  [optional] |
|**title** | **String** | Video title (video mode only) |  [optional] |
|**publishedAt** | **OffsetDateTime** | Video publish date (video mode only) |  [optional] |
|**demographics** | **Map&lt;String, List&lt;YouTubeDemographicsResponseDemographicsValueInner&gt;&gt;** | Object keyed by breakdown dimension (age, gender, country) |  [optional] |
|**dateRange** | [**YouTubeDemographicsResponseDateRange**](YouTubeDemographicsResponseDateRange.md) |  |  [optional] |
|**provisionalSince** | **LocalDate** | Present only when the range reaches into YouTube&#39;s ~3-day processing window: the first date whose numbers are provisional and may still be revised by YouTube. |  [optional] |
|**note** | **String** |  |  [optional] |



