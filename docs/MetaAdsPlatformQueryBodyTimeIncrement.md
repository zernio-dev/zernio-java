

# MetaAdsPlatformQueryBodyTimeIncrement

Days per row, 1 to 90, or monthly or all_days.

## anyOf schemas
* [Integer](Integer.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.MetaAdsPlatformQueryBodyTimeIncrement;
import dev.zernio.model.Integer;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        MetaAdsPlatformQueryBodyTimeIncrement exampleMetaAdsPlatformQueryBodyTimeIncrement = new MetaAdsPlatformQueryBodyTimeIncrement();

        // create a new Integer
        Integer exampleInteger = new Integer();
        // set MetaAdsPlatformQueryBodyTimeIncrement to Integer
        exampleMetaAdsPlatformQueryBodyTimeIncrement.setActualInstance(exampleInteger);
        // to get back the Integer set earlier
        Integer testInteger = (Integer) exampleMetaAdsPlatformQueryBodyTimeIncrement.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set MetaAdsPlatformQueryBodyTimeIncrement to String
        exampleMetaAdsPlatformQueryBodyTimeIncrement.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleMetaAdsPlatformQueryBodyTimeIncrement.getActualInstance();
    }
}
```


