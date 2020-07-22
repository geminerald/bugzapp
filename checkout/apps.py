from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        """
        Loads the checkout signals upon loading the page
        """
        import checkout.signals
