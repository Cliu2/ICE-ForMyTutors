from django.urls import path
from . import views

urlpatterns = [
    # both users
    path('view/<int:user_id>/', views.showCourses.as_view(), name='showCourses'),                                               # view course list
    path('view/<int:user_id>/<int:course_id>/', views.showModules.as_view(), name='showModules'),                               # view module list
    path('view/<int:user_id>/<int:course_id>/<int:module_id>', views.ShowComponents.as_view(), name='showComponents'),          # view component list

    # instructor editing mode
    path('manage/<int:instructor_id>/<int:course_id>/',views.ManageModule.as_view(),name='manageModule'),                       # module list edit mode
    path('manage/<int:instructor_id>/<int:course_id>/<int:module>/',views.showComponent.as_view(),name='showComponent'),        # component list edit mode
    path('manage/<int:instructor_id>/<int:course_id>/<int: module>/quiz/', views.showQuizzes.as_view(), name='showQuizzes'),    # add quiz view
    path('view/<int:instructor_id>/<int:course_id>/<int:module_id>/', views.viewQuiz.as_view(), name='viewQuiz'),

    # learner study mode
    path('study/<int:learner_id>/<int:course_id>/<int:module_id>/quiz/', views.takeQuiz, name='takeQuiz'),                # learner take quiz
]
