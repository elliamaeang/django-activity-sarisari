from django.urls import path
from . import views
from sarisaristoreapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name="index"),
    path("upload/", views.upload, name="upload"),
    path("update/<int:product_id>", views.update),
    path("delete/<int:product_id>", views.delete)
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)