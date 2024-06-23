from django.urls import path
from . import views
urlpatterns = [
    path('', views.test,name="test"),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('<int:id>/',views.update,name='update')
    
]
