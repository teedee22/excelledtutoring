from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel
)

from wagtailcaptcha.models import WagtailCaptchaEmailForm
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)
from streams import blocks


class FormField(AbstractFormField):
    page = ParentalKey(
        "ContactPage", on_delete=models.CASCADE, related_name="form_fields"
    )


class ContactPage(WagtailCaptchaEmailForm):
    """Contact Page containing form a Captcha verification"""
    max_count = 1
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    template = "contact/contact_page.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    content = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
        ],
        null=True,
        blank=True,
    )
    contact_small_text = models.CharField(
        max_length=50, blank=True, null=True
    )
    contact_large_text = models.CharField(
        max_length=50, blank=True, null=True
    )
    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        ImageChooserPanel("banner_image"),
        FieldPanel("contact_small_text"),
        FieldPanel("contact_large_text"),
        InlinePanel('form_fields', label="Form Fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6")
            ]),
            FieldPanel('subject'),
        ], heading="Email Settings"),
        StreamFieldPanel("content"),
    ]
