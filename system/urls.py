from django.urls import path
from . import views

urlpatterns = [
    # both users view mode
    path('view/<int:user_id>/', views.viewEnrolled, name='viewEnrolled'),                                         # view course list
    path('view/<int:user_id>/<int:course_id>/', views.viewCourse, name='viewCourse'),                           # view module list
    path('view/<int:user_id>/<int:course_id>/<int:module_id>/', views.viewModule, name='viewModule'),        # view component list
    path('view/<int:user_id>/<int:course_id>/<int:module_id>/quiz/', views.takeQuiz, name='takeQuiz'),          # learner takes quiz
    path('view/<int:user_id>/<int:course_id>/<int:module_id>/quiz/submitAnswer/', views.submitAnswer, name='submitAnswer'),        # learner submits answer

    # instructor editing mode
    path('view/<int:instructor_id>/<int:course_id>/add/',views.manageModule, name='manageModule'),                                            # edit module list
    path('view/<int:instructor_id>/<int:course_id>/<int:module_id>/addComponent/',views.selectComponent, name='selectComponent'),             # edit component list
    path('view/<int:instructor_id>/<int:course_id>/<int:module_id>/addComponent/<int:component_id>',views.addComponent, name='addComponent'), # edit module 
    path('view/<int:instructor_id>/<int:course_id>/<int:module_id>/selectQuiz/', views.selectQuiz, name='selectQuiz'),                        # edit module quiz
    path('view/<int:instructor_id>/<int:course_id>/<int:module_id>/addQuiz/<int:quiz_id>', views.addQuiz, name='addQuiz'),                    # edit quiz
    path('view/<int:instructor_id>/<int:course_id>/<int:module_id>/modiModuleOrd/',views.modiModuleOrd,name='modiModuleOrd'),
    path('view/<int:instructor_id>/<int:course_id>/<int:module_id>/modiModuleOrd/moduleOrder/',views.moduleOrder,name='moduleOrder'),
]
