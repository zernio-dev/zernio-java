

# UpdateBlogArticleRequest

At least one field is required.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** |  |  [optional] |
|**bodyHtml** | **String** | Article body as HTML. |  [optional] |
|**handle** | **String** | URL slug of the article. |  [optional] |
|**tags** | **List&lt;String&gt;** | Replaces the full tag-name list. WordPress resolves existing names case-insensitively and creates missing tags. |  [optional] |
|**author** | **String** | Shopify author display name, or numeric WordPress user id serialized as a string. Assigning another WordPress user may require elevated capability. |  [optional] |
|**excerpt** | **String** | Short summary shown in blog listings. |  [optional] |
|**image** | [**UpdateBlogArticleRequestImage**](UpdateBlogArticleRequestImage.md) |  |  [optional] |
|**seo** | [**CreateBlogArticleRequestSeo**](CreateBlogArticleRequestSeo.md) |  |  [optional] |
|**isPublished** | **Boolean** | Set false to move to draft or true to publish. On WordPress false takes priority over a future publishDate; omission preserves status unless publishDate is sent. |  [optional] |
|**publishDate** | **OffsetDateTime** | ISO 8601 datetime with offset (or Z). A future date schedules publication natively on the platform. |  [optional] |



