

# AutomationBacktest

What the automation would have done on each past day, replayed on stored daily metrics. Nothing is changed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**from** | **LocalDate** | The first day replayed, in the ad account timezone. |  |
|**to** | **LocalDate** | The last day replayed, yesterday in the ad account timezone. |  |
|**timezone** | **String** |  |  |
|**timezoneAssumed** | **Boolean** | True when the ad account timezone is unknown and UTC was used. |  |
|**currency** | **String** |  |  |
|**totals** | [**AutomationBacktestTotals**](AutomationBacktestTotals.md) |  |  |
|**days** | [**List&lt;AutomationBacktestDay&gt;**](AutomationBacktestDay.md) |  |  |
|**notes** | [**List&lt;AutomationBacktestNotesInner&gt;**](AutomationBacktestNotesInner.md) | What this replay could not know, for example that budgets have no history. |  |



