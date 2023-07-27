# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('',views.index,name = 'index'),
#     path('complaint',views.complaint,name = 'complaint'),
#
#
# ]
from django.urls import path

from .views import HomePageView ,CreatePostView

urlpatterns =[
    path ('',HomePageView.as_view(), name = 'index'),
    path ('post', CreatePostView.as_view(),name='post'),

]
