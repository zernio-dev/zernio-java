

# ConversionEventMessaging

Meta only, read when `actionSource` is `business_messaging` (Conversions API for Business Messaging). `channel` is sent as the event's `messaging_channel` (`instagram_direct` goes out as `instagram`). Each id lands in Meta's `user_data` unhashed, and an id that does not belong to `channel` is ignored. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**channel** | [**ChannelEnum**](#ChannelEnum) |  |  |
|**wabaId** | **String** | WhatsApp only. WhatsApp Business Account id, sent as &#x60;whatsapp_business_account_id&#x60;. |  [optional] |
|**ctwaClid** | **String** | WhatsApp only. Click-to-WhatsApp click id from the first inbound message referral, sent as &#x60;ctwa_clid&#x60;. |  [optional] |
|**pageId** | **String** | Messenger: Facebook Page id, sent as &#x60;page_id&#x60;. Instagram Direct: when &#x60;instagramBusinessAccountId&#x60; is absent, Zernio reads the Instagram professional account linked to this Page and sends its id as &#x60;ig_account_id&#x60;; if none is linked or the lookup fails, &#x60;page_id&#x60; is sent instead. |  [optional] |
|**instagramBusinessAccountId** | **String** | Instagram Direct only. Instagram professional account id (&#x60;instagram_business_account&#x60; on the Page), sent as &#x60;ig_account_id&#x60; next to &#x60;ig_sid&#x60;. |  [optional] |
|**pageScopedUserId** | **String** | Messenger only. The page-scoped user id (PSID) your Messenger webhook gives for the person, sent as &#x60;page_scoped_user_id&#x60; next to &#x60;page_id&#x60;. |  [optional] |
|**instagramScopedUserId** | **String** | Instagram Direct only. The Instagram-scoped user id (IGSID) your Instagram messaging webhook gives for the person, sent as &#x60;ig_sid&#x60;. |  [optional] |



## Enum: ChannelEnum

| Name | Value |
|---- | -----|
| WHATSAPP | &quot;whatsapp&quot; |
| MESSENGER | &quot;messenger&quot; |
| INSTAGRAM_DIRECT | &quot;instagram_direct&quot; |



