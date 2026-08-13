

# UpdateBlogArticleRequest

At least one field is required.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** |  |  [optional] |
|**bodyHtml** | **String** | Article body as HTML. |  [optional] |
|**handle** | **String** | URL slug of the article. |  [optional] |
|**tags** | **List&lt;String&gt;** | Replaces the full tag list. |  [optional] |
|**author** | **String** | Display name of the article author. |  [optional] |
|**excerpt** | **String** | Short summary shown in blog listings. |  [optional] |
|**image** | [**CreateBlogArticleRequestImage**](CreateBlogArticleRequestImage.md) |  |  [optional] |
|**seo** | [**CreateBlogArticleRequestSeo**](CreateBlogArticleRequestSeo.md) |  |  [optional] |
|**isPublished** | **Boolean** | Set false to unpublish the article back to a draft. |  [optional] |
|**publishDate** | **OffsetDateTime** | ISO 8601 datetime with offset (or Z). A future date schedules publication natively on the platform. |  [optional] |



