

# XArticleEntity

Entity keys must be unique decimal strings matching their zero-based array index (`\"0\"`, `\"1\"`, ...).

## oneOf schemas
* [XArticleEntityOneOf](XArticleEntityOneOf.md)
* [XArticleEntityOneOf1](XArticleEntityOneOf1.md)
* [XArticleEntityOneOf2](XArticleEntityOneOf2.md)
* [XArticleEntityOneOf3](XArticleEntityOneOf3.md)
* [XArticleEntityOneOf4](XArticleEntityOneOf4.md)
* [XArticleEntityOneOf5](XArticleEntityOneOf5.md)

## Example
```java
// Import classes:
import dev.zernio.model.XArticleEntity;
import dev.zernio.model.XArticleEntityOneOf;
import dev.zernio.model.XArticleEntityOneOf1;
import dev.zernio.model.XArticleEntityOneOf2;
import dev.zernio.model.XArticleEntityOneOf3;
import dev.zernio.model.XArticleEntityOneOf4;
import dev.zernio.model.XArticleEntityOneOf5;

public class Example {
    public static void main(String[] args) {
        XArticleEntity exampleXArticleEntity = new XArticleEntity();

        // create a new XArticleEntityOneOf
        XArticleEntityOneOf exampleXArticleEntityOneOf = new XArticleEntityOneOf();
        // set XArticleEntity to XArticleEntityOneOf
        exampleXArticleEntity.setActualInstance(exampleXArticleEntityOneOf);
        // to get back the XArticleEntityOneOf set earlier
        XArticleEntityOneOf testXArticleEntityOneOf = (XArticleEntityOneOf) exampleXArticleEntity.getActualInstance();

        // create a new XArticleEntityOneOf1
        XArticleEntityOneOf1 exampleXArticleEntityOneOf1 = new XArticleEntityOneOf1();
        // set XArticleEntity to XArticleEntityOneOf1
        exampleXArticleEntity.setActualInstance(exampleXArticleEntityOneOf1);
        // to get back the XArticleEntityOneOf1 set earlier
        XArticleEntityOneOf1 testXArticleEntityOneOf1 = (XArticleEntityOneOf1) exampleXArticleEntity.getActualInstance();

        // create a new XArticleEntityOneOf2
        XArticleEntityOneOf2 exampleXArticleEntityOneOf2 = new XArticleEntityOneOf2();
        // set XArticleEntity to XArticleEntityOneOf2
        exampleXArticleEntity.setActualInstance(exampleXArticleEntityOneOf2);
        // to get back the XArticleEntityOneOf2 set earlier
        XArticleEntityOneOf2 testXArticleEntityOneOf2 = (XArticleEntityOneOf2) exampleXArticleEntity.getActualInstance();

        // create a new XArticleEntityOneOf3
        XArticleEntityOneOf3 exampleXArticleEntityOneOf3 = new XArticleEntityOneOf3();
        // set XArticleEntity to XArticleEntityOneOf3
        exampleXArticleEntity.setActualInstance(exampleXArticleEntityOneOf3);
        // to get back the XArticleEntityOneOf3 set earlier
        XArticleEntityOneOf3 testXArticleEntityOneOf3 = (XArticleEntityOneOf3) exampleXArticleEntity.getActualInstance();

        // create a new XArticleEntityOneOf4
        XArticleEntityOneOf4 exampleXArticleEntityOneOf4 = new XArticleEntityOneOf4();
        // set XArticleEntity to XArticleEntityOneOf4
        exampleXArticleEntity.setActualInstance(exampleXArticleEntityOneOf4);
        // to get back the XArticleEntityOneOf4 set earlier
        XArticleEntityOneOf4 testXArticleEntityOneOf4 = (XArticleEntityOneOf4) exampleXArticleEntity.getActualInstance();

        // create a new XArticleEntityOneOf5
        XArticleEntityOneOf5 exampleXArticleEntityOneOf5 = new XArticleEntityOneOf5();
        // set XArticleEntity to XArticleEntityOneOf5
        exampleXArticleEntity.setActualInstance(exampleXArticleEntityOneOf5);
        // to get back the XArticleEntityOneOf5 set earlier
        XArticleEntityOneOf5 testXArticleEntityOneOf5 = (XArticleEntityOneOf5) exampleXArticleEntity.getActualInstance();
    }
}
```


