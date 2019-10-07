from django import forms
from wagtailstreamforms.fields import BaseField, register


@register('multiline')
class MultiLineTextField(BaseField):
    field_class = forms.CharField
    widget = forms.widgets.Textarea(attrs={'rows': 4})
