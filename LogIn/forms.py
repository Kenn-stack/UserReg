from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm

# Form for collecting user authentication data
class SignUpForm(UserCreationForm):
    field_order= ('username','email','password1', 'checkbox1', 'password2')
    checkbox1 = forms.BooleanField(required = False, label = '', widget = forms.CheckboxInput(attrs={'class': 'form-check-input', 'onclick': 'checkBox("id_password1")'}))
    checkbox2 = forms.BooleanField(required = False, label = '', widget = forms.CheckboxInput(attrs={'class': 'form-check-input', 'onclick': 'checkBox("id_password2")'}))

    class Meta(UserCreationForm.Meta):
        fields = ("username","email")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'password1':
                self.fields[field].widget = forms.PasswordInput(attrs={'placeholder':'enter password', 'class': 'form-control my-2'})
                self.fields[field].label = '' 

            elif field == 'password2':
                self.fields[field].widget = forms.PasswordInput(attrs = {'placeholder':'re-enter password', 'class': 'form-control my-4'})
                self.fields[field].label = '' 

        
            elif field == 'username':
                self.fields[field].help_text = "<li> Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</li>"
                self.fields[field].widget = forms.TextInput(attrs = {'placeholder':field, 'class': 'form-control my-4', 'autocomplete':'off'})
                self.fields[field].label = ''
            
            elif field == 'email':
                self.fields[field].widget = forms.EmailInput(attrs = {'placeholder':field, 'class': 'form-control my-4', 'autocomplete':'off'})
                self.fields[field].label = ''



# Form for collecting user details
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'middlename', 'phone', 'date_of_birth']
        widgets ={
            'firstname' : forms.TextInput(attrs = {'placeholder': 'Firstname', 'class': 'form-control mb-4', 'autocomplete':'off'}),
            'lastname' : forms.TextInput(attrs = {'placeholder': 'Lastname', 'class': 'form-control mb-4', 'autocomplete':'off'}),
            'lastname' : forms.TextInput(attrs = {'placeholder': 'Lastname', 'class': 'form-control mb-4', 'autocomplete':'off'}),
            'middlename' : forms.TextInput(attrs = {'placeholder': 'Middlename', 'class': 'form-control mb-4', 'autocomplete':'off'}),
            'phone' : forms.TextInput(attrs = {'placeholder': 'Phone', 'class': 'form-control mb-4', 'autocomplete':'off'}),
            'date_of_birth' : forms.DateInput(attrs = {'placeholder': 'Date of Birth','class': 'form-control mb-4', 'autocomplete':'off', 'type': 'date'}),
        }
        labels = {}
        for field in fields:
            labels[field]= ''
                    

# Signin form
class SignInForm(AuthenticationForm):
    checkbox = forms.BooleanField(required = False, label = '', widget = forms.CheckboxInput(attrs={'class': 'form-check-input', 'onclick': 'checkBox("id_password")'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'username':
                self.fields[field].widget = forms.TextInput(attrs = {'placeholder': 'username or email', 'class': 'form-control', 'autocomplete':'off'})
                self.fields[field].label = ''

            elif field == 'password': 
                self.fields[field].widget = forms.PasswordInput(attrs = {'placeholder': field, 'class': 'form-control', 'autocomplete':'off'})
                self.fields[field].label = ''

# Custom form for password reset. Inherits from PasswordResetForm
class MyPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget = forms.EmailInput(attrs={'placeholder': field, 'class': 'form-control', 'autocomplete':'off'})
            self.fields[field].label = ''


# Custom form for setting new password. Inherits from SetPasswordForm
class MySetPasswordForm(SetPasswordForm):
    checkbox = forms.BooleanField(required = False, label = '', widget = forms.CheckboxInput(attrs={'class': 'form-check-input', 'onclick': 'checkBox("id_password")'}))
    def __init__(self, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'password':
                self.fields[field].widget = forms.PasswordInput(attrs={'placeholder': field, 'class': 'form-control'})
                self.fields[field].label = ''

