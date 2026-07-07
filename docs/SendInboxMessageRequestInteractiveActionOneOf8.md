

# SendInboxMessageRequestInteractiveActionOneOf8

Carousel action. `type` on the parent must be `carousel`. Carries 2-10 cards, either all product cards (`type: \"product\"`, all referencing the same `catalog_id`) or media cards (any other `type`, e.g. `cta_url`, with a required image/video `header` on each card). `card_index` (0-9, non-repeating) is auto-filled sequentially when omitted. Product carousels require a Meta catalog connected to the WhatsApp Business Account in Commerce Manager; media carousels do not. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cards** | **List&lt;SendInboxMessageRequestInteractiveActionOneOf8CardsInner&gt;** |  |  |



