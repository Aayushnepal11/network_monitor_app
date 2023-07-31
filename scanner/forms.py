from django import forms


class MyGenericIpAddressField(forms.GenericIPAddressField):
    def __init__(self,*args, **kwargs):
        kwargs.setdefault('widget', forms.TextInput(attrs={'class': 'form-control'}))
        super().__init__(*args, **kwargs)

class SearchForm(forms.Form):
    ip_address = MyGenericIpAddressField(max_length=32, required=True)

