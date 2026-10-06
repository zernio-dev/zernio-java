

# CommentAutomationStats

Running counters for the automation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**triggered** | **Integer** | Matched triggers that reached the audience or send stage. |  [optional] |
|**dmsSent** | **Integer** |  |  [optional] |
|**dmsFailed** | **Integer** |  |  [optional] |
|**uniqueContacts** | **Integer** |  |  [optional] |
|**trackedSends** | **Integer** | DMs sent with a trackable (wrapped) link. CTR denominator: divide clicks by this, not dmsSent. Lags dmsSent for campaigns that predate click tracking. |  [optional] |
|**linkClicks** | **Integer** | Total clicks on tracked links (bots/prefetch excluded). |  [optional] |
|**uniqueClicks** | **Integer** | Distinct people who clicked a tracked link. |  [optional] |
|**delivered** | **Integer** | DMs confirmed delivered (Messenger; IG emits no delivery receipt). |  [optional] |
|**read** | **Integer** | DMs confirmed read (IG messaging_seen / Messenger message_reads). |  [optional] |
|**audienceSkipped** | **Integer** | Triggers the audience rule did not answer with the DM. |  [optional] |
|**followGateSent** | **Integer** |  |  [optional] |
|**followGatePassed** | **Integer** |  |  [optional] |
|**followGateFailed** | **Integer** |  |  [optional] |



