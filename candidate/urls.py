from django.urls import path
from candidate import views
urlpatterns = [
     path('expjobs/',views.explorejobs,name='explorejobs'),
     path('candihome/',views.candihome,name='candihome'),
     path('dash/',views.candidateHome,name='dash'),
    #  path('',views.candidateHome,name='dash'),
     path('applyjob/<int:id>/',views.applyJob,name='applyjob'),
     path('applylist/',views.myjoblist,name='mylist')
]
