from django.shortcuts import render

# Create your views here.
def index(req):
  return render(req, 'login_registration_apps/index.html')
