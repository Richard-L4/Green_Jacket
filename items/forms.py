
from django import forms
from .widgets import CustomClearableFileInput
from .models import Review, Item, Category


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text']
        widgets = {
            'review_text': forms.Textarea(attrs={'rows': 3}),
        }