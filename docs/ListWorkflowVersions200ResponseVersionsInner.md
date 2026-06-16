

# ListWorkflowVersions200ResponseVersionsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**version** | **Integer** | Monotonically increasing version number |  [optional] |
|**name** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**createdBy** | **String** | User id that authored this version |  [optional] |
|**createdByEmail** | **String** | Denormalized email so the history UI can render without a join |  [optional] |
|**restoredFromVersion** | **Integer** | When non-null, this snapshot was created by restoring that version |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |



