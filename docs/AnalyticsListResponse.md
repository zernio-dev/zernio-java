

# AnalyticsListResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**overview** | [**AnalyticsOverview**](AnalyticsOverview.md) |  |  [optional] |
|**posts** | [**List&lt;AnalyticsListResponsePostsInner&gt;**](AnalyticsListResponsePostsInner.md) |  |  [optional] |
|**pagination** | [**Pagination**](Pagination.md) |  |  [optional] |
|**accounts** | [**List&lt;SocialAccount&gt;**](SocialAccount.md) | Connected accounts (followerCount and followersLastUpdated only included if user has analytics add-on) |  [optional] |
|**hasAnalyticsAccess** | **Boolean** | Whether user has analytics add-on access |  [optional] |
|**analyticsOff** | [**List&lt;AnalyticsOffAccount&gt;**](AnalyticsOffAccount.md) | The X accounts this list covers (after its platform, profile and account filters) whose analytics sync does not run: their numbers stay as of the last read. Also sent with &#x60;view&#x3D;summary&#x60;. Absent when there are none. |  [optional] |



