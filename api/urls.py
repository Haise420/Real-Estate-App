from django.urls import path
from . import views


urlpatterns = [
    path('properties/', views.getProperties, name='get-properties'),
    path('property/<int:note_id>/', views.getProperty, name='get-property'),
    path('property/create/', views.createProperty, name='create-property'),
    path('property/delete/<int:note_id>/', views.deleteProperty, name='delete-property'),

]

