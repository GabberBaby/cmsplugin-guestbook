"""Applications hooks for cmsplugin_zinnia"""
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class GuestbookApphook(CMSApp):
    name = _('Guestbook')
    urls = ['cmsplugin_guestbook.urls']

apphook_pool.register(GuestbookApphook)
