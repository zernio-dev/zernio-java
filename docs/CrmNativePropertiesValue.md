

# CrmNativePropertiesValue

## anyOf schemas
* [BigDecimal](BigDecimal.md)
* [Boolean](Boolean.md)
* [String](String.md)

NOTE: this class is nullable.

## Example
```java
// Import classes:
import dev.zernio.model.CrmNativePropertiesValue;
import dev.zernio.model.BigDecimal;
import dev.zernio.model.Boolean;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        CrmNativePropertiesValue exampleCrmNativePropertiesValue = new CrmNativePropertiesValue();

        // create a new BigDecimal
        BigDecimal exampleBigDecimal = new BigDecimal();
        // set CrmNativePropertiesValue to BigDecimal
        exampleCrmNativePropertiesValue.setActualInstance(exampleBigDecimal);
        // to get back the BigDecimal set earlier
        BigDecimal testBigDecimal = (BigDecimal) exampleCrmNativePropertiesValue.getActualInstance();

        // create a new Boolean
        Boolean exampleBoolean = new Boolean();
        // set CrmNativePropertiesValue to Boolean
        exampleCrmNativePropertiesValue.setActualInstance(exampleBoolean);
        // to get back the Boolean set earlier
        Boolean testBoolean = (Boolean) exampleCrmNativePropertiesValue.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set CrmNativePropertiesValue to String
        exampleCrmNativePropertiesValue.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleCrmNativePropertiesValue.getActualInstance();
    }
}
```


