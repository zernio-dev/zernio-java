

# OnRcsAgentStatusUpdatedRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**test** | **Boolean** | Always true when present: only a sample sent by POST /v1/webhooks/test with an event carries it. Real deliveries never do. |  [optional] |
|**id** | **String** | Stable webhook event ID: the dedupe key, also sent as the X-Zernio-Event-Id header and identical on every retry and redelivery. It identifies the event only, never an account or other resource. |  [optional] |
|**event** | [**EventEnum**](#EventEnum) |  |  [optional] |
|**timestamp** | **OffsetDateTime** | UTC time at which Zernio generated this event (set once when the event payload is built, before delivery is queued). Retries and redeliveries keep the original value, so it reflects the event, not the delivery attempt. |  [optional] |
|**agent** | [**OnRcsAgentStatusUpdatedRequestAgent**](OnRcsAgentStatusUpdatedRequestAgent.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**reason** | **String** | Our review note on changes_requested, the reason on rejected, or why a launch filing bounced back to testing. |  [optional] |



## Enum: EventEnum

| Name | Value |
|---- | -----|
| RCS_AGENT_STATUS_UPDATED | &quot;rcs.agent.status_updated&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CHANGES_REQUESTED | &quot;changes_requested&quot; |
| BRAND_VETTING | &quot;brand_vetting&quot; |
| AGENT_REVIEW | &quot;agent_review&quot; |
| TESTING | &quot;testing&quot; |
| LAUNCH_REVIEW | &quot;launch_review&quot; |
| LAUNCHING | &quot;launching&quot; |
| LIVE | &quot;live&quot; |
| REJECTED | &quot;rejected&quot; |
| DEACTIVATED | &quot;deactivated&quot; |



