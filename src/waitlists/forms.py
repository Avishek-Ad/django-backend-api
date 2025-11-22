from django import forms
from .models import WaitListEntry
from django.utils import timezone


class WaitListEntryCreateForm(forms.ModelForm):
    class Meta:
        model = WaitListEntry
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        today = timezone.now().date()
        qs = WaitListEntry.objects.filter(email=email, timestamp__date=today)
        if qs.count() >= 5:
            raise forms.ValidationError('Cannot enter this email again today.')
        # if email.endswith("@gmail.com"):
        #     raise forms.ValidationError('Cannot use gmail')
        return email