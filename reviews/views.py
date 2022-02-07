from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm ######## Forms using Class #########
from .models import Review
# Create your views here.

def review(request):

    ######## When using Forms with Class #########
    if request.method =="POST":
        form=ReviewForm(request.POST) #here, POST is collected data that is part of POST request
        #and the collected data is the data entered in form by user

    # To vaidate the i/p:
                #  data should not be empty
                #if data is valid then it returns True else returns False
                #if data is valid then it populates another field with that valid data

        if form.is_valid(): #if data is valid
            # print(form.cleaned_data) #dictionary will be returned
            review=Review(
                user_name=form.cleaned_data['user_name'],
                review_text=form.cleaned_data['review_text'],
                rating=form.cleaned_data['rating']
                )
            review.save()
            return HttpResponseRedirect('/thank-you')
    
    else: #if data is not valid
        form=ReviewForm() #recreate the form
    return render(request,"reviews/review.html",{ #re-render the template   
                "form": form
            })

        ####### When using Normal forms ######
    # if request.method =="POST": #request.method -> gives access to the method is used for submitting data
    #     entered_username=request.POST['entered_name'] #request.POST -> gives access to the data itself 
    #     # print(entered_username)
    #     if entered_username=="" and len(entered_username)>=100 :
    #         return render(request,"reviews/review.html",{
    #             "has_error":True
    #         })
    #     #POST method will hold a dictionary,where
    #         # keys -> names set on inputs in the form 
    #         #values-> entered values
    #     return HttpResponseRedirect('/thank-you') #name given is urls.py for thank_you()   
    #
    # return render(request,"reviews/review.html",{
    #         "has_error":False
    #     })

def thank_you(request):
    return render(request,"reviews/thankyou.html")
