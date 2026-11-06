

# BoostPost201Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ad** | [**Ad**](Ad.md) |  |  [optional] |
|**message** | **String** |  |  [optional] |
|**instagramVideoFallback** | [**InstagramVideoFallback**](InstagramVideoFallback.md) |  |  [optional] |
|**recoveredWrites** | [**List&lt;MetaRecoveredWritesInner&gt;**](MetaRecoveredWritesInner.md) | Meta only, present only when needed. Every object this request did not get confirmed by its first POST: found by name after Meta lost or failed its answer (&#x60;adopted&#x60;), or created by a second POST after a Meta 5xx (&#x60;repostedAfter&#x60;).  A re-POSTed object may have a twin from the first POST that Meta wrote late: check its parent for a duplicate name. Send &#x60;retryOnServerError: false&#x60; to never re-POST.  |  [optional] |
|**warnings** | **List&lt;String&gt;** | Human-readable notes about the boost.  - **With instagramVideoFallback:** one line saying how the Instagram video was boosted. - **&#x60;activation_failed:&#x60; (Meta):** Meta refused the final switch to ACTIVE of the campaign, ad set or ad this boost created. Nothing was deleted and &#x60;message&#x60; says not everything is ACTIVE. - **&#x60;activation_failed:&#x60; content:** names what was kept PAUSED and what was switched ACTIVE, and quotes Meta&#39;s error and the status calls that switch the PAUSED ones on later. - **&#x60;replayed_paused:&#x60;:** a retry without Idempotency-Key inside the 10-minute dedup window found the stored ad PAUSED although it asks for ACTIVE. Carries the same status calls.  |  [optional] |



