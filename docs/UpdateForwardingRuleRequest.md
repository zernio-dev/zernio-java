

# UpdateForwardingRuleRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiSecret** | **String** |  |  [optional] |
|**eventNameMap** | **Map&lt;String, String&gt;** | Your event name to the name this destination gets, such as &#x60;{ \&quot;Lead\&quot;: \&quot;Purchase\&quot; }&#x60;. Names not in the map are sent unchanged.  A target spelled like a standard event in another case or form (&#x60;purchase&#x60;, &#x60;generate_lead&#x60;) is saved as the standard name (&#x60;Purchase&#x60;, &#x60;Lead&#x60;), so each platform gets its own standard event.  &#x60;eventNames&#x60; and &#x60;valueCondition&#x60; are checked against the name and value as received, before renaming. The event id is never changed, so deduplication still works. |  [optional] |
|**valueOverride** | [**ForwardingRuleValueOverride**](ForwardingRuleValueOverride.md) |  |  [optional] |
|**valueCondition** | [**ForwardingRuleValueCondition**](ForwardingRuleValueCondition.md) |  |  [optional] |



