from django.urls import path
from . import views

#paths for account app.
urlpatterns = [
    path('',views.BookView, name='Book_url'),
    path('requestBook/',views.RequestBookView, name="RequestBook_url"),
]