from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
     path('teachers/', views.TeacherListView.as_view(), name='teachers'),
     path('teacher/<int:pk>', views.TeacherDetailView.as_view(), name='teacher-detail'),
     path('students/', views.StudentListView.as_view(), name='students'),
     path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
 	path('locations/', views.LocationListView.as_view(), name='locations'),
 	path('location/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),
]
urlpatterns += [
    path('location/create/', views.LocationCreate.as_view(), name='location_create'),
    path('location/<int:pk>/update/', views.LocationUpdate.as_view(), name='location_update'),
    path('location/<int:pk>/delete/', views.LocationDelete.as_view(), name='location_delete'),
]
urlpatterns += [
    path('student/create/', views.StudentCreate.as_view(), name='student_create'),
    path('student/<int:pk>/update/', views.StudentUpdate.as_view(), name='student_update'),
    path('student/<int:pk>/delete/', views.StudentDelete.as_view(), name='student_delete'),
]
urlpatterns += [
    path('teacher/create/', views.TeacherCreate.as_view(), name='teacher_create'),
    path('teacher/<int:pk>/update/', views.TeacherUpdate.as_view(), name='teacher_update'),
    path('teacher/<int:pk>/delete/', views.TeacherDelete.as_view(), name='teacher_delete'),
]
