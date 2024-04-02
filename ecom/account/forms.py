from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

# Registration Form
class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

  def __init__(self, *args, **kwargs):
    super(CreateUserForm, self).__init__(*args, **kwargs)
    # email field required
    self.fields["email"].required = True

  # Validation for email
  def clean_email(self):
    email = self.cleaned_data.get("email")

    if User.objects.filter(email=email).exists():
      raise forms.ValidationError("Email already exists")
    
    if len(email) >= 350:
      raise forms.ValidationError("Email is too long")
    return email
  
class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=TextInput())
  password = forms.CharField(widget=PasswordInput())

# Update form
  
class UpdateUserForm(forms.ModelForm):
  password = None
  class Meta:
    model = User
    fields = ['username', 'email']
    exclude = ['password1', 'password2']
  def __init__(self, *args, **kwargs):
    super(UpdateUserForm, self).__init__(*args, **kwargs)
    # email field required
    self.fields["email"].required = True

  # Validation for email
  def clean_email(self):
    email = self.cleaned_data.get("email")

    # if you're updating your username but keeping the email the same, 
    # the update won't raise an error if the email already exists for 
    # this account, but does raise an error if the email exists for
    # another account
    if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
      raise forms.ValidationError("Email already exists")
    
    if len(email) >= 350:
      raise forms.ValidationError("Email is too long")
    return email
