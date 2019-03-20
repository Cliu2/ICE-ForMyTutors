from django.urls import path
from . import views

urlpatterns = [
    path('manage/module/',views.ManageModule.as_view(),name='manageModule'),
    path('manage/component/<int:module>/',views.showComponent.as_view(),name='showComponent'),
    path('manage/quiz/<int: module>/', views.showQuiz.as_view(), name='showQuiz'),
    
    path('study/<int:learner_id>', views.showCourses, name='showCourses'),
    path('study/<int:learner_id>/<int:course_id>/', views.viewCourse, name='viewCourse'),
    path('study/<int:learner_id>/<int:course_id>/<int:module>', views.studyModule, name='studyModule'),
    path('study/<int:learner_id>/<int:course_id>/<int:quiz>', views.takeQuiz, name='takeQuiz'),
]
