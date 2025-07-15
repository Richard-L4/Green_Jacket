from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form for collecting user order information.
    Tied to the Order model and includes styling, placeholder setup,
    and label adjustments in the init method.
    """

    class Meta:
        model = Order
        fields = (
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode', 'country', 'county',
        )

    def __init__(self, *args, **kwargs):
        """
        Customize the form on initialization:
        - Add placeholders
        - Add CSS classes for Stripe styling
        - Remove labels
        - Autofocus on the first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        # Set autofocus on the full_name field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # Loop through all fields to apply custom styling and placeholders
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

            # Apply custom class for consistent styling (e.g., with Stripe)
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'

            # Hide labels visually (set to False to render without label text)
            self.fields[field].label = False
