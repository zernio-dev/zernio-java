

# BulkCreateContactsRequestContactsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** |  |  |
|**platformIdentifier** | **String** | Required when the top-level accountId is set (channel mode). A row missing it in that mode is rejected individually and reported in errors[], not a 400 for the whole import. |  [optional] |
|**displayIdentifier** | **String** |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**company** | **String** |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |



