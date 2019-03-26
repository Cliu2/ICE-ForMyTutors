from django.urls import path
from . import views
from .moreviews import manageModules

urlpatterns = [
    # both users
    path('view/<int:user_id>/', views.showCourses, name='showCourses'),                                               # view course list
    path('view/<int:user_id>/<int:course_id>/', views.showModules, name='showModules'),                               # view module list
    #path('view/<int:user_id>/<int:course_id>/<int:module_id>/', views.showComponents, name='showComponents'),          # view component list

    # instructor editing mode
    path('manage/<int:instructor_id>/<int:course_id>/requestAdd/', views.enterModuleInfo, name='enterModuleInfo'),
    path('manage/<int:instructor_id>/<int:course_id>/add/',views.addModule, name='manageModule'),                       
    path('manage/<int:instructor_id>/<int:course_id>/<int:module_id>/deleteModule/', views.deleteModule, name="deleteModule"),
    path('manage/<int:instructor_id>/<int:course_id>/<int:module_id>/selectQuiz/', views.showQuizzes, name='showQuizzes'),    # add quiz view
    path('manage/<int:instructor_id>/<int:course_id>/<int:module_id>/addQuiz/<int:quiz_id>/', views.addQuiz, name="addQuiz"),
    path('manage/<int:instructor_id>/<int:course_id>/<int:module_id>/addComponent/',manageModules.selectComponent, name='display_available_components'),
    path('manage/<int:instructor_id>/<int:course_id>/<int:module_id>/addComponent/<int:component_id>/',manageModules.addComponent, name='append_component'),
    path('manage/<int:instructor_id>/<int:course_id>/<int:module_id>/displayModuleContent/',manageModules.displayModuleContent,name='displayModuleContent'),
    path('manage/<int:instructor_id>/<int:course_id>/<int:module_id>/displayModuleContent/saveOrder/<slug:neworder>/',manageModules.saveOrder,name='saveOrder')
    # learner study mode
    #path('study/<int:learner_id>/<int:course_id>/<int:module_id>/quiz/', views.takeQuiz, name='takeQuiz'),                # learner take quiz
]
