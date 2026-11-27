

# ListLeads200ResponseMeta


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lastCheckedAt** | **OffsetDateTime** | Meta only, present when &#x60;accountId&#x60; is passed: when the recovery pass that catches leads the webhook missed last ran for the Page, failed or parked passes included, so not proof the forms were read. Null when no leads matched or before the first pass. |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] |
|**contentNotRetained** | **Boolean** | True when this team does not retain content. Answers and form names are not searchable with &#x60;q&#x60;. |  [optional] |



