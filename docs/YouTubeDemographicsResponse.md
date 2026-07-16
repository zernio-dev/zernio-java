

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
|**note** | **String** |  |  [optional] |



