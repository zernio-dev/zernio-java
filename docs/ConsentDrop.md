

# ConsentDrop

An event the destination did not get because the visitor did not consent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventIndex** | **Integer** | Position of the event in the request&#39;s &#x60;events&#x60; array, counted from 0, also when repeats or events this destination does not take were left out. |  [optional] |
|**eventId** | **String** |  |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | &#x60;consent_denied&#x60;: a signal the platform needs is &#x60;DENIED&#x60;. &#x60;consent_missing&#x60;: the visitor is in the EEA, UK or CH and the signal was never given. |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| CONSENT_DENIED | &quot;consent_denied&quot; |
| CONSENT_MISSING | &quot;consent_missing&quot; |



