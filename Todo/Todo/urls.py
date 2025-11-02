
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup),
    path('loginn/',views.loginn),
    path('todopage/',views.todo),
    path('signout/', views.signout, name='signout'),

]
