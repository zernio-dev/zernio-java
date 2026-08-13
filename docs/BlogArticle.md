

# BlogArticle

An article inside a blog on the connected platform.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Platform-native article id (numeric string for Shopify). |  [optional] |
|**blogId** | **String** | Platform-native id of the blog the article belongs to. |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**bodyHtml** | **String** | Article body as HTML. |  [optional] |
|**handle** | **String** | URL slug of the article. |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**author** | **String** | Display name of the article author. |  [optional] |
|**excerpt** | **String** | Short summary shown in blog listings. |  [optional] |
|**image** | [**BlogArticleImage**](BlogArticleImage.md) |  |  [optional] |
|**isPublished** | **Boolean** | False while the article is a draft or its publish date is still in the future. |  [optional] |
|**publishedAt** | **OffsetDateTime** | When the article was (or is scheduled to be) published; null for drafts. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| SHOPIFY | &quot;shopify&quot; |



