"""
URL configuration for quotes_site project.

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

from django.urls import path

from . import views

app_name = "quotes"


urlpatterns = [
    path("", views.main, name='root'),
    path("<int:page>/", views.main, name='root_paginate'),
    path('author/<uuid:id>', views.profile, name='author'),
    path('quotes/add_author/', views.add_author, name='add_author'),
    path('quotes/add_quote/', views.add_quote, name='add_quote'),
]
