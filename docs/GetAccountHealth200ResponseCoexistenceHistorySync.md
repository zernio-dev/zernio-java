

# GetAccountHealth200ResponseCoexistenceHistorySync

WhatsApp accounts only. The outcome of the latest chat history request Zernio sent Meta for a coexistence number, read from the account (not a live probe). Null when no request ran for the current connection, and on numbers that are not in coexistence.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | - &#x60;requested&#x60;: Meta accepted the request and has not sent history yet, which can take a while. - &#x60;imported&#x60;: Meta sent chat history to this account, including history a reconnect kept. - &#x60;declined&#x60;: the business chose not to share its chat history in Meta&#39;s window. - &#x60;already_synced&#x60;: Meta refused the request because an earlier connection already used the number&#39;s one history share. The description above says how to get a new import. - &#x60;refused&#x60;: Meta refused it for another reason.  |  [optional] |
|**requestId** | **String** | The id of the last history request Meta accepted, kept across reconnects. Quote it in a Meta support case. |  [optional] |
|**refusedAt** | **OffsetDateTime** | When Meta refused the latest request. Null when it was accepted. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| REQUESTED | &quot;requested&quot; |
| IMPORTED | &quot;imported&quot; |
| DECLINED | &quot;declined&quot; |
| ALREADY_SYNCED | &quot;already_synced&quot; |
| REFUSED | &quot;refused&quot; |



