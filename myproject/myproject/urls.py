from django.contrib import admin
from django.urls import path, include
from myapp.views import AttractionAPIView
from myapp.views import AttractionDetailView, AttractionAPIList, AttractionAPIUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/attractionlist/', AttractionAPIView.as_view()),
    # path('api/attractionlist/', AttractionAPIList.as_view()),
    # path('api/attractionlist/<int:pk>/', AttractionAPIUpdate.as_view()),
    # path('api/attractionlist/<int:pk>/', AttractionDetailView.as_view()),
]
