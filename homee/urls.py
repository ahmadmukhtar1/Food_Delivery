from django.urls import path
from . import views
urlpatterns = [
	path('home/', views.Home, name = "home"),
	path('form/', views.create, name = "form"),
	path('menu/', views.Menu, name = "menu"),
	path('contact/', views.Contact, name = "contact"),
	path('faq/', views.Faq, name = "faq"),
	path('list/', views.List, name = "list"),
	path('update/<int:id>/', views.Update, name = "update"),
]