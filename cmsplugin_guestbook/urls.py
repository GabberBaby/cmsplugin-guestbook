# -*- coding: UTF-8 -*-

from django.conf.urls.defaults import *
from django.views.generic import ListView, CreateView
import forms
import models

urlpatterns = patterns('',
    url(r'^$', 
        ListView.as_view(
            queryset=models.Guestbook.published.all(),
            paginate_by=5
            ), 
        name='list_guestbook'),
    url(r'^new/$', 
        CreateView.as_view(
            form_class=forms.GuestbookForm,
            model=models.Guestbook,
        ),
        name='new_guestbook'),

)