from django.urls import path
from .views import HomeView, DetailView, AddView, EditView, DeleteView, contactus, SearchView, BollywoodView, HollywoodView, PunjabiView, SouthView, aboutus


urlpatterns = [
     path('', HomeView.as_view(), name='home'),
     path('detail/<int:pk>122/12/', DetailView.as_view(), name='detail'),
     path('add^post/^admin^_^pan$nel^/^add^post/', AddView.as_view(), name='addpost'),
     path('update/admin^$$pannel/$$edit^post/admin/danish/<int:pk>182/',EditView.as_view(), name='update'),
     path('delete/admin^$$pannel/$$delete^post/admin/danish/<int:pk>/', DeleteView.as_view(), name='delete'),
     path('Contact-us/', contactus, name='contactus'),
     path('results/', SearchView,name='search'),
     path('Bollywood/', BollywoodView.as_view(), name='bollywood'),
     path('Hollywood/', HollywoodView.as_view(), name='hollywood'),
     path('Punjabi/', PunjabiView.as_view(), name='punjabi'),
     path('South^Indian/', SouthView.as_view(), name='South'),
     path('about-us/', aboutus, name='aboutus'),
]
