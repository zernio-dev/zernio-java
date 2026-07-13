

# InlineObject2Details

Structured context for SDK clients that want to render their own UX. Keys vary by `reason`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**freeTierAccountLimit** | **Integer** | How many accounts the free tier allows. Only set when reason&#x3D;free_tier_exceeded. |  [optional] |
|**currentAccountCount** | **Integer** | How many accounts the team currently has connected. Set when reason&#x3D;free_tier_exceeded or reason&#x3D;enterprise_required. |  [optional] |
|**hasPaymentMethod** | **Boolean** | Whether the team currently has a card on file in Stripe. Set when reason&#x3D;free_tier_exceeded or reason&#x3D;twitter_passthrough. |  [optional] |
|**effectiveAccountLimit** | **Integer** | The negotiated connected-account cap from the team&#39;s enterprise contract. Self-service teams have no cap and never receive this reason. Only set when reason&#x3D;enterprise_required.  |  [optional] |



