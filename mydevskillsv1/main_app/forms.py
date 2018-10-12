from django.forms import ModelForm, Form, CharField, PasswordInput, CheckboxSelectMultiple

class LoginForm(Form):
    username = CharField(label="User Name", max_length=50)
    password = CharField(widget=PasswordInput())