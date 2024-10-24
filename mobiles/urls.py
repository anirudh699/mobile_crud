"""
URL configuration for mobiles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mob import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mobiles/add',views.MobileView.as_view(),name="mobile-add"),
    path('mobiles/list',views.MobilesList.as_view(),name="mobile-list"),
    path('mobiles/<int:pk>/detail',views.MobileDetail.as_view(),name="mobile-detail"),
    path('mobiles/<int:pk>/remove',views.MobileDeleteview.as_view(),name="mobile-delete"),
]
