

# XArticle

Long-form X Article payload. X Articles require an eligible X Premium+ account. Articles are mutually exclusive with top-level/custom tweet media and with threadItems, poll, quoteTweetId, replyToTweetId, inReplyToTweetId, replySettings, sensitiveMedia, paidPartnership, and madeWithAi. Publishing normally performs two billable X API requests at $0.010 each (draft + publish, $0.020 total); mode `draft` performs only the $0.010 draft request. `articleDraftId` is an internal recovery checkpoint and must not be supplied by API clients. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** |  |  |
|**contentState** | [**XArticleContentState**](XArticleContentState.md) |  |  |
|**mode** | [**ModeEnum**](#ModeEnum) | Publish creates an X Article draft and then publishes it. Draft stops after draft creation and returns the X draft ID without a public URL. |  [optional] |
|**cover** | [**XArticleCover**](XArticleCover.md) |  |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| PUBLISH | &quot;publish&quot; |
| DRAFT | &quot;draft&quot; |



