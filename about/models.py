from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    StreamFieldPanel,
    FieldPanel,
    InlinePanel,
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable

from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.

from streams import blocks


class OurTeam(Orderable):
    """Orderable for team members"""

    page = ParentalKey("about.AboutPage", related_name="team")
    name = models.CharField(max_length=200, blank=False, null=True)
    position = models.CharField(max_length=200, blank=True, null=False)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    description = RichTextField(features=[], blank=True, null=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("position"),
        ImageChooserPanel("image"),
        FieldPanel("description"),
    ]


class AboutPage(Page):
    """About page"""

    max_count = 1
    template = "about/about.html"
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    banner_title = models.CharField(max_length=120, blank=True, null=True)

    content = StreamField(
        [("full_richtext", blocks.RichTextBlock())], null=True, blank=True
    )
    team_intro_large_text = models.CharField(
        max_length=50, blank=True, null=True
    )
    team_intro_small_text = models.CharField(
        max_length=50, blank=True, null=True
    )
    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        ImageChooserPanel("banner_image"),
        StreamFieldPanel("content"),
        MultiFieldPanel(
            [
                FieldPanel("team_intro_small_text"),
                FieldPanel("team_intro_large_text"),
                InlinePanel("team")
            ],
            heading="Add team members"),
    ]
