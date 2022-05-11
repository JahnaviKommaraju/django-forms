from django.db import models

# Create your models here.
class UserProfile(models.Model):
    #  In settings.py,
#        MEDIA_ROOT : It is an absolute path BASE_DIR/"folder_name_for_uploads"
#                     it will tell django where our files shld be stored in general
#                     n then any folders we might point at in our models will be subfolders to MEDIA_ROOT
    ###django accpets all types of files using FileField
    # image= models.FileField(upload_to="images") #django will automatically move uploaded images into "/images" folder inside "/uploads" folder
    # filefield -> takes i/p a file n this file will not be stored in database
    #once we save our model into database, filefield will take that file n move it somewhere onto our hardrive/disk n only stores tha path to that file in the model in database
    
    ###django accpets only images using ImageField
    image= models.ImageField(upload_to="images")

