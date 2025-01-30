from django.contrib import admin
from django.urls import path, include
from myapp.views import AttractionAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/attractionlist/', AttractionAPIView.as_view()),
]
