

# WhatsAppCarouselCardComponent

## oneOf schemas
* [WhatsAppBodyComponent](WhatsAppBodyComponent.md)
* [WhatsAppButtonsComponent](WhatsAppButtonsComponent.md)
* [WhatsAppHeaderComponent](WhatsAppHeaderComponent.md)

## Example
```java
// Import classes:
import dev.zernio.model.WhatsAppCarouselCardComponent;
import dev.zernio.model.WhatsAppBodyComponent;
import dev.zernio.model.WhatsAppButtonsComponent;
import dev.zernio.model.WhatsAppHeaderComponent;

public class Example {
    public static void main(String[] args) {
        WhatsAppCarouselCardComponent exampleWhatsAppCarouselCardComponent = new WhatsAppCarouselCardComponent();

        // create a new WhatsAppBodyComponent
        WhatsAppBodyComponent exampleWhatsAppBodyComponent = new WhatsAppBodyComponent();
        // set WhatsAppCarouselCardComponent to WhatsAppBodyComponent
        exampleWhatsAppCarouselCardComponent.setActualInstance(exampleWhatsAppBodyComponent);
        // to get back the WhatsAppBodyComponent set earlier
        WhatsAppBodyComponent testWhatsAppBodyComponent = (WhatsAppBodyComponent) exampleWhatsAppCarouselCardComponent.getActualInstance();

        // create a new WhatsAppButtonsComponent
        WhatsAppButtonsComponent exampleWhatsAppButtonsComponent = new WhatsAppButtonsComponent();
        // set WhatsAppCarouselCardComponent to WhatsAppButtonsComponent
        exampleWhatsAppCarouselCardComponent.setActualInstance(exampleWhatsAppButtonsComponent);
        // to get back the WhatsAppButtonsComponent set earlier
        WhatsAppButtonsComponent testWhatsAppButtonsComponent = (WhatsAppButtonsComponent) exampleWhatsAppCarouselCardComponent.getActualInstance();

        // create a new WhatsAppHeaderComponent
        WhatsAppHeaderComponent exampleWhatsAppHeaderComponent = new WhatsAppHeaderComponent();
        // set WhatsAppCarouselCardComponent to WhatsAppHeaderComponent
        exampleWhatsAppCarouselCardComponent.setActualInstance(exampleWhatsAppHeaderComponent);
        // to get back the WhatsAppHeaderComponent set earlier
        WhatsAppHeaderComponent testWhatsAppHeaderComponent = (WhatsAppHeaderComponent) exampleWhatsAppCarouselCardComponent.getActualInstance();
    }
}
```


