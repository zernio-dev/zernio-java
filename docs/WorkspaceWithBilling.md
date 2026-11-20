

# WorkspaceWithBilling

A workspace, plus `billing` for owners, admins and billing admins.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**personal** | **Boolean** | True for the caller&#39;s own Personal workspace, which is never shared, renamed or deleted. |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | The caller&#39;s role in this workspace. |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**deletionScheduledAt** | **OffsetDateTime** | When a scheduled deletion runs; null when none is scheduled. |  [optional] |
|**billing** | [**WorkspaceWithBillingAllOfBilling**](WorkspaceWithBillingAllOfBilling.md) |  |  [optional] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| OWNER | &quot;owner&quot; |
| ADMIN | &quot;admin&quot; |
| BILLING_ADMIN | &quot;billing_admin&quot; |
| MEMBER | &quot;member&quot; |
| VIEWER | &quot;viewer&quot; |



