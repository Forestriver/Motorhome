from django import forms

class ContactForm(forms.Form):
    sender_name = forms.EmailField(required = False, label = 'Ваша e-mail адреса')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=form.Textarea, label = 'Повідомлення')
