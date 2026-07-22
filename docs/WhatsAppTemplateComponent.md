

# WhatsAppTemplateComponent

## oneOf schemas
* [WhatsAppBodyComponent](WhatsAppBodyComponent.md)
* [WhatsAppButtonsComponent](WhatsAppButtonsComponent.md)
* [WhatsAppCarouselComponent](WhatsAppCarouselComponent.md)
* [WhatsAppFooterComponent](WhatsAppFooterComponent.md)
* [WhatsAppHeaderComponent](WhatsAppHeaderComponent.md)
* [WhatsAppLimitedTimeOfferComponent](WhatsAppLimitedTimeOfferComponent.md)

## Example
```java
// Import classes:
import dev.zernio.model.WhatsAppTemplateComponent;
import dev.zernio.model.WhatsAppBodyComponent;
import dev.zernio.model.WhatsAppButtonsComponent;
import dev.zernio.model.WhatsAppCarouselComponent;
import dev.zernio.model.WhatsAppFooterComponent;
import dev.zernio.model.WhatsAppHeaderComponent;
import dev.zernio.model.WhatsAppLimitedTimeOfferComponent;

public class Example {
    public static void main(String[] args) {
        WhatsAppTemplateComponent exampleWhatsAppTemplateComponent = new WhatsAppTemplateComponent();

        // create a new WhatsAppBodyComponent
        WhatsAppBodyComponent exampleWhatsAppBodyComponent = new WhatsAppBodyComponent();
        // set WhatsAppTemplateComponent to WhatsAppBodyComponent
        exampleWhatsAppTemplateComponent.setActualInstance(exampleWhatsAppBodyComponent);
        // to get back the WhatsAppBodyComponent set earlier
        WhatsAppBodyComponent testWhatsAppBodyComponent = (WhatsAppBodyComponent) exampleWhatsAppTemplateComponent.getActualInstance();

        // create a new WhatsAppButtonsComponent
        WhatsAppButtonsComponent exampleWhatsAppButtonsComponent = new WhatsAppButtonsComponent();
        // set WhatsAppTemplateComponent to WhatsAppButtonsComponent
        exampleWhatsAppTemplateComponent.setActualInstance(exampleWhatsAppButtonsComponent);
        // to get back the WhatsAppButtonsComponent set earlier
        WhatsAppButtonsComponent testWhatsAppButtonsComponent = (WhatsAppButtonsComponent) exampleWhatsAppTemplateComponent.getActualInstance();

        // create a new WhatsAppCarouselComponent
        WhatsAppCarouselComponent exampleWhatsAppCarouselComponent = new WhatsAppCarouselComponent();
        // set WhatsAppTemplateComponent to WhatsAppCarouselComponent
        exampleWhatsAppTemplateComponent.setActualInstance(exampleWhatsAppCarouselComponent);
        // to get back the WhatsAppCarouselComponent set earlier
        WhatsAppCarouselComponent testWhatsAppCarouselComponent = (WhatsAppCarouselComponent) exampleWhatsAppTemplateComponent.getActualInstance();

        // create a new WhatsAppFooterComponent
        WhatsAppFooterComponent exampleWhatsAppFooterComponent = new WhatsAppFooterComponent();
        // set WhatsAppTemplateComponent to WhatsAppFooterComponent
        exampleWhatsAppTemplateComponent.setActualInstance(exampleWhatsAppFooterComponent);
        // to get back the WhatsAppFooterComponent set earlier
        WhatsAppFooterComponent testWhatsAppFooterComponent = (WhatsAppFooterComponent) exampleWhatsAppTemplateComponent.getActualInstance();

        // create a new WhatsAppHeaderComponent
        WhatsAppHeaderComponent exampleWhatsAppHeaderComponent = new WhatsAppHeaderComponent();
        // set WhatsAppTemplateComponent to WhatsAppHeaderComponent
        exampleWhatsAppTemplateComponent.setActualInstance(exampleWhatsAppHeaderComponent);
        // to get back the WhatsAppHeaderComponent set earlier
        WhatsAppHeaderComponent testWhatsAppHeaderComponent = (WhatsAppHeaderComponent) exampleWhatsAppTemplateComponent.getActualInstance();

        // create a new WhatsAppLimitedTimeOfferComponent
        WhatsAppLimitedTimeOfferComponent exampleWhatsAppLimitedTimeOfferComponent = new WhatsAppLimitedTimeOfferComponent();
        // set WhatsAppTemplateComponent to WhatsAppLimitedTimeOfferComponent
        exampleWhatsAppTemplateComponent.setActualInstance(exampleWhatsAppLimitedTimeOfferComponent);
        // to get back the WhatsAppLimitedTimeOfferComponent set earlier
        WhatsAppLimitedTimeOfferComponent testWhatsAppLimitedTimeOfferComponent = (WhatsAppLimitedTimeOfferComponent) exampleWhatsAppTemplateComponent.getActualInstance();
    }
}
```


