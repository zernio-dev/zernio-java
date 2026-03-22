

# InstagramDemographicsResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**success** | **Boolean** |  |  [optional] |
|**accountId** | **String** | The Zernio SocialAccount ID |  [optional] |
|**platform** | **String** |  |  [optional] |
|**metric** | [**MetricEnum**](#MetricEnum) |  |  [optional] |
|**timeframe** | [**TimeframeEnum**](#TimeframeEnum) | The timeframe used for demographic data |  [optional] |
|**demographics** | **Map&lt;String, List&lt;InstagramDemographicsResponseDemographicsValueInner&gt;&gt;** | Object keyed by breakdown dimension (age, city, country, gender) |  [optional] |
|**note** | **String** |  |  [optional] |



## Enum: MetricEnum

| Name | Value |
|---- | -----|
| FOLLOWER_DEMOGRAPHICS | &quot;follower_demographics&quot; |
| ENGAGED_AUDIENCE_DEMOGRAPHICS | &quot;engaged_audience_demographics&quot; |



## Enum: TimeframeEnum

| Name | Value |
|---- | -----|
| THIS_WEEK | &quot;this_week&quot; |
| THIS_MONTH | &quot;this_month&quot; |



