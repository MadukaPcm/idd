import email
from django.shortcuts import render,redirect
from . models import REgisterdMember,User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import Group

# Create your views here.
def LoginView(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        Password = request.POST.get('password')
        
        user_obj = User.objects.filter(email=email).first()
        if user_obj is None:
            messages.info(request,'Email not found')
            return redirect('login_url')
        
        # profile_obj = Profile.objects.filter(user=user_obj).first()
        # if not profile_obj.is_verified:
        #     messages.info('User not verified')
        #     return redirect('login_url')
            
        user = authenticate(request, email=email, password=Password)
        if user is not None and user.is_active:
            login(request,user)
            messages.success(request,'your now logged in !!')
            return redirect('dashboard_url')
            
        else:
            messages.warning(request,"Invalid username or password")
            return redirect('login_url')
    
    context = {}
    return render(request,"login.html",context)

def RegisterView(request):
    
    if request.method == 'POST':
        regNo = request.POST.get('regNo')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        # first_name = request.POST.get('FirstName')
        # last_name = request.POST.get('LastName')
        # email = request.POST.get('Email')
        # PhoneNumber = request.POST.get('PhoneNumber')
        # NidaNumber = request.POST.get('NidaNumber')
        # DateofBirth = request.POST.get('DateofBirth')
        # Gender = request.POST.get('Gender')
        # profileImage = request.FILES.get('profileImage')
        
        try: 
            if not REgisterdMember.objects.filter(regNo=regNo).first():
                messages.info(request,'Registration Number Doest Not Exist')
                return redirect('/register')
                
            if User.objects.filter(username=regNo).first():
                messages.info(request,'Username is already taken')
                return redirect('/register')
        
            if User.objects.filter(email=email).first():
                messages.info(request,'Email is already taken')
                return redirect('/register')
            
            # if len(username) < 5:
            #     messages.info(request,'username, atlest 5 characters')
            #     return redirect('/register')
            
            # if len(PhoneNumber) < 11:
            #     messages.info(request,'Invalid phone number format')
            #     return redirect('/register')
            
            # if len(NidaNumber) < 20:
            #     messages.info(request,'Invalid Nida Number')
            #     return redirect('/register')
            
            if password != password1:
                messages.info(request,'password does not match')
                return redirect('/register')
            
            if len(password) < 8:
                messages.info(request, 'password, 8 mixed characters required')
                return redirect('/register')
                
            else:
                user_obj = User.objects.create_user(username=regNo, email=email,password=password)
                user_obj.save()
                
                grp = Group.objects.get(name="student")
                user= User.objects.get(username=regNo)
                user.groups.add(grp)

                return redirect('login_url')
            
                # user_obj.first_name = first_name
                # user_obj.last_name = last_name
                # user_obj.PhoneNumber = PhoneNumber
                # user_obj.NidaNumber = NidaNumber
                # user_obj.DateofBirth = DateofBirth
                # user_obj.Gender = Gender
                # user_obj.profileImage = profileImage
                # user_obj.save()
            
        except Exception as e:
            print(e)
    
    context = {}
    return render(request,"auth/register.html",context)


def DashboardView(request):
    
    context = {}
    return render(request,"auth/dashboard.html",context)

def ProfileView(request):
    
    context = {}
    return render(request,"auth/profile.html",context)

def AllUsersView(request):
    
    context = {}
    return render(request,"auth/allUsers.html",context)

