# from django.contrib import admin
from django.urls import path
from testapp import views

app_name='testapp'
urlpatterns = [
    # path('api/',views.EmployeeListAPIView.as_view()),
    # path('api/',views.EmployeeCreateAPIView.as_view()),
    # path('api/<id>',views.EmployeeRetriveAPIView.as_view()),
    # path('api/<pk>',views.EmployeeUpdateAPIView.as_view()),
    # path('api/<id>',views.EmployeeDestroyAPIView.as_view()),
    #*******************************************************
    path('api/',views.EmployeeListCreateAPIView.as_view()),
    # path('api/<id>', views.EmployeeRetriveUpdateAPIView.as_view()),
    # path('api/<id>', views.EmployeeRetriveDestroyAPIView.as_view()),
    path('api/<id>', views.EmployeeRetriveUpdateDestroyAPIView.as_view()),

]