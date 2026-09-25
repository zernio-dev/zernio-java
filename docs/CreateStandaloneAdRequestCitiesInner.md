

# CreateStandaloneAdRequestCitiesInner

## oneOf schemas
* [CreateStandaloneAdRequestCitiesInnerOneOf](CreateStandaloneAdRequestCitiesInnerOneOf.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateStandaloneAdRequestCitiesInner;
import dev.zernio.model.CreateStandaloneAdRequestCitiesInnerOneOf;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        CreateStandaloneAdRequestCitiesInner exampleCreateStandaloneAdRequestCitiesInner = new CreateStandaloneAdRequestCitiesInner();

        // create a new CreateStandaloneAdRequestCitiesInnerOneOf
        CreateStandaloneAdRequestCitiesInnerOneOf exampleCreateStandaloneAdRequestCitiesInnerOneOf = new CreateStandaloneAdRequestCitiesInnerOneOf();
        // set CreateStandaloneAdRequestCitiesInner to CreateStandaloneAdRequestCitiesInnerOneOf
        exampleCreateStandaloneAdRequestCitiesInner.setActualInstance(exampleCreateStandaloneAdRequestCitiesInnerOneOf);
        // to get back the CreateStandaloneAdRequestCitiesInnerOneOf set earlier
        CreateStandaloneAdRequestCitiesInnerOneOf testCreateStandaloneAdRequestCitiesInnerOneOf = (CreateStandaloneAdRequestCitiesInnerOneOf) exampleCreateStandaloneAdRequestCitiesInner.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set CreateStandaloneAdRequestCitiesInner to String
        exampleCreateStandaloneAdRequestCitiesInner.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleCreateStandaloneAdRequestCitiesInner.getActualInstance();
    }
}
```


