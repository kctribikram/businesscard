from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Q
from app.models import UserLogin
from app.models import User

# /*------------Authentication to for Admin------------------*/
class Authenticate:
	def valid_user(function):
		def wrap(request):
			try:
				# User.objects.get(email=request.session['email'])
				UserLogin.objects.get(Q(password=request.session['password']) & Q(username=request.session['username']))
				return function (request)
			except:
				messages.warning(request,"Invalid email or password")
				return redirect('/login')
		return wrap


class AuthenticateA:
	def valid_admin(function):
		def wrap(request):
			try:
				# User.objects.get(email=request.session['email'])
				User.objects.get(Q(password=request.session['password']) & Q(email=request.session['email']))
				return function (request)
			except:
				messages.warning(request,"Invalid email or password")
				return redirect('/admin')
		return wrap