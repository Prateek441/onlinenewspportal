from django.shortcuts import render,redirect
from .models import Users, Userprofile
import random
from django.core.mail import send_mail
# Create your views here.
from .forms import SignpForm,LoginForm,UprofileForm
from django.contrib import messages
def sign_up(request):
    if 'verify' in request.POST:
        otp_val =request.POST.get('otp_val')
        otp1 =request.session.get('otp')
        username2 =request.session.get('username1')
        email2 =request.session.get('email1')
        password2 =request.session.get('password1')
        mobile2 =request.session.get('mobile1')
        # print(name2,email2,query2,otp_val)
        # print(otp_val,otp1)
        # 7762
        if int(otp_val)==int(otp1):
            print('sab sahi hai')
            Users.objects.create(username=username2,email=email2,password=password2,mobile=mobile2)
            del request.session['otp']
            del request.session['username1']
            del request.session['email1']
            del request.session['password1']
            del request.session['mobile1']


            return redirect('dashboard')


        else:
            messages.success(request,"OTP didn't match")
            return render(request, 'users/verification.html')
    form = SignpForm(request.POST or None)
    context = {
        'form':form
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        subject = 'KG News Portal OTP Verification'
        otp = random.randrange(1111, 9999)
        message = f'Thanks {username} for showing intreast in KG News Portal. Your OTP is {otp}. Please verify your email address to register your account successfully.'
        request.session['otp'] = otp
        request.session['username1'] = username
        request.session['email1'] = email
        request.session['password1'] = password
        request.session['mobile1'] = mobile
        print(username, email, password, mobile, otp)
        send_mail(subject, message, 'pkhandelwal2017@gmail.com', [email])
        return render(request, 'users/verification.html', )

    return render(request, 'users/signup.html', context)


def login(request):

    if request.session.get('myemail'):
        return redirect('dashboard')
    form =LoginForm(request.POST or None)
    if form.is_valid():
        email1 =form.cleaned_data.get('email')
        password1 =form.cleaned_data.get('password')
        print(email1,password1)

        u =Users.objects.filter(email=email1, password=password1, status=True)
        if u.exists():
            request.session['myemail']=email1
            return redirect('dashboard')
        f = Users.objects.filter(email=email1, password=password1, status=False)
        if f.exists():
            messages.success(request, "You are blocked because of any reason!")
            return redirect('u_login')
        else:
            messages.success(request, "Email or password didn't match!")

        print(u)
    context ={
        'form':form
    }
    return  render(request,'users/login.html',context)

def dashboard(request):
    if not request.session.get('myemail'):
        return redirect('u_login')
    form = UprofileForm(request.POST or None)
    us =request.session.get('myemail')
    u =Users.objects.get(email=us)
    upro = Userprofile.objects.get(user=u)
    context={
        'us':us,
        'u':u,
        'upro' : upro,
        'form' : form
    }
    return render(request,'users/dashboard.html',context)

def upro_edit(request, id=None):
    if not request.session.get('myemail'):
        return redirect('u_login')
    uObj = Userprofile.objects.get(id=id)
    form = UprofileForm(request.POST or None, request.FILES or None, instance=uObj)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'users/u_edit.html', context)

def logout(request):
    del request.session['myemail']
    return redirect('u_login')