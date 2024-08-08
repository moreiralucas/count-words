from django import forms
from core.models import Counter


class TextForm(forms.Form):
    text = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter your text here"}),
        required=False,
    )

    def clean_text(self):
        text = self.cleaned_data.get("text", "")
        if len(text) == 0:
            raise forms.ValidationError("This field cannot be empty.")
        return text
