from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile information.

    Excludes the 'user' field because it's managed separately.
    Adds placeholders and CSS classes to fields,
    removes labels, and sets autofocus on the phone number field.
    """

    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Customize form fields after initialization.

        - Add placeholders for better UX.
        - Mark required fields with an asterisk (*).
        - Set autofocus on phone number field.
        - Add consistent CSS classes to all input widgets.
        - Remove auto-generated labels for cleaner look.
        """
        super().__init__(*args, **kwargs)

        # Dictionary mapping fields to their placeholder texts
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        # Set autofocus on the phone number input
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        for field_name, field in self.fields.items():
            # Skip placeholder for default_country field
            if field_name != 'default_country':
                # Add '*' to placeholder if field is required
                if field.required:
                    placeholder = f"{placeholders[field_name]} *"
                else:
                    placeholder = placeholders[field_name]
                field.widget.attrs['placeholder'] = placeholder

            # Add CSS classes for styling all fields uniformly
            field.widget.attrs['class'] = \
                'border-black rounded-0 profile-form-input'

            # Remove field labels since placeholders are used
            field.label = False
