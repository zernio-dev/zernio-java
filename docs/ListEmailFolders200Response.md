

# ListEmailFolders200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**List&lt;EmailFolder&gt;**](EmailFolder.md) |  |  [optional] |
|**stale** | **Boolean** | Always true when present. Present only when the provider did not answer and &#x60;data&#x60; is the last folder list Zernio read for the same account within the past 24 hours (&#x60;unreadCount&#x60; and &#x60;totalCount&#x60; may be out of date). |  [optional] |
|**asOf** | **OffsetDateTime** | When a stale list was read from the provider. Present only with &#x60;stale&#x60;. |  [optional] |



