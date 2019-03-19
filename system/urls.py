from django.urls import path
from system import views

urlpatterns = [
    path('manage/module/',views.ManageModule.as_view(),name='manageModule'),
    path('manage/component/<int:module>/',views.showComponent.as_view(),name='showComponent')
]