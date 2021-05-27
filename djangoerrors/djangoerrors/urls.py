"""djangoerrors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from djangoerrors.errors.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-thing/', AddThing.as_view(), name="add-thing"),
    path('add-thing-error/', AddThingError.as_view()),
    path('add-thing-with-file/', AddThingWithFile.as_view()),
    path('add-thing-with-save-method/', AddThingWithSaveMethod.as_view()),
    path('add-thing-error-atomic/', AddThingErrorAtomic.as_view()),
    path('add-thing-error-atomic-with-save-method/', AddThingErrorAtomicWithSaveMethod.as_view()),
    path('add-thing-with-file/', AddThingErrorAtomicWithFile.as_view()),
    path('add-thing-error-atomic-with-file/', AddThingErrorAtomicWithFile.as_view()),
    path('loop/', Loop.as_view()),
    path('', ViewsList.as_view()),

]
