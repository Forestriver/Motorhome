from django import forms

class ContactForm(forms.Form):
    sender = forms.CharField(label="Ім'я відправника",
                             max_length=100,
                             required = True,
                             widget=forms.TextInput(attrs={'class':'form-control'}))         
    email = forms.EmailField(label = "Ваша e-mail адреса",
                             max_length=100,
                             required=True,
                             widget=forms.EmailInput(attrs={'class':'form-control'}))
    message = forms.CharField(widget=form.Textarea, label = 'Повідомлення')
