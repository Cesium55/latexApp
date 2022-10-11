from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('conspects/', views.defaulConspect, name="conspects"),
    path('conspects/<int:id>/', views.conspectById, name="conspects"),
    path('dynamic', views.dynamicFormula, name="dynamic"),
]