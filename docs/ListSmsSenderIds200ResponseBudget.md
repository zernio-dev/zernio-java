

# ListSmsSenderIds200ResponseBudget

Workspace-wide daily sending budget, shared by every sender ID (resets midnight UTC).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cap** | **Integer** | Daily message cap (raisable via &#x60;/v1/sms/sender-ids/limit-request&#x60;). |  [optional] |
|**usedToday** | **Integer** | Messages already counted against today&#39;s cap. |  [optional] |
|**level** | **Integer** | Cap tier (Level 1 &#x3D; 500/day). |  [optional] |
|**pendingRequest** | [**ListSmsSenderIds200ResponseBudgetPendingRequest**](ListSmsSenderIds200ResponseBudgetPendingRequest.md) |  |  [optional] |



