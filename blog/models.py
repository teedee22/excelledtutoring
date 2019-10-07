from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.admin.edit_handlers import (
    FieldPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.

# Blog Author

# Blog Listing


class BlogListingPage(Page):
    """Lists all the blog posts"""
    max_count = 1
    template = "blog/blog_listing_page.html"
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        related_name="+",
        on_delete="models.SET_NULL",
    )
    banner_title = models.CharField(max_length=120, blank=True, null=True)
    intro_text = RichTextField(blank=True, null=True)
    blog_listing_large_text = models.CharField(max_length=50, blank=True, null=True)
    blog_listing_small_text = models.CharField(max_length=50, blank=True, null=True)
    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        ImageChooserPanel("banner_image"),
        FieldPanel("intro_text"),
        FieldPanel("blog_listing_large_text"),
        FieldPanel("blog_listing_small_text"),
    ]

    def get_context(self, request):
        """get all blog posts to list"""
        context = super().get_context(request)
        all_posts = (
            BlogPost.objects.live()
            .public()
            .order_by("-first_published_at")
        )
        # Adding paginator to blog listing page:
        paginator = Paginator(all_posts, 2)
        page = request.GET.get("page")
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context["posts"] = posts
        return context
# Blog Detail page


class BlogPost(Page):
    """Page for Blog Posts"""

    template = "blog/blog_post.html"
    blog_post_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text="Overwrites the default title",
    )
    blog_post_description = RichTextField(features=[], blank=True, null=True)
    blog_post_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete="models.SET_NULL",
    )
    blog_post_content = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("blog_post_title"),
        ImageChooserPanel("blog_post_image"),
        FieldPanel("blog_post_description"),
        FieldPanel("blog_post_content"),
    ]
