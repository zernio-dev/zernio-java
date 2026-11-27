

# GetAutomationCatalog200ResponseTriggersInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | [**KindEnum**](#KindEnum) |  |  |
|**group** | [**GroupEnum**](#GroupEnum) | Where a trigger picker files it: the same groups as the template marketplace. |  |
|**resourceGroup** | [**ResourceGroupEnum**](#ResourceGroupEnum) | The API key resource group its kind needs to create one. |  |
|**type** | **String** | &#x60;schedule&#x60;, &#x60;enrollment&#x60;, a comment door such as &#x60;comment.keyword&#x60; (comment to DM), a flow trigger such as &#x60;inbound_message&#x60;, or the Zernio event name. |  |
|**label** | **String** | Its short name, such as &#x60;Ad rule schedule&#x60;. |  |
|**description** | **String** | One line on when it starts and what the automation does then. |  |
|**subject** | **String** | What an event is about, such as &#x60;post&#x60; or &#x60;account&#x60;. |  [optional] |
|**scope** | **Object** | Which of &#x60;profileId&#x60;, &#x60;accountId&#x60;, &#x60;accountIds&#x60; and &#x60;platformPostId&#x60; the trigger needs. |  [optional] |
|**platforms** | **List&lt;String&gt;** | The platforms a sequence, comment to DM or flow trigger runs on. |  [optional] |
|**facts** | [**List&lt;GetAutomationCatalog200ResponseTriggersInnerFactsInner&gt;**](GetAutomationCatalog200ResponseTriggersInnerFactsInner.md) | The facts a &#x60;filter&#x60; can compare, for an event trigger. |  [optional] |
|**subjects** | **List&lt;Object&gt;** | Scheduled trigger only: what it can check (&#x60;post&#x60;), with the facts of each. |  [optional] |
|**every** | **List&lt;String&gt;** |  |  [optional] |
|**times** | **Object** | Ad rule trigger only: the weekly set times it takes. |  [optional] |
|**filterOperators** | **List&lt;String&gt;** |  |  [optional] |
|**steps** | **List&lt;String&gt;** | The step types allowed after the trigger. For an event, only those its subject can reach. |  |
|**boost** | **Object** | Scheduled trigger only: the platforms, goals, most days and most boosts a day of &#x60;ads.boost_post&#x60;. |  [optional] |
|**limits** | **List&lt;String&gt;** |  |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| AD_RULE | &quot;ad_rule&quot; |
| EVENT | &quot;event&quot; |
| SCHEDULED | &quot;scheduled&quot; |
| SEQUENCE | &quot;sequence&quot; |
| COMMENT | &quot;comment&quot; |
| WORKFLOW | &quot;workflow&quot; |



## Enum: GroupEnum

| Name | Value |
|---- | -----|
| SOCIAL | &quot;social&quot; |
| MESSAGING | &quot;messaging&quot; |
| ADS | &quot;ads&quot; |



## Enum: ResourceGroupEnum

| Name | Value |
|---- | -----|
| MESSAGES | &quot;messages&quot; |
| ADS | &quot;ads&quot; |



