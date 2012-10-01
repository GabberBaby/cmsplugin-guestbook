from classytags.arguments import Argument, StringArgument
from classytags.core import Options
from classytags.helpers import InclusionTag
from django import template

from ..forms import GuestbookForm

register = template.Library()

class Guestbook(InclusionTag):
    name = 'guestbook_form'
    template = 'cmsplugin_guestbook/guestbook_form.html'

    def get_context(self, context):
        return context.update({
            'csrf_token': context['csrf_token'],
            'form': GuestbookForm()
            })

register.tag(Guestbook)