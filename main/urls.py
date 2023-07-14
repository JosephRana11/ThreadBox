from django.urls import path
from .views import home_view , signup_view ,create_post_view

urlpatterns = [
    path('' , home_view , name='home'),
    path('home' , home_view , name='home'),
    path('sign-up' , signup_view, name='signup'),
    path('create-post' , create_post_view , name = 'createpost')
]

