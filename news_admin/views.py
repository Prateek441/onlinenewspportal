from django.shortcuts import render, redirect
from .forms import LoginForm, Add_News_Form
from kg_news.models import Add_news_ch,ChannelDetails, ChPost
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def ch_login(request):

    if request.session.get('chemail'):
        return redirect('ch_dash')
    form =LoginForm(request.POST or None)
    if request.method=="POST":
        email1 =request.POST.get('email')
        password1 =request.POST.get('password')
        
        f = Add_news_ch.objects.filter(email=email1, password=password1, status=False)
        if f.exists():
            messages.success(request, "You are blocked because of any reason!")
            return redirect('ch_login')
        u =Add_news_ch.objects.filter(email=email1, password=password1, status=True)
        if u.exists():
            request.session['chemail']=email1
            return redirect('ch_dash')
        else:
            messages.success(request, "Email or password didn't match!")

        print(u)
    context ={
        'form':form
    }
    return  render(request,'ch_admin/login.html',context)

def ch_dash(request):
    if not request.session.get('chemail'):
        return redirect('ch_login')
    chid = request.session.get('chid')
    chemail=request.session.get('chemail')
    chdetail = Add_news_ch.objects.filter(email=chemail)
    chpost=ChPost.objects.filter(ch_post=chid).count()

    blockchpost=ChPost.objects.filter(status=False,ch_post=chid).count()
    showchpost=ChPost.objects.filter(status=True,ch_post=chid).count()
    dict={
        'chdetail':chdetail,
        'chpost':chpost,
        'blockchpost':blockchpost,
        'showpost':showchpost,

    }
    return render(request, 'ch_admin/dashboard.html', dict)

def ch_profile(request):
    if not request.session.get('chemail'):
        return redirect('ch_login')
    chemail = request.session.get('chemail')
    chdetail = Add_news_ch.objects.filter(email=chemail)

    context = {
        'chemail': chemail,
        'chdetail': chdetail,


    }


    return render(request, 'ch_admin/ch_profile.html', context)

def ch_add_post(request):
    if not request.session.get('chemail'):
        return redirect('ch_login')
    chid = request.session.get('chid')
    uObj = Add_news_ch.objects.get(id=chid)
    form = Add_News_Form(request.POST or None, request.FILES or None, instance=uObj)
    if form.is_valid():
        form.save()
    chemail=request.session.get('chemail')
    chdetail = Add_news_ch.objects.filter(email=chemail)
    dict = {
        'chdetail': chdetail,
        'form':form


    }
    return render(request, 'ch_admin/ch_add_post.html', dict)

def ch_all_post(request):
    chid = request.session.get('chid')
    all_post = ChPost.objects.filter(status=True, ch_post_id=chid).order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(all_post, 3)
    try:
        all_post1 = paginator.page(page)
    except PageNotAnInteger:
        all_post1 = paginator.page(1)
    except EmptyPage:
        all_post1 = paginator.page(paginator.num_pages)
    chemail = request.session.get('chemail')
    chdetail = Add_news_ch.objects.filter(email=chemail)
    dict = {

        'chdetail': chdetail,
        'all_post1': all_post1,

    }
    return render(request, 'ch_admin/ch_all_post.html', dict)

def ch_total_post(request):
    chid = request.session.get('chid')
    all_post = ChPost.objects.filter(ch_post_id=chid).order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(all_post, 3)
    try:
        all_post1 = paginator.page(page)
    except PageNotAnInteger:
        all_post1 = paginator.page(1)
    except EmptyPage:
        all_post1 = paginator.page(paginator.num_pages)
    chemail = request.session.get('chemail')
    chdetail = Add_news_ch.objects.filter(email=chemail)
    dict = {

        'chdetail': chdetail,
        'all_post1': all_post1,

    }
    return render(request, 'ch_admin/ch_total_post.html', dict)

def ch_block_post(request):
    chid = request.session.get('chid')
    all_post = ChPost.objects.filter(status=False, ch_post_id=chid).order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(all_post, 3)
    try:
        all_post1 = paginator.page(page)
    except PageNotAnInteger:
        all_post1 = paginator.page(1)
    except EmptyPage:
        all_post1 = paginator.page(paginator.num_pages)
    chemail = request.session.get('chemail')
    chdetail = Add_news_ch.objects.filter(email=chemail)
    dict = {

        'chdetail': chdetail,
        'all_post1': all_post1,

    }
    return render(request, 'ch_admin/ch_block_post.html', dict)

def delete_record(request,id=None):
    if not request.session.get('chemail'):
        return redirect('ch_login')
    print(id)
    m1 = ChPost.objects.get(id=id)
    m1.delete()

    return redirect('ch_all_post')

def edit_record(request,id=None):
    if not request.session.get('chemail'):
        return redirect('ch_login')
    chemail = request.session.get('chemail')
    chdetail = Add_news_ch.objects.filter(email=chemail)
    uObj = ChPost.objects.get(id=id)
    form = Add_News_Form(request.POST or None, request.FILES or None, instance=uObj)
    if form.is_valid():
        form.save()
        return redirect('ch_all_post')
    context = {
        'form': form,
        'chdetail':chdetail
    }
    return render(request, 'ch_admin/post_edit.html', context)

def del_block_post(request,id=None):
    if not request.session.get('chemail'):
        return redirect('ch_login')
    print(id)
    m1 = ChPost.objects.get(id=id)
    m1.delete()

    return redirect('ch_block_post')

def edit_block_post(request,id=None):
    if not request.session.get('chemail'):
        return redirect('ch_login')
    chemail = request.session.get('chemail')
    chdetail = Add_news_ch.objects.filter(email=chemail)
    uObj = ChPost.objects.get(id=id)
    form = Add_News_Form(request.POST or None, request.FILES or None, instance=uObj)
    if form.is_valid():
        form.save()
        return redirect('ch_block_post')
    context = {
        'form': form,
        'chdetail': chdetail,

    }
    return render(request, 'ch_admin/post_edit.html', context)

def del_post_t(request,id=None):
    if not request.session.get('chemail'):
        return redirect('ch_login')
    print(id)
    m1 = ChPost.objects.get(id=id)
    m1.delete()

    return redirect('ch_total_post')

def edit_post_t(request,id=None):
    if not request.session.get('chemail'):
        return redirect('ch_login')
    chemail = request.session.get('chemail')
    chdetail = Add_news_ch.objects.filter(email=chemail)
    uObj = ChPost.objects.get(id=id)
    form = Add_News_Form(request.POST or None, request.FILES or None, instance=uObj)
    if form.is_valid():
        form.save()
        return redirect('ch_total_post')
    context = {
        'form': form,
        'chdetail':chdetail
    }
    return render(request, 'ch_admin/post_edit.html', context)

def ch_dashboard(request):
    return render(request, 'ch_admin/dashboard.html')

def ch_logout(request):
    del request.session['chemail']
    return redirect('ch_login')
