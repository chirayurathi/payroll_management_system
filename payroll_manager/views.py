from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from datetime import datetime
from .models import *
import datetime
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'payroll_manager/index.html')
def employee_dashboard(request,emp_id):
    user_info=user_paygrade=user_pay=user_achieve=user_leave=None
    user = Account.objects.get(user_id = emp_id)
    if user == request.user:
        if MEmployee.objects.filter(employee= user).exists():
            user_info = MEmployee.objects.get(employee= user)
        if MPaygrade.objects.filter(employee= user_info).exists():
            user_paygrade = MPaygrade.objects.filter(employee=user_info).first()
        if MPay.objects.filter(employee= user_info).exists():
            user_pay = MPay.objects.filter(employee=user_info).first()
        if TAchievement.objects.filter(employee= user_info).exists():
            user_achieve = TAchievement.objects.filter(employee=user_info)
        if TLeave.objects.filter(employee= user_info).exists():
            user_leave = TLeave.objects.filter(employee=user_info)
        return render(request,'payroll_manager/employee_dashboard.html', context={'user_info':user_info,'user_paygrade':user_paygrade,'user_pay':user_pay,'user_achieve':user_achieve,'user_leave':user_leave})
    else:
        messages.info(request, 'You Are Not Authorized To Access That Page')
        return redirect('index')
def employee_login(request):
    if request.method == 'POST':
        Acc = Account()
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        user = authenticate(username = user_id , password = password )
        if user is not None:
            if Account.objects.filter(user_id=user_id, is_employee=True).exists():
                login(request,user)
                return redirect('employee_dashboard',emp_id=user_id)
            else:
                messages.info(request, 'Invalid, user not An Employee.')
                form = EmployeeLogin()
                return render(request,'payroll_manager/employee_login.html',context={'form':form})
        else:
            messages.info(request, 'Invalid Credentials.')
            form = EmployeeLogin()
            return render(request,'payroll_manager/employee_login.html',context={'form':form})
    form = EmployeeLogin()
    return render(request,'payroll_manager/employee_login.html',context={'form':form})

def admin_dashboard(request):
    if Account.objects.filter(user_id= request.user.user_id, is_employer=True):
        allEmp = MEmployee.objects.all()
        LeaveRequests = TLeave.objects.filter(is_approved=0)
        return render(request,'payroll_manager/admin_dashboard.html', context={'allEmp':allEmp, 'LeaveR':LeaveRequests})
    else:
        messages.info(request, 'You Are Not Authorized To Access That Page')
        return redirect('index')
def admin_login(request):
    if request.method == 'POST':
        Acc = Account()
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        user = authenticate(username = user_id , password = password )
        if user is not None:
            if Account.objects.filter(user_id=user_id, is_employer=True).exists():
                login(request,user)
                return redirect('admin_dashboard')
            else:
                messages.info(request, 'Invalid, user not An Admin.')
                form = EmployeeLogin()
                return render(request,'payroll_manager/admin_login.html',context={'form':form})
        else:
            messages.info(request, 'Invalid Credentials.')
            form = EmployeeLogin()
            return render(request,'payroll_manager/admin_login.html',context={'form':form})
    form = EmployeeLogin()
    return render(request,'payroll_manager/admin_login.html',context={'form':form})
def register(request):
    if request.method == 'POST':
        user = Account()
        if request.POST.get('password1') == request.POST.get('password2'):
            user.user_id = request.POST.get('user_id')
            user.set_password(request.POST.get('password1'))
            user.is_employee=True
            user.is_employer=False
            user.date_joined=datetime.datetime.now()
            user.save()
            add = MEmployee()

            add.employee = user
            add.employee_name = request.POST.get('employee_name')
            add.employee_doj = request.POST.get('employee_doj')
            add.department = MDepartment.objects.get(department_id=request.POST.get('department'))
            add.company = MCompany.objects.get(company_id=request.POST.get('company'))
            add.grade = MGrade.objects.get(grade_id=request.POST.get('grade'))
            add.save()
            return redirect('admin_dashboard')
    form = RegisterEmployeeForm()
    formSub = employeeInfoForm()
    return render(request,'payroll_manager/register.html',context={'form':form,'formSub':formSub})

def logoutUser(request):
    logout(request)
    return redirect('index')
def deleteAll(request):
    Account.objects.all().delete()
    return redirect('index')
def leaveApply(request,emp_id):
    user = Account.objects.get(user_id = emp_id)
    if user == request.user:
        if request.method == 'POST':
            leaveApp = TLeave()
            leaveApp.employee = MEmployee.objects.get(employee=user)
            leaveApp.fin_year= int(datetime.datetime.now().year)
            leaveApp.leave_date = request.POST.get('leave_date')
            leaveApp.leave_type=request.POST.get('leave_type')
            leaveApp.save()
            messages.success(request, 'Leave Application Submitted.')
            return redirect('employee_dashboard', emp_id=emp_id)
        leaveForm = leaveApplyForm()
        return render(request,'payroll_manager/leaveApply.html',context={'form':leaveForm})
def changeAddress(request,emp_id):
    user = Account.objects.get(user_id = emp_id)
    if True:
        if request.method == 'POST':
            if MAddress.objects.filter(memployee=MEmployee.objects.get(employee=user)).exists():
                add = MAddress.objects.filter(memployee=MEmployee.objects.get(employee=user)).first()
            else:
                add = MAddress()
                add.employee = MEmployee.objects.get(employee=user)
            add.building_details = request.POST.get('building_details')
            add.road = request.POST.get('road')
            add.landmark = request.POST.get('landmark')
            add.city = request.POST.get('city')
            add.state = MState.objects.get(state_code=request.POST.get('state')) 
            add.country = request.POST.get('country')
            add.save()
            messages.success(request, 'Address Details Updated.')
            if request.user.is_employer :
                return redirect('admin_dashboard')
            else: 
                return redirect('employee_dashboard', emp_id=emp_id)
        oldData = MAddress.objects.filter(memployee=MEmployee.objects.get(employee=user)).first()
        AddForm = addressForm(instance=oldData)
        return render(request,'payroll_manager/addressChange.html',context={'form':AddForm})
def admin_employee_dashboard(request,emp_id):
    user_info=user_paygrade=user_pay=user_achieve=user_leave=None
    user = Account.objects.get(user_id = emp_id)
    # if request.user.is_admin:
    if MEmployee.objects.filter(employee= user).exists():
        user_info = MEmployee.objects.get(employee= user)
    if MPaygrade.objects.filter(employee= user_info).exists():
        user_paygrade = MPaygrade.objects.filter(employee=user_info).first()
    if MPay.objects.filter(employee= user_info).exists():
        user_pay = MPay.objects.filter(employee=user_info).first()
    if TAchievement.objects.filter(employee= user_info).exists():
        user_achieve = TAchievement.objects.filter(employee=user_info)
    if TLeave.objects.filter(employee= user_info).exists():
        user_leave = TLeave.objects.filter(employee=user_info)
    return render(request,'payroll_manager/admin_employee_dashboard.html', context={'user_info':user_info,'user_paygrade':user_paygrade,'user_pay':user_pay,'user_achieve':user_achieve,'user_leave':user_leave})

def changePay(request,emp_id):
    user = Account.objects.get(user_id = emp_id)
    if True:
        if request.method == 'POST':
            if MPay.objects.filter(employee=MEmployee.objects.get(employee=user)).exists():
                addPay = MPay.objects.filter(employee=MEmployee.objects.get(employee=user)).first()
            else:
                addPay = MPay()
                addPay.employee = MEmployee.objects.get(employee=user)
            if MPaygrade.objects.filter(employee=MEmployee.objects.get(employee=user)).exists():
                addPaygrade = MPaygrade.objects.filter(employee=MEmployee.objects.get(employee=user)).first()
            else:
                addPaygrade = MPaygrade()
                addPaygrade.employee = MEmployee.objects.get(employee=user)
            addPay.employee = MEmployee.objects.get(employee=user)
            addPaygrade.employee = MEmployee.objects.get(employee=user)
            addPay.fin_year = int(datetime.datetime.now().year)
            addPay.gross_salary = request.POST.get('gross_salary')
            addPay.gross_dedn = request.POST.get('gross_dedn')
            addPay.net_salary = request.POST.get('net_salary')
            addPaygrade.grade = MEmployee.objects.get(employee=user).grade
            addPaygrade.basic_amt = request.POST.get('basic_amt')
            addPaygrade.da_amt = request.POST.get('da_amt')
            addPaygrade.pf_amt = request.POST.get('pf_amt')
            addPaygrade.medical_amt = request.POST.get('medical_amt')
            addPay.save()
            addPaygrade.save()
            messages.success(request, 'Income Details Updated.')
            return redirect('admin_dashboard')
        oldDataPay = MPay.objects.filter(employee=MEmployee.objects.get(employee=user)).first()
        oldDataPaygrade = MPaygrade.objects.filter(employee=MEmployee.objects.get(employee=user)).first()
        AddFormpay = payForm(instance=oldDataPay)
        AddFormpaygrade = paygradeForm(instance=oldDataPaygrade)
        return render(request,'payroll_manager/payChange.html',context={'formPay':AddFormpay,'formPaygrade':AddFormpaygrade})
def changeInfo(request,emp_id):
    user = Account.objects.get(user_id = emp_id)
    if True:
        if request.method == 'POST':
            if MEmployee.objects.filter(employee=user).exists():
                add = MEmployee.objects.get(employee=user)
            else:
                add = MEmployee()
                add.employee = user
            add.employee_name = request.POST.get('employee_name')
            add.employee_doj = request.POST.get('employee_doj')
            add.department = MDepartment.objects.get(department_id=request.POST.get('department'))
            add.company = MCompany.objects.get(company_id=request.POST.get('company'))
            add.grade = MGrade.objects.get(grade_id=request.POST.get('grade'))
            add.save()
            messages.success(request, 'Personal Details Updated.')
            return redirect('admin_dashboard')
        oldData = MEmployee.objects.get(employee=user)
        AddForm = employeeInfoForm(instance=oldData)
        return render(request,'payroll_manager/infoChange.html',context={'form':AddForm})
def changeAchievement(request,emp_id):
    user = Account.objects.get(user_id = emp_id)
    if request.method == 'POST':
        achievement = TAchievement()
        achievement.employee = MEmployee.objects.get(employee=user)
        achievement.achievement_date = request.POST.get('achievement_date')
        achievement.achievement_type = request.POST.get('achievement_type')
        achievement.save()
        return redirect('admin_dashboard')
    form = AchievementForm()
    return render(request,'payroll_manager/achievementChange.html',context={'form':form})
def approval(request,leave_id,app_id):
    leave = TLeave.objects.get(leave_id=leave_id)
    if app_id == 1:
        leave.is_approved = 1
    else:
        leave.is_approved = -1
    leave.save()
    return redirect('admin_dashboard')