

# FoodMenuItemAttributes


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**price** | [**Money**](Money.md) |  |  [optional] |
|**spiciness** | [**SpicinessEnum**](#SpicinessEnum) | Spiciness level (e.g. MILD, MEDIUM, HOT) |  [optional] |
|**allergen** | **List&lt;String&gt;** | Allergens (e.g. DAIRY, GLUTEN, SHELLFISH) |  [optional] |
|**dietaryRestriction** | **List&lt;String&gt;** | Dietary labels (e.g. VEGETARIAN, VEGAN, GLUTEN_FREE) |  [optional] |
|**servesNumPeople** | **Integer** | Number of people the item serves |  [optional] |
|**preparationMethods** | **List&lt;String&gt;** | Preparation methods (e.g. GRILLED, FRIED) |  [optional] |
|**mediaKeys** | **List&lt;String&gt;** | Media references for item photos |  [optional] |



## Enum: SpicinessEnum

| Name | Value |
|---- | -----|
| SPICINESS_UNSPECIFIED | &quot;SPICINESS_UNSPECIFIED&quot; |
| MILD | &quot;MILD&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HOT | &quot;HOT&quot; |



