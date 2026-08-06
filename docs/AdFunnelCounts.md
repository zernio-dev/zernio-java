

# AdFunnelCounts

Named conversion-funnel steps, resolved from the same data as `actions` so you never have to parse action-type strings yourself.  Meta reports one event under several action types at once (`offsite_conversion.fb_pixel_purchase`, `omni_purchase`, `purchase`, …). Each field below takes the FIRST family member present rather than summing them, which is what makes these counts safe to add up — summing the raw `actions` keys yourself double or triple counts. The same priority order backs `conversions`, so a purchase-optimised campaign reports the identical number in `conversions` and `funnel.purchases`.  Every field is 0 when that step never fired. Populated for Meta ads; other platforms report a different action taxonomy and generally leave these at 0 (read `actions` for those). At ad-set and campaign level each step is summed from its per-ad values. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**landingPageViews** | **Integer** | Landing page views — the visitor actually loaded the destination, unlike a link click. Meta &#x60;landing_page_view&#x60;. |  [optional] |
|**contentViews** | **Integer** | Content views (Meta &#x60;ViewContent&#x60; pixel event). |  [optional] |
|**searches** | **Integer** | On-site searches (Meta &#x60;Search&#x60; pixel event). |  [optional] |
|**wishlistAdds** | **Integer** | Adds to wishlist (Meta &#x60;AddToWishlist&#x60; pixel event). |  [optional] |
|**cartAdds** | **Integer** | Adds to cart (Meta &#x60;AddToCart&#x60; pixel event). |  [optional] |
|**checkoutsInitiated** | **Integer** | Checkouts started (Meta &#x60;InitiateCheckout&#x60; pixel event). |  [optional] |
|**paymentInfoAdds** | **Integer** | Payment details added at checkout (Meta &#x60;AddPaymentInfo&#x60; pixel event). |  [optional] |
|**purchases** | **Integer** | Purchases (Meta &#x60;Purchase&#x60; pixel event). Pair with &#x60;purchaseValue&#x60; for revenue. |  [optional] |
|**leads** | **Integer** | Leads, from either the website pixel or an instant form — whichever the ad uses. |  [optional] |
|**registrationsCompleted** | **Integer** | Completed registrations (Meta &#x60;CompleteRegistration&#x60; pixel event). |  [optional] |
|**appInstalls** | **Integer** | Mobile app installs attributed to the ad. |  [optional] |
|**messagingConversationsStarted** | **Integer** | Messaging conversations started within 7 days — the headline metric for click-to-WhatsApp and click-to-Messenger ads. |  [optional] |
|**messagingFirstReplies** | **Integer** | Messaging threads where the person sent a first reply. |  [optional] |



