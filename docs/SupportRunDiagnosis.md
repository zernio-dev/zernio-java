

# SupportRunDiagnosis


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) | What kind of problem the answer describes. New values may be added: treat any value you do not recognize as &#x60;other&#x60;. |  |
|**cause** | **String** | The cause the answer gives, in one sentence. Null when the answer reports no problem, for example a how-to question. |  |
|**fixSteps** | **List&lt;String&gt;** | The steps the answer recommends, in order. Empty when it recommends none. |  |
|**docsLinks** | **List&lt;String&gt;** | Links to docs.zernio.com that the answer itself cites. Empty when it cites none. |  |
|**whoMustAct** | [**WhoMustActEnum**](#WhoMustActEnum) | Who has to act to resolve it: you (&#x60;integrator&#x60;), your end user, Zernio, the social platform, or nobody. New values may be added: treat any value you do not recognize as &#x60;none&#x60;. |  |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| ACCOUNT_CONNECTION | &quot;account_connection&quot; |
| CONTENT_REJECTED | &quot;content_rejected&quot; |
| RATE_LIMITED | &quot;rate_limited&quot; |
| PLATFORM_ISSUE | &quot;platform_issue&quot; |
| ZERNIO_ISSUE | &quot;zernio_issue&quot; |
| BILLING | &quot;billing&quot; |
| CONFIGURATION | &quot;configuration&quot; |
| HOW_TO | &quot;how_to&quot; |
| OTHER | &quot;other&quot; |



## Enum: WhoMustActEnum

| Name | Value |
|---- | -----|
| INTEGRATOR | &quot;integrator&quot; |
| END_USER | &quot;end_user&quot; |
| ZERNIO | &quot;zernio&quot; |
| PLATFORM | &quot;platform&quot; |
| NONE | &quot;none&quot; |



