from django import forms
from .widgets import CustomClearableFileInput
from .models import Review, Item, Category


class ItemForm(forms.ModelForm):
    """
    Form for creating and updating Item instances in the admin panel.
    Includes a custom image input widget and custom styling for all fields.
    """

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )

    class Meta:
        model = Item
        fields = '__all__'  # Include all fields from the Item model

    def __init__(self, *args, **kwargs):
        """
        Customize the form:
        - Replace category IDs with friendly names.
        - Add consistent styling to all fields.
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names

        # Add custom CSS classes to each form field
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """
    Form for submitting a review. Only includes the review_text field.
    """

    class Meta:
        model = Review
        fields = ['review_text']
        widgets = {
            # Use a small textarea for reviews (3 rows)
            'review_text': forms.Textarea(attrs={'rows': 3}),
        }