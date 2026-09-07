

# KeywordEntry

A Google Search keyword: a bare string (BROAD match), or an object naming the match type.

## oneOf schemas
* [AddAdKeywordsRequestKeywordsInnerAnyOf](AddAdKeywordsRequestKeywordsInnerAnyOf.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.KeywordEntry;
import dev.zernio.model.AddAdKeywordsRequestKeywordsInnerAnyOf;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        KeywordEntry exampleKeywordEntry = new KeywordEntry();

        // create a new AddAdKeywordsRequestKeywordsInnerAnyOf
        AddAdKeywordsRequestKeywordsInnerAnyOf exampleAddAdKeywordsRequestKeywordsInnerAnyOf = new AddAdKeywordsRequestKeywordsInnerAnyOf();
        // set KeywordEntry to AddAdKeywordsRequestKeywordsInnerAnyOf
        exampleKeywordEntry.setActualInstance(exampleAddAdKeywordsRequestKeywordsInnerAnyOf);
        // to get back the AddAdKeywordsRequestKeywordsInnerAnyOf set earlier
        AddAdKeywordsRequestKeywordsInnerAnyOf testAddAdKeywordsRequestKeywordsInnerAnyOf = (AddAdKeywordsRequestKeywordsInnerAnyOf) exampleKeywordEntry.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set KeywordEntry to String
        exampleKeywordEntry.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleKeywordEntry.getActualInstance();
    }
}
```


