

# CheckPhoneNumberAvailability200ResponseAreaAvailabilityInStockInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ndc** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**count** | **Integer** | Numbers we can sell there: the carrier count minus the numbers we hold back (WhatsApp refused them or another order holds them). |  [optional] |
|**ndcs** | **List&lt;String&gt;** | Every area code of the city, deepest first (Madrid: 915, 911, 910, ...). &#x60;ndc&#x60; is the one an order is placed against. |  [optional] |
|**aliases** | **List&lt;String&gt;** | Other names the area answers to, present only when it has some (Milano for Milan, Sevilla for Seville). |  [optional] |



