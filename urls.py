"""projecr12345 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
{% elif form.instance.pk and student.student_status == 'enquiry' %}

        <h1><em>Student Enquiary and Payment Form</em></h1><br><br>
              <form method="POST">
             {{ form.as_p }}
             {% csrf_token %}
    <input class="btn btn-outline-primary" type="submit" value="SUBMIT">
</form>
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from app12345 import views
app_name='app12345'

urlpatterns = [
    path('create/', views.Create.as_view(),name='create'),
    path('', views.list,name='list'),
    path('register/', views.register,name='register'),
    path('login/', views.login1,name='login'),
    path('logout/', views.logout1,name='logout'),
    url(r'^(?P<pk>\d+)/$',views.Detail.as_view(),name='detail'),
    url(r'^update/(?P<pk>\d+)/$',views.Update.as_view(),name='update'),

    url(r'^delete/(?P<pk>\d+)/$',views.Delete.as_view(),name='delete')

]
