

# InlineObject2Details

Structured context for SDK clients that want to render their own UX. Keys vary by `reason`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**freeTierAccountLimit** | **Integer** | How many accounts the free tier allows. Only set when reason&#x3D;free_tier_exceeded. |  [optional] |
|**currentAccountCount** | **Integer** | How many accounts the team currently has connected. Set when reason&#x3D;free_tier_exceeded or reason&#x3D;enterprise_required. |  [optional] |
|**hasPaymentMethod** | **Boolean** | Whether the team currently has a card on file in Stripe. Set when reason&#x3D;free_tier_exceeded or reason&#x3D;twitter_passthrough. |  [optional] |
|**publicAccountLimit** | **Integer** | Public pricing ceiling (the published cap beyond which an enterprise contract is required). Only set when reason&#x3D;enterprise_required. |  [optional] |
|**effectiveAccountLimit** | **Integer** | The cap actually applied to this team. Equals &#x60;public_account_limit&#x60; for organic teams; for teams with a per-customer override (grandfathered legacy customers, signed enterprise contracts) this can be higher. Only set when reason&#x3D;enterprise_required.  |  [optional] |



