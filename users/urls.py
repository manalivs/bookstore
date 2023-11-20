from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name = 'index'),
    path('delete/<str:pk>', views.delete, name = 'delete')
]



# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
