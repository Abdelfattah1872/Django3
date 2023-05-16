from django.urls import path
from . import views
from .views import StudentList
from .views import StudentCreate
from .views import StudentUpdateView
from .views import StudentDeleteView

urlpatterns = [

    path('', views.get_data, name='get_data' ),
    path('create/', views.StudentCreate.as_view()),
    path('<pk>/update', StudentUpdateView.as_view()),
    path('<pk>/delete/', StudentDeleteView.as_view()),
]