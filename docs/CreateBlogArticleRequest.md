

# CreateBlogArticleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** |  |  |
|**bodyHtml** | **String** | Article body as HTML. |  [optional] |
|**handle** | **String** | URL slug. Generated from the title when omitted. |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**author** | **String** | Display name of the article author. |  [optional] |
|**excerpt** | **String** | Short summary shown in blog listings. |  [optional] |
|**image** | [**CreateBlogArticleRequestImage**](CreateBlogArticleRequestImage.md) |  |  [optional] |
|**seo** | [**CreateBlogArticleRequestSeo**](CreateBlogArticleRequestSeo.md) |  |  [optional] |
|**isPublished** | **Boolean** | Set false to create the article as a draft. |  [optional] |
|**publishDate** | **OffsetDateTime** | ISO 8601 datetime with offset (or Z). A future date schedules publication natively on the platform. |  [optional] |



