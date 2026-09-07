

# AddAdKeywordsRequestKeywordsInner

## anyOf schemas
* [AddAdKeywordsRequestKeywordsInnerAnyOf](AddAdKeywordsRequestKeywordsInnerAnyOf.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.AddAdKeywordsRequestKeywordsInner;
import dev.zernio.model.AddAdKeywordsRequestKeywordsInnerAnyOf;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        AddAdKeywordsRequestKeywordsInner exampleAddAdKeywordsRequestKeywordsInner = new AddAdKeywordsRequestKeywordsInner();

        // create a new AddAdKeywordsRequestKeywordsInnerAnyOf
        AddAdKeywordsRequestKeywordsInnerAnyOf exampleAddAdKeywordsRequestKeywordsInnerAnyOf = new AddAdKeywordsRequestKeywordsInnerAnyOf();
        // set AddAdKeywordsRequestKeywordsInner to AddAdKeywordsRequestKeywordsInnerAnyOf
        exampleAddAdKeywordsRequestKeywordsInner.setActualInstance(exampleAddAdKeywordsRequestKeywordsInnerAnyOf);
        // to get back the AddAdKeywordsRequestKeywordsInnerAnyOf set earlier
        AddAdKeywordsRequestKeywordsInnerAnyOf testAddAdKeywordsRequestKeywordsInnerAnyOf = (AddAdKeywordsRequestKeywordsInnerAnyOf) exampleAddAdKeywordsRequestKeywordsInner.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set AddAdKeywordsRequestKeywordsInner to String
        exampleAddAdKeywordsRequestKeywordsInner.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleAddAdKeywordsRequestKeywordsInner.getActualInstance();
    }
}
```


