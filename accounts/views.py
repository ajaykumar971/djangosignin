from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login


def homePage(request):
	return render(request, 'pages/home.html', {})

def loginPage(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = User.objects.filter(username=username)
		if user.exists():
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('home')
		else:
			# message.error(request, 'invalid password')
			return redirect('login')

	return render(request, 'auth/login.html', {})

def registerPage(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']

		user = User.objects.filter(username=username)
		if user.exists():
			return redirect('register')

		new_user = User.objects.create(
				first_name=first_name,
				last_name=last_name,
				username=username,
				email=email,
			)

		new_user.set_password(password)
		new_user.save()
		return redirect('login')

	return render(request, 'auth/register.html', {})

def logoutPage(request):
	logout(request)
	return redirect('home')