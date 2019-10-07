from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel

from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    """Home page model/ landing page"""
    template = "home/home_page.html"
    max_count = 1
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                ImageChooserPanel("banner_image"),
            ],
            heading="Banner Options",)
        ]
