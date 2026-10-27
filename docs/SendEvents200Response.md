

# SendEvents200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventsReceived** | **Integer** | Events in the request. |  [optional] |
|**stored** | **Boolean** | Whether the events were stored for reporting (always false with testCode). |  [optional] |
|**testCode** | **String** | The test code forwarded to every destination, or &#x60;null&#x60; when the request carried none. |  [optional] |
|**destinations** | [**List&lt;SendEvents200ResponseDestinationsInner&gt;**](SendEvents200ResponseDestinationsInner.md) |  |  [optional] |



