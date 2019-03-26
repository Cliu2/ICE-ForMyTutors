from django.test import TestCase

# Create your tests here.

#
# ForMyTutors id=1
# Instructor1 id=5
# Instructor2 id=7
# Instructor3 id=10
# Instructor4 id=11
# Learner1 id=12
# Learner2 id=13
# Learner3 id=14
# Learner4 id=15
#
#
# success senario
# learner2:
#   view enrolled courses: http://127.0.0.1:8000/system/view/13/
#   view modules in course 1: http://127.0.0.1:8000/system/view/13/1/
#   view components in module 1 entitled: <<It has an order 0>>: http://127.0.0.1:8000/system/view/13/1/4/
#   take quiz of module 1: http://127.0.0.1:8000/system/view/13/1/4/quiz/
#   submit answer: http://127.0.0.1:8000/system/view/13/1/4/quiz/submitAnswer/
# 
# 
# 
# 
# 
# 
# 
# 