"""Streamfields find their home in this file"""

from wagtail.core import blocks


class RichTextBlock(blocks.RichTextBlock):
    """Richtext with all the features"""

    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"
