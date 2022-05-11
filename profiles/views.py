from dataclasses import field
import profile
from sre_constants import SUCCESS
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ProfileForm

from .models import UserProfile

from django.views.generic.edit import CreateView #### to build class based views that deals with forms

from django.views.generic import ListView
# Create your views here.


# def store_file(file):
#     with open("temp/image.png","wb+") as dest: #wb+ --> write binary file data
#         for chunk in file.chunks():
#             dest.write(chunk)

# class CreateProfileView(View):
#     def get(self,request):
#         form = ProfileForm()
#         return render(request,"profiles/create_profile.html",{
#             "form":form
#         })

#     def post(self,request):
#         submitted_form=ProfileForm(request.POST,request.FILES) #form to pass-in the submitted data n files
#         #request.POST ##gives acess to all data(non-file types)
#         if submitted_form.is_valid():
#             ####using def store_file(file):
#             # store_file(request.FILES["image"])#gives access to uploaded file of any type
#             #above, in FILES["image"] , image is the name given to input tag

#             ######using models and forms:
#             profile=UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles")
#         # else:
#         return render(request,"profiles/create_profile.html",{
#             "form":submitted_form
#         })

##instead of above, we can use Create View
class CreateProfileView(CreateView):
    template_name="profiles/create_profile.html"
    model=UserProfile
    fields="__all__"
    success_url="/profiles"

class ProfilesView(ListView):
    model=UserProfile
    template_name="profiles/user_profiles.html"
    context_object_name="profiles"