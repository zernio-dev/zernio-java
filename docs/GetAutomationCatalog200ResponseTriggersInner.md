

# GetAutomationCatalog200ResponseTriggersInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | [**KindEnum**](#KindEnum) |  |  |
|**type** | **String** | &#x60;schedule&#x60;, or the Zernio event name. |  |
|**label** | **String** | Event triggers only. |  [optional] |
|**subject** | **String** | What an event is about, such as &#x60;post&#x60; or &#x60;account&#x60;. |  [optional] |
|**scope** | **Object** | Which of &#x60;profileId&#x60; and &#x60;accountIds&#x60; an event trigger needs. |  [optional] |
|**facts** | [**List&lt;GetAutomationCatalog200ResponseTriggersInnerFactsInner&gt;**](GetAutomationCatalog200ResponseTriggersInnerFactsInner.md) | The facts a &#x60;filter&#x60; can compare, for an event trigger. |  [optional] |
|**subjects** | **List&lt;Object&gt;** | Scheduled trigger only: what it can check (&#x60;post&#x60;), with the facts of each. |  [optional] |
|**every** | **List&lt;String&gt;** |  |  [optional] |
|**times** | **Object** | Ad rule trigger only: the weekly set times it takes. |  [optional] |
|**filterOperators** | **List&lt;String&gt;** |  |  [optional] |
|**steps** | **List&lt;String&gt;** |  |  [optional] |
|**boost** | **Object** | Scheduled trigger only: the platforms, goals, most days and most boosts a day of &#x60;ads.boost_post&#x60;. |  [optional] |
|**limits** | **List&lt;String&gt;** |  |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| AD_RULE | &quot;ad_rule&quot; |
| EVENT | &quot;event&quot; |
| SCHEDULED | &quot;scheduled&quot; |



