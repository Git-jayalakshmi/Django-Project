from django.urls import path,include
from. import views
app_name='todoapp'
urlpatterns = [
    path('',views.adddetails,name='adddetails'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.TaskListView.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetail')
#path('details/',views.details,name='details')
]
