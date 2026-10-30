

# PlatformTarget


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platform** | **String** | Supported values: twitter, threads, instagram, youtube, facebook, linkedin, pinterest, reddit, tiktok, bluesky, googlebusiness, telegram |  [optional] |
|**accountId** | [**PlatformTargetAccountId**](PlatformTargetAccountId.md) |  |  [optional] |
|**customContent** | **String** | Platform-specific text override. When set, this content is used instead of the top-level post content for this platform. Useful for tailoring captions per platform (e.g. keeping tweets under 280 characters). |  [optional] |
|**customMedia** | [**List&lt;MediaItem&gt;**](MediaItem.md) |  |  [optional] |
|**scheduledFor** | **OffsetDateTime** | Optional per-platform scheduled time override (uses post.scheduledFor when omitted) |  [optional] |
|**platformSpecificData** | **Map&lt;String, Object&gt;** | The platform-specific options stored on this target, echoed back as sent.  Typed per platform on the way in (see the *PlatformData schemas on the request body); free-form on the way out. A response is not guaranteed to match exactly one variant, and generated clients that pick a variant by structure reject the entire response when it doesn&#39;t.  Zernio&#39;s internal publishing state (snapshots, container ids, publish stage) is never returned here. The key is omitted rather than sent as an empty object.  |  [optional] |
|**status** | **String** | Platform-specific status: pending, processing, uploading, published, failed, cancelled (removed from the platform via POST /v1/posts/{postId}/unpublish) |  [optional] |
|**platformPostId** | **String** | The native post ID on the platform (populated after successful publish) |  [optional] |
|**platformPostUrl** | **String** | Public URL of the published post. Included in the response for immediate posts; for scheduled posts, fetch via GET /v1/posts/{postId} after publish time.  Empty when the platform confirmed the publish without returning an id a permalink can be built from (TikTok returns a publish id for some uploads). The TikTok reconcile cron backfills it later. If TikTok never returns one, /v1/analytics reports that entry as syncStatus unavailable.  |  [optional] |
|**publishedAt** | **OffsetDateTime** | Timestamp when the post was published to this platform. YouTube uploads a scheduled public video up to 15 minutes early as private with YouTube&#39;s own release time, so its entry is published with this set to scheduledFor, the moment the video goes public. |  [optional] |
|**removedFromPlatformAt** | **OffsetDateTime** | Set when a successfully published post later disappears from the platform (deleted on-platform or taken down by the platform). Absent while the post is live, and cleared if it reappears.  status stays \&quot;published\&quot; (it reflects the publish outcome), so poll this field to detect post-publish removals. Detection runs with the analytics sync: expect up to a few hours of lag.  |  [optional] |
|**isTrialReel** | **Boolean** | Present and true only when this Instagram reel was launched as a Trial through Zernio (created with platformSpecificData.trialParams). Use it to segment trial reels in analytics.  Instagram&#39;s Graph API exposes no readable trial field, so this reflects creation-time intent only: the reel STARTED as a trial, not whether or when it graduated.  |  [optional] |
|**trialGraduationStrategy** | [**TrialGraduationStrategyEnum**](#TrialGraduationStrategyEnum) | Graduation strategy the trial reel was launched with. Present only when isTrialReel is true. |  [optional] |
|**publishAttempts** | **Integer** | Number of times the publishing pipeline claimed this target to publish it since it was created or last manually retried (a manual retry resets it, except on TikTok). Not the number of retries (see publishRetries). |  [optional] |
|**publishRetries** | **Integer** | Instagram only. Automatic re-sends of media_publish on the same container that Zernio scheduled after Meta answered a transient error: 30 min, 2 h and 6 h after each failure, at most 3. Absent when none was scheduled.  While the target is still processing, the latest one may not have been sent yet. Not reset by a manual retry. Independent of publishAttempts, which counts publish-leg claims.  |  [optional] |
|**errorMessage** | **String** | Human-readable reason this target has not published yet, or why it failed.  - Failed entries: why the publish failed, with the platform&#39;s error details. - Pending entries: why the publish has not gone out yet, for example the last temporary error while Zernio retries the publish automatically, or a posting limit notice.  A posting limit holds the post with the notice \&quot;This post is queued and will publish automatically after &lt;timestamp&gt;\&quot;.  The limits are the hourly posting velocity limit and, on a TikTok account connected through the TikTok for Business app, the daily cap of 15 videos and 15 photo posts.  A held post keeps status pending and its scheduledFor moves to that timestamp. It is not failed.  |  [optional] |
|**errorCategory** | [**ErrorCategoryEnum**](#ErrorCategoryEnum) | Error category for programmatic handling:  - &#x60;auth_expired&#x60;: token expired/revoked - &#x60;user_content&#x60;: wrong format/too long - &#x60;user_abuse&#x60;: rate limits/spam - &#x60;account_issue&#x60;: config problems - &#x60;platform_rejected&#x60;: policy violation - &#x60;platform_error&#x60;: 5xx/maintenance - &#x60;platform_rate_limit&#x60;: platform throttling, retried automatically - &#x60;quota_exhausted&#x60;: a shared quota pool the integration draws on is empty, including our own capacity gate in front of one. Not caused by your content or account, and safe to retry once the pool frees up. - &#x60;system_error&#x60;: Zernio infra - &#x60;unknown&#x60;  |  [optional] |
|**errorSource** | [**ErrorSourceEnum**](#ErrorSourceEnum) | Who caused the error: user (fix content/reconnect), platform (outage/API change), system (Zernio issue, rare) |  [optional] |
|**platformError** | [**PostPlatformError**](PostPlatformError.md) |  |  [optional] |



## Enum: TrialGraduationStrategyEnum

| Name | Value |
|---- | -----|
| MANUAL | &quot;MANUAL&quot; |
| SS_PERFORMANCE | &quot;SS_PERFORMANCE&quot; |



## Enum: ErrorCategoryEnum

| Name | Value |
|---- | -----|
| AUTH_EXPIRED | &quot;auth_expired&quot; |
| USER_CONTENT | &quot;user_content&quot; |
| USER_ABUSE | &quot;user_abuse&quot; |
| ACCOUNT_ISSUE | &quot;account_issue&quot; |
| PLATFORM_REJECTED | &quot;platform_rejected&quot; |
| PLATFORM_ERROR | &quot;platform_error&quot; |
| PLATFORM_RATE_LIMIT | &quot;platform_rate_limit&quot; |
| QUOTA_EXHAUSTED | &quot;quota_exhausted&quot; |
| SYSTEM_ERROR | &quot;system_error&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: ErrorSourceEnum

| Name | Value |
|---- | -----|
| USER | &quot;user&quot; |
| PLATFORM | &quot;platform&quot; |
| SYSTEM | &quot;system&quot; |



