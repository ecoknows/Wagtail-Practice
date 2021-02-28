from wagtail.core import blocks

class TittleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else"""
    title = blocks.CharBlock(required=True,help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text="Add Additional Text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text"

class RichTextBlock(blocks.RichTextBlock):
    """RichText with all the featuers"""
    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"

class SimpleRichTextBlock(blocks.RichTextBlock):
    """RichText without (limited) all the featuers"""
    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"
        