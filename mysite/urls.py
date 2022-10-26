"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
# from rest_framework import routers
# from budget.views import CategoryViewSet, CatExpenseViewSet
from users import views as user_views
from budget import views as budget_views
from django.contrib.auth import views as authentication_views

# router = routers.DefaultRouter()
# router.register('category-rest', CategoryViewSet)
#
# router = routers.SimpleRouter()
# router.register('category-ep', CatExpenseViewSet)
# router.register('EXPENSE', CatExpenseViewSet)

urlpatterns = [
    path('', budget_views.index, name="index"),
    path('admin/', admin.site.urls),
    path('budget/', include('budget.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profilepage, name='profile')
    # path('', include(router.urls))
]
