from dataclasses import fields
from email import message
from re import template
from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect
from matplotlib.style import context

import reviews
from .forms import ReviewForm ######## Forms using Class #########
from .models import Review
from django.views import View  ########## Class based Views#########

from django.views.generic.base import TemplateView ####built-in class view, if we use views for template####

from django.views.generic import ListView,DetailView ####built-in class view, if we have similar template views

from django.views.generic.edit import FormView, CreateView #### to build class based views that deals with forms

# Create your views here.

### Class based views(same as below view methods but using class )
# class ReviewView(View):
#     ##django will automaticaly call these Http methods based on request
#     def get(self,request):
#         form=ReviewForm() #recreate the form
#         return render(request,"reviews/review.html",{ #re-render the template   
#                 "form": form
#             })

#     def post(self,request):
#         form=ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/thank-you')
#         return render(request,"reviews/review.html",{ #re-render the template   
#                 "form": form
#             })


#######FormView: helps to build class based views that deals with forms
# class ReviewView(FormView):

#     #form_class -> to know which form class shld be used to render the form for 
#     # providing the form to template and for validating the i/p data
#     form_class= ReviewForm
#     #template_name-> which template shld be used to render the form
#     template_name="reviews/review.html"

#     #django automatically handles the form submission and form validation

#     #success-url -> to which url it shld redirect after form submission
#     success_url="/thank-you"

#     #but django doesn't know what to do with data, so we use
#             # def form_valid(self, form: _FormT) -> HttpResponse:
#             #     return super().form_valid(form)

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


#######CreateView: specialized form view which automatically creates and save data
                    # to render form 
                    # validate form
                    # show errors if needed
                    # save data 
class ReviewView(CreateView):
    model=Review
    form_class=ReviewForm
    template_name="reviews/review.html"
    success_url="/thank-you"



### Views using methods
# def review(request):

#     ######## When using Forms with Class #########
#     if request.method =="POST":
#         form=ReviewForm(request.POST) #populating form with submitted data
#     #      #here, POST is collected data that is part of POST request
#     #     #and the collected data is the data entered in form by user

#         ####in method-2 --> save() for already existing_data
#         ##existing_data= Review.objects.get(pk=1)
#         ##form=ReviewForm(request.POST, instance=existing_data)
#     # # To vaidate the i/p:
#     #             #  data should not be empty
#     #             #if data is valid then it returns True else returns False
#     #             #if data is valid then it populates another field with that valid data

#         if form.is_valid(): #if data is valid
#             ######### method-1 : 
#                     ##--> populating form with submitted data
#                     ##--> validating data
#                     ##--> if valid creating a model instance
#                     ##--> saving the form

#     #         # print(form.cleaned_data) #dictionary will be returned
#     #         review=Review(
#     #             user_name=form.cleaned_data['user_name'],
#     #             review_text=form.cleaned_data['review_text'],
#     #             rating=form.cleaned_data['rating']
#     #             )  #model instance
#     #         review.save()

#             #########(PREFER)method-2 : using model form
#             form.save() #saves data in database through that connected model(here, it is REVIEW Model)
#             #here, save() -> it is also used to update the exsiting data in form
#         return HttpResponseRedirect('/thank-you')


    
#     else: #if data is not valid
#         form=ReviewForm() #recreate the form
#     return render(request,"reviews/review.html",{ #re-render the template   
#                 "form": form
#             })

#         ####### When using Normal forms ######
#     # if request.method =="POST": #request.method -> gives access to the method is used for submitting data
#     #     entered_username=request.POST['entered_name'] #request.POST -> gives access to the data itself 
#     #     # print(entered_username)
#     #     if entered_username=="" and len(entered_username)>=100 :
#     #         return render(request,"reviews/review.html",{
#     #             "has_error":True
#     #         })
#     #     #POST method will hold a dictionary,where
#     #         # keys -> names set on inputs in the form 
#     #         #values-> entered values
#     #     return HttpResponseRedirect('/thank-you') #name given is urls.py for thank_you()   
#     #
#     # return render(request,"reviews/review.html",{
#     #         "has_error":False
#     #     })



### method based view
# def thank_you(request):
#     return render(request,"reviews/thankyou.html")

### Class based view
# class ThankuView(View):
#     def get(self,request):
#         return render(request,"reviews/thankyou.html")

### Using inbuilt Templateview
    ####  --> so that we need not use get() to get templates while using class based views 
class ThankuView(TemplateView):
    template_name ="reviews/thankyou.html"
    ########to send dynamic data into template and interpolate it
    # 
    # pre-defined method returns dict -> Dict[str, Any]
    def get_context_data(self, **kwargs):
        mydata= super().get_context_data(**kwargs)
        mydata["message"] ="This works"
        return mydata

#####To get data in form of lists using Template View
# class ReviewsListView(TemplateView):
#     template_name ="reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         mydata=super().get_context_data(**kwargs)
#         reviews=Review.objects.all()
#         mydata["reviews"]=reviews
#         return mydata

#####using ListView instead of template view for above class ReviewsListView
        # ---> ListView - specialized template view
        #               - renders the template for a get request
        #               - for fetching list of data based on some model i.e. same as above

class ReviewsListView(ListView):
    template_name ="reviews/review_list.html"
    model= Review #just poinitng to Review class in model
    context_object_name="reviews" #to change object_list name

    #####to apply conditions on our output
    # def get_queryset(self):
    #     my_query=super().get_queryset()
    #     data=my_query.filter(rating__gt=4)
    #     return data


# class SingleReviewView(TemplateView):
#     template_name="reviews/single_review.html"

#     def get_context_data(self, **kwargs):
#         mydata=super().get_context_data(**kwargs)
#         review_id=kwargs["id"]
#         selected_review=Review.objects.get(pk=review_id)
#         mydata["review"]= selected_review
#         return mydata

#####using DetailView instead of template view for above class SingleReviewView
        # --->DetailView - when we only just want to fetch some single peice of data based on some model
class SingleReviewView(DetailView):
    template_name="reviews/single_review.html"
    model= Review #automatically fetches Review 
    ##########here, django uses slug/ primary key to identify a single item########

    ##storing session data
    def get_context_data(self, **kwargs):
        mydata=super().get_context_data(**kwargs)
        loaded_review=self.object #will give acess to automatically loaded Review
        request=self.request
        # favourite_id=request.session["favourite_review"] #directly accessing key #it will throw error if session doesn't exist
        favourite_id=request.session.get("favourite_review") ##this is safer way to access session data instead of above i.e it will not throw error if session doesn't exist
        mydata["is_favourite"]=favourite_id==str(loaded_review.id)
        return mydata



####creating view for favourite reviews

class AddFavouriteView(View):
    def post(self,request):
        review_id=request.POST['review_id']
        fav_review=Review.objects.get(pk=review_id)

        #storing fav_review in session
        # request.session["favourite_review"] =fav_review#to acess already stored data / to add new data into session

        request.session["favourite_review"] =review_id #as we can't store objects in session we store review id in session
        return HttpResponseRedirect("/reviews/"+review_id)

