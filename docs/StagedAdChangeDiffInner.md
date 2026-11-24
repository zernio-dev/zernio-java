

# StagedAdChangeDiffInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**field** | **String** | The dotted path of the value in the request body. |  |
|**before** | **Object** |  |  |
|**after** | **Object** |  |  |
|**beforeAvailable** | **Boolean** | False when &#x60;before&#x60; is unknown: the live read of the object does not return this field, or the change creates the object. The field is still staged. |  |
|**added** | **List&lt;Object&gt;** | Only on a list of plain values (strings or numbers) with &#x60;beforeAvailable&#x60; true: the values in &#x60;after&#x60; that are not in &#x60;before&#x60;. Order is ignored. |  [optional] |
|**removed** | **List&lt;Object&gt;** | Only on a list of plain values (strings or numbers) with &#x60;beforeAvailable&#x60; true: the values in &#x60;before&#x60; that are not in &#x60;after&#x60;. Order is ignored. |  [optional] |



