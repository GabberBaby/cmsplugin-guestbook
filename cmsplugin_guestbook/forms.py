from django.forms import ModelForm
import models

class GuestbookForm(ModelForm):
    class Meta:
        model = models.Guestbook
        fields = ['message', 'name', 'email', 'webpage']