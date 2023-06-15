from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include

from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add,name='home'),
    # path('details/',views.details,name='details.html'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    # path('cbvhome/',views.TasklistView.as_view(),name='cbvhome'),
    path('cbvdetail/<int:id>/',views.detail,name='cbvdetail'),
    # path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    # path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvDelete'),
]



app_name='todo'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
