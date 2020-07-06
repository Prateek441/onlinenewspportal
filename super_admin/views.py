from django.shortcuts import render,redirect
from .forms import LoginForm, SliderForm,AdminprofileForm, Add_News_Form,Add_Newsch_Form, UserForm,MediaForm,WelMsgForm
from django.contrib import messages
from .models import Admin, Adminprofile
from kg_news.models import ChPost, Slider, Media, Add_news_ch, WelMsg
from users.models import Users
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def admin_login(request):
    if request.session.get('ad_email'):
        return redirect('choice_dash')
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        email1 = request.POST.get('email')
        password1 = request.POST.get('password')

        f = Admin.objects.filter(email=email1, password=password1, status=False)
        if f.exists():
            messages.success(request, "You are blocked because of any reason!")
            return redirect('admin_login')
        u = Admin.objects.filter(email=email1, password=password1, status=True)
        if u.exists():
            request.session['ad_email'] = email1
            return redirect('choice_dash')
        else:
            messages.success(request, "Email or password didn't match!")

        print(u)
    context = {
        'form': form
    }
    return render(request, 'super_admin/login.html', context)

def admin_dash1(request):
    if not request.session.get('ad_email'):
        return redirect('admin_login')
    allslider = Slider.objects.all().count()
    magzine = Media.objects.filter().count()
    showallpost = ChPost.objects.filter(status=True).count()
    us = request.session.get('ad_email')
    u = Admin.objects.get(email=us)
    ad_pro = Adminprofile.objects.get(admin=u)
    dict={
        'allslider':allslider,
        'magzine':magzine,
        'showallpost':showallpost,
        'ad_pro':ad_pro
    }
    return render(request, 'super_admin/dashboard.html', dict)

def admin_dash2(request):
    if not request.session.get('ad_email'):
        return redirect('admin_login')
    allch = Add_news_ch.objects.all().count()
    totalpost = ChPost.objects.all().count()
    totaluser = Users.objects.all().count()
    totalblockuser = Users.objects.filter(status=False).count()
    activeusers = Users.objects.filter(status=True).count()
    blockpost = ChPost.objects.filter(status=False).count()
    unblockpost = ChPost.objects.filter(status=True).count()
    totaladmin = Admin.objects.filter(status=True).count()
    us = request.session.get('ad_email')
    u = Admin.objects.get(email=us)
    ad_pro = Adminprofile.objects.get(admin=u)
    dict={
        'allch':allch,
        'totalpost':totalpost,
        'blockpost':blockpost,
        'unblockpost':unblockpost,
        'totaluser':totaluser,
        'totalblockuser':totalblockuser,
        'activeusers':activeusers,
        'totaladmin':totaladmin
    }
    return render(request, 'super_admin/backend/dashboard2.html', dict)

def choice_dash(request):
    if not request.session.get('ad_email'):
        return redirect('admin_login')
    ademail = request.session.get('ad_email')
    Admindata = Admin.objects.filter(email=ademail)
    dict={
        'ademail':ademail,
        'Admindata':Admindata
    }
    return render(request, 'super_admin/choice_dashboard.html',dict)

def ad_slider(request):
    if not request.session.get('ad_email'):
        return redirect('admin_login')
    slider=Slider.objects.filter(status=True)
    form=SliderForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('ad_slider')
    dict={
        'slider':slider,
        'form':form
    }
    return render(request, 'super_admin/frontend/slider.html', dict)

def ad_media(request):
    if not request.session.get('ad_email'):
        return redirect('admin_login')
    slider=Media.objects.filter(status=True)
    form = MediaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print('ok')
        form.save()
        print('done')
        return redirect('ad_media')
    dict={
        'slider':slider,
        'form': form,
    }
    return render(request, 'super_admin/frontend/media.html', dict)

def delete_slider(request,id=None):
    if not request.session.get('ad_email'):
        return redirect('admin_login')
    print(id)
    m1 = Slider.objects.get(id=id)
    m1.delete()

    return redirect('ad_slider')

def edit_slider(request,id=None):
    if not request.session.get('ad_email'):
        return redirect('admin_login')


    uObj = Slider.objects.get(id=id)
    form = SliderForm(request.POST or None, request.FILES or None, instance=uObj)
    if form.is_valid():
        print('ok')
        form.save()
        print('done')
        return redirect('ad_slider')
    context = {
        'form': form,
    }
    return render(request, 'super_admin/frontend/edit_slider.html', context)

def all_users(request):
    if not request.session.get('ad_email'):
        return redirect('admin_login')
    users=Users.objects.all()
    blockuser=Users.objects.filter(status=False)
    activeuser=Users.objects.filter(status=True)
    dict={
        'users':users,
        'blockuser':blockuser,
        'activeuser':activeuser
    }
    return render(request, 'super_admin/backend/all_users.html', dict)

def all_channels(request):
    if not request.session.get('ad_email'):
        return redirect('admin_login')
    channels=Add_news_ch.objects.all()
    blockch=Add_news_ch.objects.filter(status=False)
    activech=Add_news_ch.objects.filter(status=True)
    page = request.GET.get('page', 1)

    paginator = Paginator(channels, 3)
    try:
        all_ch1 = paginator.page(page)
    except PageNotAnInteger:
        all_ch1 = paginator.page(1)
    except EmptyPage:
        all_ch1 = paginator.page(paginator.num_pages)

    page = request.GET.get('page', 1)

    paginator = Paginator(blockch, 3)
    try:
        block_ch1 = paginator.page(page)
    except PageNotAnInteger:
        block_ch1 = paginator.page(1)
    except EmptyPage:
        block_ch1 = paginator.page(paginator.num_pages)

    page = request.GET.get('page', 1)

    paginator = Paginator(activech, 3)
    try:
        activech1 = paginator.page(page)
    except PageNotAnInteger:
        activech1 = paginator.page(1)
    except EmptyPage:
        activech1 = paginator.page(paginator.num_pages)
    dict={
        'channels':all_ch1,
        'blockch':block_ch1,
        'activech':activech1
    }
    return render(request, 'super_admin/backend/all_channels.html', dict)

def all_posts(request):
    if not request.session.get('ad_email'):
        return redirect('admin_login')
    posts=ChPost.objects.all()
    blockpost=ChPost.objects.filter(status=False)
    activepost=ChPost.objects.filter(status=True)
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 3)
    try:
        posts1 = paginator.page(page)
    except PageNotAnInteger:
        posts1 = paginator.page(1)
    except EmptyPage:
        posts1 = paginator.page(paginator.num_pages)

    paginator = Paginator(blockpost, 3)
    try:
        blockpost1 = paginator.page(page)
    except PageNotAnInteger:
        blockpost1 = paginator.page(1)
    except EmptyPage:
        blockpost1 = paginator.page(paginator.num_pages)

    paginator = Paginator(activepost, 3)
    try:
        activepost1 = paginator.page(page)
    except PageNotAnInteger:
        activepost1 = paginator.page(1)
    except EmptyPage:
        activepost1 = paginator.page(paginator.num_pages)
    dict={
        'posts':posts1,
        'blockpost':blockpost1,
        'activepost':activepost1
    }
    return render(request, 'super_admin/backend/all_posts.html', dict)

def ad_edit_post(request, id=None):
    if not request.session.get('ad_email'):
        return redirect('admin_login')
    uObj = ChPost.objects.get(id=id)
    form = Add_News_Form(request.POST or None, request.FILES or None, instance=uObj)
    if form.is_valid():
        form.save()
        return redirect('all_posts')
    context = {
        'form': form,
    }
    return render(request, 'super_admin/backend/post_edit.html', context)

def ad_add_post(request):
    if not request.session.get('ad_email'):
        return redirect('admin_login')

    form = Add_News_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('all_posts')
    dict = {

        'form': form

    }
    return render(request, 'super_admin/backend/ad_add_post.html', dict)

def ad_add_newsch(request):
    if not request.session.get('ad_email'):
        return redirect('admin_login')

    form = Add_Newsch_Form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('all_channels')

    dict = {

        'form': form

    }
    return render(request, 'super_admin/backend/ad_add_ch.html', dict)

def delete_user(request,id=None):
    if not request.session.get('ad_email'):
        return redirect('admin_login')

    m1 = Users.objects.get(id=id)
    m1.delete()

    return redirect('all_users')

def ad_del_post(request,id=None):
    if not request.session.get('ad_email'):
        return redirect('admin_login')

    m1 = ChPost.objects.get(id=id)
    m1.delete()

    return redirect('all_posts')

def delete_ch(request,id=None):
    if not request.session.get('ad_email'):
        return redirect('admin_login')

    m1 = Add_news_ch.objects.get(id=id)
    m1.delete()

    return redirect('all_channels')

def edit_user(request,id=None):
    if not request.session.get('ad_email'):
        return redirect('admin_login')


    uObj = Users.objects.get(id=id)
    form = UserForm(request.POST or None, instance=uObj)
    if form.is_valid():
        print('ok')
        form.save()
        print('done')
        return redirect('all_users')
    context = {
        'form': form,

    }
    return render(request, 'super_admin/backend/edit_user.html', context)


def edit_ch(request,id=None):
    if not request.session.get('ad_email'):
        return redirect('admin_login')


    uObj = Add_news_ch.objects.get(id=id)
    form = Add_Newsch_Form(request.POST or None,request.FILES or None, instance=uObj)
    if form.is_valid():
        print('ok')
        form.save()
        print('done')
        return redirect('all_channels')
    context = {
        'form': form,
    }
    return render(request, 'super_admin/backend/edit_user.html', context)

def add_user(request):
    if not request.session.get('ad_email'):
        return redirect('admin_login')
    form=UserForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('all_users')
    context = {
        'form': form,
    }
    return render(request, 'super_admin/backend/add_user.html',context)

def edit_media(request,id=None):
    if not request.session.get('ad_email'):
        return redirect('admin_login')


    uObj = Media.objects.get(id=id)
    form = MediaForm(request.POST or None,request.FILES or None, instance=uObj)
    if form.is_valid():
        print('ok')
        form.save()
        print('done')
        return redirect('ad_media')
    context = {
        'form': form,

    }
    return render(request, 'super_admin/frontend/edit_media.html', context)

def edit_wel_msg(request,id=None):
    if not request.session.get('ad_email'):
        return redirect('admin_login')


    uObj = WelMsg.objects.get(id=id)
    form = WelMsgForm(request.POST or None,request.FILES or None, instance=uObj)
    if form.is_valid():
        form.save()
        return redirect('wel_msg')
    context = {
        'form': form,

    }
    return render(request, 'super_admin/frontend/edit_wel_msg.html', context)

def del_media(request,id=None):
    if not request.session.get('ad_email'):
        return redirect('admin_login')

    m1 = Media.objects.get(id=id)
    m1.delete()

    return redirect('ad_media')

def wel_msg(request):
    if not request.session.get('ad_email'):
        return redirect('admin_login')
    msg=WelMsg.objects.all()
    dict={
        'msg':msg
    }
    return render(request, 'super_admin/frontend/wel_msg.html', dict)

def ad_profile(request):
    if not request.session.get('ad_email'):
        return redirect('admin_login')
    ademail = request.session.get('ad_email')
    addetail = Admin.objects.get(email=ademail)
    adpro = Adminprofile.objects.get(admin=addetail)
    context = {
        'ademail': ademail,
        'u': addetail,
        'upro' : adpro,

    }


    return render(request, 'super_admin/ad_profile.html', context)

def ad_logout(request):
    del request.session['ad_email']
    return redirect('admin_login')

def edit_adpro(request, id=None):
    if not request.session.get('myemail'):
        return redirect('u_login')
    uObj = Adminprofile.objects.get(id=id)
    form = AdminprofileForm(request.POST or None, request.FILES or None, instance=uObj)
    if form.is_valid():
        form.save()
        return redirect('ad_profile')
    context = {
        'form': form
    }
    return render(request, 'super_admin/edit_adpro.html', context)