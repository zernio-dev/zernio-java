

# ListCommentAutomations200ResponseAutomationsInnerStats


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**triggered** | **Integer** |  |  [optional] |
|**dmsSent** | **Integer** |  |  [optional] |
|**dmsFailed** | **Integer** |  |  [optional] |
|**uniqueContacts** | **Integer** |  |  [optional] |
|**trackedSends** | **Integer** | DMs sent with a trackable (wrapped) link. CTR denominator: divide clicks by this, not dmsSent. Lags dmsSent for campaigns that predate click tracking. |  [optional] |
|**linkClicks** | **Integer** | Total clicks on tracked links (bots/prefetch excluded). |  [optional] |
|**uniqueClicks** | **Integer** | Distinct people who clicked a tracked link. |  [optional] |
|**delivered** | **Integer** | DMs confirmed delivered (Messenger; IG emits no delivery receipt). |  [optional] |
|**read** | **Integer** | DMs confirmed read (IG messaging_seen / Messenger message_reads). |  [optional] |



