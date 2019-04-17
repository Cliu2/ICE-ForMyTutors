from django.urls import path
from django.conf.urls import url
from . import views
from .moreviews import manageModules, studyModule, moreviews, enrollment, auth

urlpatterns = [
    # both users
    path('view/<int:user_id>/', views.showCourses, name='showCourses'),                                               # view course list
    path('view/<int:user_id>/<int:course_id>/', views.showModules, name='showModules'),                               # view module list
    path('view/<int:user_id>/<int:course_id>/<int:module_id>/', studyModule.viewModule, name='viewModule'),      # view component list
    #path('view/<int:user_id>/<int:course_id>/<int:module_id>/', views.showComponents, name='showComponents'),          # view component list
    
    #authentication related
    path('loadHome/',auth.loadHome,name='loadHome'),   # by LC, redirect users to their home after login
    path('auth/sendInstructorLink/',auth.sendInstructorLink,name='sendInstructorLink'),
    url(r'^activateInstructor/(?P<uidb64>[0-9A-Za-z_\- ]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth.registerInstructor,name='registerInstructor'),
    path('auth/inviteInstructor/',auth.inviteInstructor,name='inviteInstructor'),
    path('auth/createInstructorAccount/',auth.createInstructorAccount,name='createInstructorAccount'),
    path('auth/requestAccountLearner/',auth.requestAccountLearner,name='requestAccountLearner'),
    path('auth/sendLearnerLink/',auth.sendLearnerLink,name='sendLearnerLink'),
    url(r'^activateLearner/(?P<uidb64>[0-9A-Za-z_\- ]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth.registerLearner,name='registerLearner'),
    path('auth/createLearnerAccount/',auth.createLearnerAccount,name='createLearnerAccount'),

    # instructor editing mode
    path('manage/<int:instructor_id>/addCourse/', views.createCourse, name='addCourse'),
    path('manage/<int:instructor_id>/editCourse/<int:course_id>/', views.editCourse, name='editCourse'),
    path('manage/<int:instructor_id>/<int:course_id>/requestAdd/', views.enterModuleInfo, name='enterModuleInfo'),
    path('manage/<int:instructor_id>/<int:course_id>/add/',views.addModule, name='manageModule'),
    path('manage/<int:instructor_id>/<int:course_id>/<int:module_id>/deleteModule/', views.deleteModule, name="deleteModule"),
    path('manage/<int:instructor_id>/<int:course_id>/<int:module_id>/selectQuiz/', views.showQuizzes, name='showQuizzes'),    # add quiz view
    path('manage/<int:instructor_id>/<int:course_id>/<int:module_id>/addQuiz/<int:quiz_id>/', views.addQuiz, name="addQuiz"),
    path('manage/<int:instructor_id>/<int:course_id>/<int:module_id>/<int:quiz_id>/removeQuiz/', views.removeQuiz, name="removeQuiz"),
    path('manage/<int:instructor_id>/<int:course_id>/<int:module_id>/addComponent/',manageModules.selectComponent, name='display_available_components'),
    path('manage/<int:instructor_id>/<int:course_id>/<int:module_id>/addComponent/<int:component_id>/',manageModules.addComponent, name='append_component'),
    path('manage/<int:instructor_id>/<int:course_id>/<int:module_id>/displayModuleContent/',manageModules.displayModuleContent,name='displayModuleContent'),
    path('manage/<int:instructor_id>/<int:course_id>/<int:module_id>/saveOrder/<slug:neworder>/',manageModules.saveOrder,name='saveOrder'),
    path('manage/<int:instructor_id>/<int:course_id>/<int:module_id>/removeComponent/<int:component_id>',manageModules.removeComponent,name='removeComponentFromModule'),

    path('manage/<int:instructor_id>/loadCourseInfo/<int:course_id>/', moreviews.loadCourseInfo, name='loadCourseInfo'),
    path('manage/<int:instructor_id>/loadCategory/', moreviews.loadCategory, name="loadCategory"),

    # learner study mode
    # path('view/<int:user_id>/', studyModule.viewEnrolled, name='viewEnrolled'),   # view course list
    # path('view/<int:user_id>/<int:course_id>/', views.viewCourse, name='viewCourse'),                           # view module list
    path('view/<int:learner_id>/browseCourse/', studyModule.browseCourse, name='browseCourse'),
    path('view/<int:learner_id>/enrollInCourse/<int:course_id>/', enrollment.enrollInCourse, name='enrollInCourse'),
    path('view/<int:user_id>/<int:course_id>/<int:module_id>/quiz/', studyModule.takeQuiz, name='takeQuiz'),        # learner takes quiz
    path('view/<int:user_id>/<int:course_id>/<int:module_id>/quiz/submitAnswer/', studyModule.submitAnswer, name='submitAnswer'),        # learner submits answer

    path('view/<int:learner_id>/loadCategoryForLearner/', moreviews.loadCategory, name='loadCategoryForLearner'),
    path('view/<int:learner_id>/browseCourse/detail/<int:course_id>/', views.viewCourseDetail, name='viewCourseDetail'),
    path('view/<int:learner_id>/viewCourseHistory/', studyModule.viewCourseHistory, name='viewCourseHistory'),
]
