from django.urls import path
from .views import *

app_name = 'info'

urlpatterns = [
    path('', homeview, name='home'),
    path('notice/', noticeview , name='notice'),
    path('contact/', contactview, name='contact'),

]