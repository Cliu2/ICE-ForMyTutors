from django.urls import path
from . import views

urlpatterns = [
    # both users
    path('view/<int:user_id>/', views.showCourses, name='showCourses'),                                               # view course list
    path('view/<int:user_id>/<int:course_id>/', views.showModules, name='showModules'),                               # view module list
    #path('view/<int:user_id>/<int:course_id>/<int:module_id>/', views.showComponents, name='showComponents'),          # view component list

    # instructor editing mode
    #path('manage/<int:instructor_id>/<int:course_id>/add',views.addModule, name='manageModule'),                       # module list edit mode
    #path('manage/<int:instructor_id>/<int:course_id>/<int:module_id>/',views.manageComponent, name='showComponent'),      # component list edit mode
    #path('manage/<int:instructor_id>/<int:course_id>/<int: module>/quiz/', views.showQuizzes, name='showQuizzes'),    # add quiz view
    #path('view/<int:instructor_id>/<int:course_id>/<int:module_id>/', views.viewQuiz, name='viewQuiz'),

    # learner study mode
    #path('study/<int:learner_id>/<int:course_id>/<int:module_id>/quiz/', views.takeQuiz, name='takeQuiz'),                # learner take quiz
]
