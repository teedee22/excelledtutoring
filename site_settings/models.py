from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class TitleSettings(BaseSetting):
    """Site title and subtitle settings"""

    site_title = models.CharField(
        max_length=250, null=True, blank=True, help_text="Site title"
    )
    site_subtitle = models.CharField(
        max_length=250, null=True, blank=True, help_text="Site subtitle"
    )

    panels = [
        MultiFieldPanel(
            [FieldPanel("site_title"), FieldPanel("site_subtitle")],
            heading="Site Title Settings",
        )
    ]


@register_setting
class FooterSettings(BaseSetting):
    """Footer settings for bar at the bottom of the screen"""

    footertext = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        help_text="Copyright logo precedes this"
    )
