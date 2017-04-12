from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page

from wagtailmarkdown.fields import MarkdownField, MarkdownPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class HomePage(Page):
    body = MarkdownField(blank=True)

    content_panels = [
        FieldPanel("title", classname="full title"),
        MarkdownPanel("body"),
    ]
