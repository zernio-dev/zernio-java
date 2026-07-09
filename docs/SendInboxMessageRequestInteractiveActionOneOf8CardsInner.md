

# SendInboxMessageRequestInteractiveActionOneOf8CardsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardIndex** | **Integer** | Card position. Auto-filled sequentially when omitted. |  [optional] |
|**type** | **String** | &#x60;product&#x60; for a product card; media cards use &#x60;cta_url&#x60; or a quick-reply type. |  [optional] |
|**header** | **Object** | Media cards only, required. Carries the card&#39;s image or video. |  [optional] |
|**body** | **Object** | Optional card body text. |  [optional] |
|**action** | **Object** | Product cards: &#x60;{ catalog_id, product_retailer_id }&#x60; (required). Media cards: the card&#39;s button action (e.g. &#x60;cta_url&#x60; with &#x60;parameters.display_text&#x60; and &#x60;parameters.url&#x60;). |  [optional] |



