

# KeywordEntry

A Google Search keyword: a bare string (BROAD match), or an object naming the match type.

## oneOf schemas
* [KeywordEntryOneOf](KeywordEntryOneOf.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.KeywordEntry;
import dev.zernio.model.KeywordEntryOneOf;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        KeywordEntry exampleKeywordEntry = new KeywordEntry();

        // create a new KeywordEntryOneOf
        KeywordEntryOneOf exampleKeywordEntryOneOf = new KeywordEntryOneOf();
        // set KeywordEntry to KeywordEntryOneOf
        exampleKeywordEntry.setActualInstance(exampleKeywordEntryOneOf);
        // to get back the KeywordEntryOneOf set earlier
        KeywordEntryOneOf testKeywordEntryOneOf = (KeywordEntryOneOf) exampleKeywordEntry.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set KeywordEntry to String
        exampleKeywordEntry.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleKeywordEntry.getActualInstance();
    }
}
```


