

# CreateBlogArticleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** |  |  |
|**bodyHtml** | **String** | Article body as HTML. |  [optional] |
|**handle** | **String** | URL slug. Generated from the title when omitted. |  [optional] |
|**tags** | **List&lt;String&gt;** | Tag names. WordPress resolves existing names case-insensitively and creates missing tags. |  [optional] |
|**author** | **String** | Shopify author display name, or numeric WordPress user id serialized as a string. Assigning another WordPress user may require elevated capability. |  [optional] |
|**excerpt** | **String** | Short summary shown in blog listings. |  [optional] |
|**image** | [**CreateBlogArticleRequestImage**](CreateBlogArticleRequestImage.md) |  |  [optional] |
|**seo** | [**CreateBlogArticleRequestSeo**](CreateBlogArticleRequestSeo.md) |  |  [optional] |
|**isPublished** | **Boolean** | Set false for a draft or true to publish. On WordPress false takes priority over a future publishDate; omission with no date defaults to draft. |  [optional] |
|**publishDate** | **OffsetDateTime** | ISO 8601 datetime with offset (or Z). A future date schedules publication natively on the platform. |  [optional] |



