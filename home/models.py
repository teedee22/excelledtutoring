from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
)

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePageTestimonial(Orderable):
    """Orderable for testimonials appearing on the homepage"""
    page = ParentalKey("home.HomePage", related_name="testimonials")
    testimonial_text = models.CharField(max_length=700, blank=True, null=True)
    testimonial_author = models.CharField(
        max_length=200, blank=True, null=True
    )
    testimonial_location = models.CharField(
        max_length=100, blank=True, null=True
    )

    panels = [
        FieldPanel("testimonial_text"),
        FieldPanel("testimonial_author"),
        FieldPanel("testimonial_location"),
    ]


class HomePageMethodology(Orderable):
    """Orderable for the three part methodology on the homepage"""
    page = ParentalKey("home.HomePage", related_name="methodology")
    method_title = models.CharField(max_length=100, blank=True, null=True)
    method_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    method_text = models.CharField(max_length=700, blank=True, null=True)

    panels = [
        FieldPanel("method_title"),
        ImageChooserPanel("method_image"),
        FieldPanel("method_text"),
    ]


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
    page_subtitle = models.CharField(max_length=150, null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [ImageChooserPanel("banner_image")], heading="Banner Options"
        ),
        MultiFieldPanel(
            [
                InlinePanel(
                    "testimonials", max_num=3, min_num=3, label="Testimonials"
                )
            ],
            heading="Testimonials",
            ),
        MultiFieldPanel(
            [
                FieldPanel("page_subtitle"),
                InlinePanel(
                    "methodology", max_num=3, min_num=3, label="Our methods"
                )
            ],
            heading="Methodology",
        ),
    ]
