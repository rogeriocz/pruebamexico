from django.shortcuts import render
from django.contrib.auth import login

from .forms import UserCreationEmailForm, EmailAuthenticationForm

# Create your views here.
def signup(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		form.save()


	return render(request, 'userprofiles/signup.html', {'form': form})


def signin(request):
	forms = EmailAuthenticationForm(request.POST or None)
	print "valido"
	if form.is_valid():
		login(request, form.get_user())

	return render(request, 'userprofiles/signin.html', {'form': form})