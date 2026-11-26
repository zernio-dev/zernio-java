

# AutomationRunSubject

What the run is about. Null for a scheduled check, which judges many subjects.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | **String** | For example &#x60;conversation&#x60;, &#x60;contact&#x60;, &#x60;comment&#x60;, &#x60;message&#x60; or &#x60;post&#x60;. |  [optional] |
|**id** | **String** |  |  [optional] |
|**name** | **String** | The person&#39;s display name, where the run knows it. Null for a check about a post, an ad or an order. |  [optional] |
|**handle** | **String** | The person&#39;s username without &#x60;@&#x60;, or their phone number in E.164 (it always starts with &#x60;+&#x60;). Null where neither is known. |  [optional] |



