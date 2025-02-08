from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# from myapp.views import AttractionAPIView
from myapp.views import AttractionDetailView, AttractionAPIList, AttractionAPIUpdate, AttractionAPIViewSet

router = routers.SimpleRouter() # DefaultRouter - добавляет api-root
router.register(r'attractions', AttractionAPIViewSet)
print(router.urls) # [<URLPattern '^attractions/$' [name='attraction-list']>, <URLPattern '^attractions/(?P<pk>[^/.]+)/$' [name='attraction-detail']>]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # path('api/attractionlist/', AttractionAPIView.as_view()),

    # path('api/attractions/', AttractionAPIList.as_view()),
    # path('api/attractionlist/<int:pk>/', AttractionAPIUpdate.as_view()),
    # path('api/attractionlist/<int:pk>/', AttractionDetailView.as_view(), name='attraction_detail'),
    # path('api/attractions/<int:pk>/', AttractionDetailView.as_view(), name='attraction_detail'),

    # path('api/v1/womenlist/', AttractionAPIViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('api/v1/womenlist/<int:pk>/', AttractionAPIViewSet.as_view({'get': 'retrieve'})),
]
