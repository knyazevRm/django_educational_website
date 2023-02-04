from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', Base.as_view(), name='base'),

    path('company/', Company.as_view(), name='company'),
    path('position/', Position.as_view(), name='position'),
    path('resume/', Resume.as_view(), name='resume'),

    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
]