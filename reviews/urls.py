from django.urls import path
from . import views
urlpatterns = [
    #path("",views.review),## for views using methods
    path("",views.ReviewView.as_view()), ##class based Views
    path("thank-you",views.ThankuView.as_view()),
    # path("thank-you",views.thank_you) ## for views using methods
    path("reviews",views.ReviewsListView.as_view()),
    path("reviews/favourite",views.AddFavouriteView.as_view()),
    # path("reviews/<int:id>",views.SingleReviewView.as_view()),
    path("reviews/<int:pk>",views.SingleReviewView.as_view()) #using DetailView
    #here, it tells django that value entered should be treated as primary key to find single piece of data
]
