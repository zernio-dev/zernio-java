

# CommerceOrderFulfillmentsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The shipment (fulfillment) id. Entries of one shipment with several tracking numbers share it. |  [optional] |
|**carrierName** | **String** |  |  [optional] |
|**trackingNumber** | **String** |  |  [optional] |
|**trackingUrl** | **String** |  |  [optional] |
|**deliveryStatus** | [**DeliveryStatusEnum**](#DeliveryStatusEnum) | Where the shipment is. pending means no carrier scan yet. Null when the platform has no delivery tracking for it. Shopify only knows it when the carrier sends tracking events. |  [optional] |
|**platformDeliveryStatus** | **String** | The platform&#39;s raw value, e.g. Shopify ATTEMPTED_DELIVERY. |  [optional] |
|**estimatedDeliveryAt** | **OffsetDateTime** |  |  [optional] |
|**inTransitAt** | **OffsetDateTime** |  |  [optional] |
|**deliveredAt** | **OffsetDateTime** |  |  [optional] |



## Enum: DeliveryStatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| IN_TRANSIT | &quot;in_transit&quot; |
| DELAYED | &quot;delayed&quot; |
| OUT_FOR_DELIVERY | &quot;out_for_delivery&quot; |
| READY_FOR_PICKUP | &quot;ready_for_pickup&quot; |
| ATTEMPTED_DELIVERY | &quot;attempted_delivery&quot; |
| DELIVERED | &quot;delivered&quot; |
| FAILED | &quot;failed&quot; |
| CANCELLED | &quot;cancelled&quot; |



