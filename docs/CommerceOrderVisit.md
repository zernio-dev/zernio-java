

# CommerceOrderVisit

A store session that led to the order.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**occurredAt** | **OffsetDateTime** | Null on WooCommerce, which records the session start without a timezone. |  [optional] |
|**landingUrl** | **String** | The first page of the session, with its query string. |  [optional] |
|**referrerUrl** | **String** |  |  [optional] |
|**source** | **String** | Where the visit came from, as the platform names it. |  [optional] |
|**sourceType** | **String** | Shopify marketing tactic (e.g. SOCIAL, AD, SEARCH) or WooCommerce source type (utm, organic, referral, typein, admin). |  [optional] |
|**utm** | [**CommerceOrderVisitUtm**](CommerceOrderVisitUtm.md) |  |  [optional] |



