from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     user_name=forms.CharField(label="Your Name",max_length=100,error_messages={
#             "required": "Your name must not be empty!",
#             "max_length" : "Please enter shorter name!"
#         })
#     review_text=forms.CharField(label="Your Feedback",widget=forms.Textarea,max_length=200) 
#     #renders the text area instead of text input 
#     #text area-> allows us to enter long text
#     rating=forms.IntegerField(label="Your Rating",min_value=1,max_value=5)

    ##---using MODEL FORM---##
class ReviewForm(forms.ModelForm): 
    #we can directly connect to model and django will automaticaaly take all the django model fields 
    # and infer proper html iputs and basically give us pre-configured form based on the feilds on the propeties of model class
    class Meta():   #to let django know about which model this form is related
        model = Review #here, we are just pointing to Review model but not creating an object
        # fields=['user_name', 'review_text','rating'] #when we want to display only few selective fields
        fields='__all__'                #all fields and properties should be rendered on the form
        # exclude=['owner_comment']         #all fields except one field
        labels={
            'user_name': 'Your name',
             'review_text': 'Your feedback',
             'rating':'Your rating'
        }
        error_messages ={
            'user_name':{
                'required': "Your name must not be empty!",
                "max_length" : "Please enter shorter name!"
            }
        }