

# BillingSnapshot

Account billing state — plan, cycle, balance, spend caps, and payment / access status. Returned by `GET /v1/billing`. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingSystem** | [**BillingSystemEnum**](#BillingSystemEnum) |  |  [optional] |
|**plan** | [**BillingSnapshotPlan**](BillingSnapshotPlan.md) |  |  [optional] |
|**period** | [**BillingSnapshotPeriod**](BillingSnapshotPeriod.md) |  |  [optional] |
|**balance** | [**BillingSnapshotBalance**](BillingSnapshotBalance.md) |  |  [optional] |
|**caps** | [**BillingSnapshotCaps**](BillingSnapshotCaps.md) |  |  [optional] |
|**status** | [**BillingSnapshotStatus**](BillingSnapshotStatus.md) |  |  [optional] |
|**legacy** | [**BillingSnapshotLegacy**](BillingSnapshotLegacy.md) |  |  [optional] |



## Enum: BillingSystemEnum

| Name | Value |
|---- | -----|
| METRONOME | &quot;metronome&quot; |
| STRIPE | &quot;stripe&quot; |



