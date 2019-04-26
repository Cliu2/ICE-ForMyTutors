from django.urls import path
from django.conf.urls import url
from . import views
from .moreviews import manageModules, studyModule, moreviews, enrollment, auth

urlpatterns = [
    # both users
    path('view/', views.showCourses, name='showCourses'),                                               # view course list
    path('view/<int:course_id>/', views.showModules, name='showModules'),                               # view module list
    path('view/<int:course_id>/<int:module_id>/', studyModule.viewModule, name='viewModule'),      # view component list
    #path('view/<int:user_id>/<int:course_id>/<int:module_id>/', views.showComponents, name='showComponents'),          # view component list

    #authentication related
    path('loadHome/',auth.loadHome,name='loadHome'),   # by LC, redirect users to their home after login
    path('auth/sendInstructorLink/',auth.sendInstructorLink,name='sendInstructorLink'),
    url(r'^activateInstructor/(?P<uidb64>[0-9A-Za-z_\- ]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth.registerInstructor,name='registerInstructor'),
    path('auth/inviteInstructor/',auth.inviteInstructor,name='inviteInstructor'),
    path('auth/createInstructorAccount/',auth.createInstructorAccount,name='createInstructorAccount'),
    path('auth/requestAccountLearner/',auth.requestAccountLearner,name='requestAccountLearner'),
    path('auth/sendLearnerLink/',auth.sendLearnerLink,name='sendLearnerLink'),
    url(r'^activateLearner/(?P<first_name>[0-9A-Za-z_\- ]+)/(?P<last_name>[0-9A-Za-z_\- ]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth.registerLearner,name='registerLearner'),
    path('auth/createLearnerAccount/',auth.createLearnerAccount,name='createLearnerAccount'),

    # instructor editing mode
    path('manage/createCourse/', views.createCourse, name='createCourse'),
    path('manage/editCourse/<int:course_id>/', views.editCourse, name='editCourse'),
    # path('manage/<int:instructor_id>/<int:course_id>/requestAdd/', views.enterModuleInfo, name='enterModuleInfo'),
    path('manage/<int:course_id>/createModule/',views.createModule, name='createModule'),
    path('manage/<int:course_id>/<int:module_id>/deleteModule/', views.deleteModule, name="deleteModule"),
    path('manage/<int:course_id>/<int:module_id>/selectQuiz/', views.showQuizzes, name='showQuizzes'),    # add quiz view
    path('manage/<int:course_id>/<int:module_id>/addQuiz/<int:quiz_id>/', views.addQuiz, name="addQuiz"),
    path('manage/<int:course_id>/<int:module_id>/<int:quiz_id>/removeQuiz/', views.removeQuiz, name="removeQuiz"),
    path('manage/<int:course_id>/<int:module_id>/selectComponent/',manageModules.selectComponent, name='display_available_components'),
    path('manage/<int:course_id>/<int:module_id>/addComponent/',manageModules.addComponent, name='append_component'),
    path('manage/<int:course_id>/<int:module_id>/loadComponents/', manageModules.loadComponents, name='loadComponents'),
    path('manage/<int:course_id>/<int:module_id>/displayModuleContent/',manageModules.displayModuleContent,name='displayModuleContent'),
    path('manage/<int:course_id>/<int:module_id>/saveOrder/<slug:neworder>/',manageModules.saveOrder,name='saveOrder'),
    path('manage/<int:course_id>/saveModuleOrder/<slug:neworder>/',manageModules.saveModuleOrder,name='saveModuleOrder'),
    path('manage/<int:course_id>/<int:module_id>/<int:component_id>/removeComponent/',manageModules.removeComponent,name='removeComponentFromModule'),

    path('manage/loadCourseInfo/<int:course_id>/', moreviews.loadCourseInfo, name='loadCourseInfo'),
    path('manage/loadCategory/', moreviews.loadCategory, name="loadCategory"),

    # learner study mode
    # path('view/<int:user_id>/', studyModule.viewEnrolled, name='viewEnrolled'),   # view course list
    # path('view/<int:user_id>/<int:course_id>/', views.viewCourse, name='viewCourse'),                           # view module list
    path('view/browseCourse/', studyModule.browseCourse, name='browseCourse'),
    path('view/enrollInCourse/<int:course_id>/', enrollment.enrollInCourse, name='enrollInCourse'),
    path('view/dropCourse/<int:course_id>/', enrollment.dropCourse, name='dropCourse'),
    path('view/<int:course_id>/<int:module_id>/quiz/', studyModule.takeQuiz, name='takeQuiz'),        # learner takes quiz
    path('view/<int:course_id>/<int:module_id>/quiz/submitAnswer/', studyModule.submitAnswer, name='submitAnswer'),        # learner submits answer

    path('view/loadCategoryForLearner/', moreviews.loadCategory, name='loadCategoryForLearner'),
    path('view/browseCourse/detail/<int:course_id>/', views.viewCourseDetail, name='viewCourseDetail'),
    path('view/viewCourseHistory/', studyModule.viewCourseHistory, name='viewCourseHistory'),
]
