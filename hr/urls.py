from django.urls import path
from hr import views
urlpatterns = [
    # path('hrdash/',views.HHhome,name='hrdash'),
    path('hrhome/',views.hrhome,name='hrhome'),
    path('hrdash/',views.hrHome,name='hrdash'),
    path('candidatedetails/<int:id>/',views.hrCandidateDetails,name='candidatedetails'),
    path('candidatedetails/<int:id>/',views.hrCandidateDetails1,name='candidatedetails'),
    path('postjob/',views.postJobs,name='postjob'),
    path('acceptapplication/',views.acceptApplication,name='acceptapplication'),
    path('rejectapplication/',views.rejectApplication,name='rejectapplication')
]
