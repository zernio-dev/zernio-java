

# AutomationStepOneOf1

Turns objects back on once their cooldown has passed. A rule on set `times` does not wait: it restarts only what a rule on set times paused.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**IdEnum**](#IdEnum) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**includeManuallyPaused** | **Boolean** | Also objects a person paused. Without it only what this automation paused is turned back on. |  [optional] |



## Enum: IdEnum

| Name | Value |
|---- | -----|
| ACTIVATE | &quot;activate&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ADS_ACTIVATE | &quot;ads.activate&quot; |



