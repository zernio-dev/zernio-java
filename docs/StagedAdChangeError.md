

# StagedAdChangeError

Present once `failed`, and on a staged change marked `stale`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | An error code, or &#x60;target_changed&#x60; when the object changed on the ad network after staging. |  [optional] |
|**message** | **String** |  |  [optional] |
|**details** | **Map&lt;String, Object&gt;** | Only on a failed change. What the write reported: the objects a failed create had already made, the fields an update had written (&#x60;appliedFields&#x60;), or the result of each item of a list write that failed in part. |  [optional] |



