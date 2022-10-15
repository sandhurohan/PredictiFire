from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("tool/", views.tool, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
]
