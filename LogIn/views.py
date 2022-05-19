from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .forms import SignUpForm, ProfileForm, SignInForm, MyPasswordResetForm, MySetPasswordForm


# View for new user
def SignUp(request):
    user_form = SignUpForm()
    profile_form = ProfileForm()
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            # Assign instance of User to Profile model
            profile.user = user
            profile.save()

            return redirect(reverse('login'))
        else:
            return render(request, 'LogIn/signup.html', {'user_form': user_form, 'profile_form': profile_form })
    else:
        return render(request, 'LogIn/signup.html', {'user_form': user_form, 'profile_form': profile_form})



def LogInView(request):
    if request.method == 'POST':
        log_in_form = SignInForm(request, request.POST)
        if log_in_form.is_valid():
           return redirect(reverse('search'))
    else:
        log_in_form = SignInForm()
    return render(request, 'LogIn/signin.html', {'log_in_form': log_in_form})



class MyPasswordResetView(PasswordResetView):
    form_class = MyPasswordResetForm


class MyPasswordResetDoneView(PasswordResetDoneView):
    pass

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = MySetPasswordForm

class MyPasswordResetCompleteView(PasswordResetCompleteView):
    pass
