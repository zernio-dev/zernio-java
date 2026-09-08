

# BusinessAgentUiSkill


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** |  |  [optional] |
|**componentType** | [**ComponentTypeEnum**](#ComponentTypeEnum) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**instruction** | **String** | When to send the component and everything needed to fill its fields. |  |
|**flowId** | **Integer** | Required for component_type flow, rejected otherwise. |  [optional] |
|**id** | **String** |  |  |
|**createdAt** | **Integer** | Unix seconds. |  [optional] |
|**updatedAt** | **Integer** | Unix seconds. |  [optional] |



## Enum: ComponentTypeEnum

| Name | Value |
|---- | -----|
| CAROUSEL_QUICK_REPLY | &quot;carousel_quick_reply&quot; |
| CAROUSEL_URL | &quot;carousel_url&quot; |
| CTA_URL | &quot;cta_url&quot; |
| FLOW | &quot;flow&quot; |
| IMAGE | &quot;image&quot; |
| INTERACTIVE_LIST | &quot;interactive_list&quot; |
| INTERACTIVE_REPLY_BUTTONS | &quot;interactive_reply_buttons&quot; |
| LOCATION | &quot;location&quot; |
| LOCATION_REQUEST | &quot;location_request&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| DISABLED | &quot;disabled&quot; |



