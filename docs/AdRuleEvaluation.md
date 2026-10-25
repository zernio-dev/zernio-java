

# AdRuleEvaluation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**evaluatedAt** | **OffsetDateTime** |  |  |
|**today** | **LocalDate** | The ad account&#39;s calendar date the windows were resolved against. |  |
|**timezone** | **String** | IANA timezone of the ad account. |  |
|**timezoneAssumed** | **Boolean** | True when the ad account has no known timezone and UTC was assumed. |  |
|**currency** | **String** |  |  |
|**matched** | **Integer** | How many objects meet every condition. |  |
|**objects** | [**List&lt;AdRuleObjectEvaluation&gt;**](AdRuleObjectEvaluation.md) | Every delivering campaign or ad set in scope (for an &#x60;activate&#x60; rule, the rule-paused ones it may reactivate). |  |



