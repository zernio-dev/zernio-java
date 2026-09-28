

# RcsSuggestion

A tappable chip. Labels are max 25 characters. postbackData (max 2048) comes back unchanged in message.received metadata as postbackPayload when tapped; defaults to the label. Any string works, JSON included: values outside A-Z a-z 0-9 - _ . are encoded on the wire and decoded for you.

## oneOf schemas
* [RcsSuggestionOneOf](RcsSuggestionOneOf.md)
* [RcsSuggestionOneOf1](RcsSuggestionOneOf1.md)
* [RcsSuggestionOneOf2](RcsSuggestionOneOf2.md)
* [RcsSuggestionOneOf3](RcsSuggestionOneOf3.md)
* [RcsSuggestionOneOf4](RcsSuggestionOneOf4.md)
* [RcsSuggestionOneOf5](RcsSuggestionOneOf5.md)

## Example
```java
// Import classes:
import dev.zernio.model.RcsSuggestion;
import dev.zernio.model.RcsSuggestionOneOf;
import dev.zernio.model.RcsSuggestionOneOf1;
import dev.zernio.model.RcsSuggestionOneOf2;
import dev.zernio.model.RcsSuggestionOneOf3;
import dev.zernio.model.RcsSuggestionOneOf4;
import dev.zernio.model.RcsSuggestionOneOf5;

public class Example {
    public static void main(String[] args) {
        RcsSuggestion exampleRcsSuggestion = new RcsSuggestion();

        // create a new RcsSuggestionOneOf
        RcsSuggestionOneOf exampleRcsSuggestionOneOf = new RcsSuggestionOneOf();
        // set RcsSuggestion to RcsSuggestionOneOf
        exampleRcsSuggestion.setActualInstance(exampleRcsSuggestionOneOf);
        // to get back the RcsSuggestionOneOf set earlier
        RcsSuggestionOneOf testRcsSuggestionOneOf = (RcsSuggestionOneOf) exampleRcsSuggestion.getActualInstance();

        // create a new RcsSuggestionOneOf1
        RcsSuggestionOneOf1 exampleRcsSuggestionOneOf1 = new RcsSuggestionOneOf1();
        // set RcsSuggestion to RcsSuggestionOneOf1
        exampleRcsSuggestion.setActualInstance(exampleRcsSuggestionOneOf1);
        // to get back the RcsSuggestionOneOf1 set earlier
        RcsSuggestionOneOf1 testRcsSuggestionOneOf1 = (RcsSuggestionOneOf1) exampleRcsSuggestion.getActualInstance();

        // create a new RcsSuggestionOneOf2
        RcsSuggestionOneOf2 exampleRcsSuggestionOneOf2 = new RcsSuggestionOneOf2();
        // set RcsSuggestion to RcsSuggestionOneOf2
        exampleRcsSuggestion.setActualInstance(exampleRcsSuggestionOneOf2);
        // to get back the RcsSuggestionOneOf2 set earlier
        RcsSuggestionOneOf2 testRcsSuggestionOneOf2 = (RcsSuggestionOneOf2) exampleRcsSuggestion.getActualInstance();

        // create a new RcsSuggestionOneOf3
        RcsSuggestionOneOf3 exampleRcsSuggestionOneOf3 = new RcsSuggestionOneOf3();
        // set RcsSuggestion to RcsSuggestionOneOf3
        exampleRcsSuggestion.setActualInstance(exampleRcsSuggestionOneOf3);
        // to get back the RcsSuggestionOneOf3 set earlier
        RcsSuggestionOneOf3 testRcsSuggestionOneOf3 = (RcsSuggestionOneOf3) exampleRcsSuggestion.getActualInstance();

        // create a new RcsSuggestionOneOf4
        RcsSuggestionOneOf4 exampleRcsSuggestionOneOf4 = new RcsSuggestionOneOf4();
        // set RcsSuggestion to RcsSuggestionOneOf4
        exampleRcsSuggestion.setActualInstance(exampleRcsSuggestionOneOf4);
        // to get back the RcsSuggestionOneOf4 set earlier
        RcsSuggestionOneOf4 testRcsSuggestionOneOf4 = (RcsSuggestionOneOf4) exampleRcsSuggestion.getActualInstance();

        // create a new RcsSuggestionOneOf5
        RcsSuggestionOneOf5 exampleRcsSuggestionOneOf5 = new RcsSuggestionOneOf5();
        // set RcsSuggestion to RcsSuggestionOneOf5
        exampleRcsSuggestion.setActualInstance(exampleRcsSuggestionOneOf5);
        // to get back the RcsSuggestionOneOf5 set earlier
        RcsSuggestionOneOf5 testRcsSuggestionOneOf5 = (RcsSuggestionOneOf5) exampleRcsSuggestion.getActualInstance();
    }
}
```


