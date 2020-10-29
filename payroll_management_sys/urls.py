"""payroll_management_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from payroll_manager import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index , name='index'),
    path('employee_login/', views.employee_login, name='employee_login'),
    path('employee_dashboard/<int:emp_id>', views.employee_dashboard, name='employee_dashboard'),
    path('employee_dashboard/<int:emp_id>/LeaveApply', views.leaveApply, name='leaveApply'),
    path('employee_dashboard/<int:emp_id>/addressChange', views.changeAddress, name='changeAddress'),
    path('employee_dashboard/<int:emp_id>/payChange', views.changePay, name='changePay'),
    path('employee_dashboard/<int:emp_id>/infoChange', views.changeInfo, name='changeInfo'),
    path('employee_dashboard/<int:emp_id>/achievementChange', views.changeAchievement, name='changeAchievement'),
    path('approval/<int:leave_id>/<int:app_id>/', views.approval, name='approval'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_dashboard/<int:emp_id>/', views.admin_employee_dashboard, name='admin_employee_dashboard'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('deleteAll', views.deleteAll, name="deleteAll"),
]
