

# BrowseAdTargeting200ResponseNodesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nodeId** | **String** | Identifies the node within this response. Not a Meta id: never put it in a targeting spec. |  |
|**parentNodeId** | **String** | nodeId of the parent organizational node, null for a root. |  |
|**id** | **String** | Meta targeting id, null on organizational nodes. |  |
|**name** | **String** |  |  |
|**type** | **String** | Meta&#39;s targeting spec key (interests, behaviors, industries, life_events, education_statuses, relationship_statuses, family_statuses, income, ...). Null on most organizational nodes. |  |
|**path** | **List&lt;String&gt;** | Labels of the ancestors, root first. Does not include the node itself. |  |
|**selectable** | **Boolean** | True when the node can be targeted (it has a Meta id). |  |
|**description** | **String** | Meta&#39;s description, when it has one. |  [optional] |
|**audienceSizeLowerBound** | **Integer** | Meta&#39;s estimated audience size, lower bound, when reported. |  [optional] |
|**audienceSizeUpperBound** | **Integer** | Meta&#39;s estimated audience size, upper bound, when reported. |  [optional] |



