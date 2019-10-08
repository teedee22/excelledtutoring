from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    MultiFieldPanel,
    InlinePanel,
    PageChooserPanel,
)
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailcaptcha.models import WagtailCaptchaEmailForm


class FormField(AbstractFormField):
    page = ParentalKey(
        "HomePage", on_delete=models.CASCADE, related_name="form_fields"
    )


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


class HomePageFeaturedBlogPost(Orderable):
    """Orderable featured blog post or posts"""
    page = ParentalKey("home.HomePage", related_name="featured")
    featured_blog_post = models.ForeignKey(
        "wagtailcore.page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    panels = [
        PageChooserPanel("featured_blog_post")
    ]


class HomePage(WagtailCaptchaEmailForm):
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
    thank_you_text = RichTextField(blank=True)
    blog_featured_large_text = models.CharField(
        max_length=50, blank=True, null=True
    )
    blog_featured_small_text = models.CharField(
        max_length=50, blank=True, null=True
        )
    content_panels = AbstractEmailForm.content_panels + [
        MultiFieldPanel(
            [ImageChooserPanel("banner_image")], heading="Banner Options"
        ),
        InlinePanel('form_fields', label="Form Fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6")
            ]),
            FieldPanel('subject'),
        ], heading="Email Settings"),
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
        MultiFieldPanel(
            [
                FieldPanel("blog_featured_large_text"),
                FieldPanel("blog_featured_small_text"),
                InlinePanel(
                    "featured", max_num=6, min_num=0, label="featured blog post(s)"
                )
            ]
        )
    ]
