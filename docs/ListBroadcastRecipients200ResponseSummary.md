

# ListBroadcastRecipients200ResponseSummary

Delivery totals across all recipients in the broadcast, independent of pagination and status filtering. Each recipient counts once, under its latest status, so `sent + delivered + read` is everyone the broadcast went out to.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**total** | **Integer** |  |  [optional] |
|**pending** | **Integer** |  |  [optional] |
|**sent** | **Integer** |  |  [optional] |
|**delivered** | **Integer** |  |  [optional] |
|**read** | **Integer** |  |  [optional] |
|**failed** | **Integer** |  |  [optional] |



