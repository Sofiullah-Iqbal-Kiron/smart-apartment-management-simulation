from django import forms
from .models import Guest


class GuardAdminForm(forms.Form):
    mens = forms.ChoiceField(choices=['a', 'a', 'd'])

# class CreateGuestForm(forms.ModelForm):
#     # form fields:
#     # guest_id: prefilled, not editable
#     # used_token: prefilled, token just used
#     # guest_of: prefilled, not editable, who seeked/fond this token
#     # nid_or_br: fill by guard
#     # photo: ImageField
#     # CreateGuest: button, when clicked:
#     # create a guest -> inc_nou -> return success and form for next page if no error raises and can_inc_now
#     class Meta:
#         model = Guest
#         exclude = ['']
