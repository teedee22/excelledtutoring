from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.core.models import Orderable, Page
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet


class BlogAuthorsOrderable(Orderable):
    """This allows us to select one or more blog authors from snippets"""

    page = ParentalKey("blog.BlogPost", related_name="blog_authors")
    author = models.ForeignKey("blog.BlogAuthor", on_delete=models.CASCADE)

    panels = [SnippetChooserPanel("author")]


@register_snippet
class BlogAuthor(models.Model):
    """Blog author for snippets."""

    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="+",
    )
    job_title = models.CharField(max_length=100, blank=True, null=True)
    description = RichTextField(features=[], blank=True, null=True)
    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("job_title"),
                ImageChooserPanel("image"),
                FieldPanel("description"),
            ],
            heading="Name, Image and description",
        ),
        MultiFieldPanel([FieldPanel("website")], heading="Links"),
    ]

    def __str__(self):
        """str repr of this class"""
        return self.name

    class Meta:  # noqa
        verbose_name = "Blog Author"
        verbose_name_plural = "Blog Authors"


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
    blog_listing_large_text = models.CharField(
        max_length=50, blank=True, null=True
    )
    blog_listing_small_text = models.CharField(
        max_length=50, blank=True, null=True
    )
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
            BlogPost.objects.live().public().order_by("-first_published_at")
        )
        # Adding paginator to blog listing page:
        paginator = Paginator(all_posts, 5)
        page = request.GET.get("page")
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context["posts"] = posts
        return context


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
    description_should_appear_at_top_of_blog_post = models.BooleanField(blank=True, null=True)
    blog_post_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete="models.SET_NULL",
    )
    blog_post_content = RichTextField()
    authored_by_large_text = models.CharField(
        max_length=50, blank=True, null=True
    )
    authored_by_small_text = models.CharField(
        max_length=50, blank=True, null=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("blog_post_title"),
        ImageChooserPanel("blog_post_image"),
        FieldPanel("blog_post_description"),
        FieldPanel("description_should_appear_at_top_of_blog_post"),
        FieldPanel("blog_post_content"),
        MultiFieldPanel(
            [
                FieldPanel("authored_by_large_text"),
                FieldPanel("authored_by_small_text"),
                InlinePanel(
                    "blog_authors", label="Author", min_num=0, max_num=10
                )
            ],
            heading="Author(s)",
        ),
    ]
