

# ConnectHandoffLink

Only with `handoff=true`: the link to show as a QR code.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** | Pass to &#x60;GET /v1/connect/handoffs/{handoffId}&#x60;. |  [optional] |
|**url** | **URI** | Short link to encode in the QR code. It opens the welcome screen on the phone. |  [optional] |
|**expiresAt** | **OffsetDateTime** | When &#x60;url&#x60; stops working (30 minutes). |  [optional] |



