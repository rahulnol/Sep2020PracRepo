from django.contrib import admin
from django.urls import path
from App2 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexPage.as_view()),
]
