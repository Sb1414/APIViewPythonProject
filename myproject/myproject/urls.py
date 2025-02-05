from django.contrib import admin
from django.urls import path, include
from myapp.views import AttractionAPIView, AttractionDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/attractionlist/', AttractionAPIView.as_view()),
    path('api/attractionlist/<int:pk>/', AttractionDetailView.as_view())
]
