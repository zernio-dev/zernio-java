

# BatchGetGoogleBusinessReviewsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**locationNames** | **List&lt;String&gt;** | Array of full location resource names (e.g. [&#39;accounts/123/locations/456&#39;]). Max 50 per request (Google&#39;s batchGetReviews cap); chunk larger sets into multiple requests. |  |
|**pageSize** | **Integer** | Number of reviews per page (max 50) |  [optional] |
|**pageToken** | **String** | Pagination token from previous response |  [optional] |
|**orderBy** | [**OrderByEnum**](#OrderByEnum) | Sort order requested from Google. Defaults to &#39;updateTime desc&#39; (newest first), which allows early-stopping pagination once results cross your date window. |  [optional] |



## Enum: OrderByEnum

| Name | Value |
|---- | -----|
| UPDATE_TIME_DESC | &quot;updateTime desc&quot; |
| RATING | &quot;rating&quot; |
| RATING_DESC | &quot;rating desc&quot; |



