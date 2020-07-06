from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import ChPost,Add_news_ch,Query,Slider, WelMsg,Media,State,Categories
from users.models import Users, Userprofile
from django.core.mail import send_mail
from django.contrib import messages
import random
from django.db.models import Q
from .forms import FilterForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(request):
    all_slider = Slider.objects.filter(status=True)
    welMsg = WelMsg.objects.all()
    media1 = Media.objects.filter(status=True).order_by('id')

    dict = {
        'all_slider': all_slider,
        'WelMsg': welMsg,
        'Media2': media1
    }
    return render(request, 'index.html', dict)

def about(request):
    return render(request, 'about.html')

def channels(request):
    all_ch = Add_news_ch.objects.filter(status=True)
    page = request.GET.get('page', 1)

    paginator = Paginator(all_ch, 3)
    try:
        all_ch2 = paginator.page(page)
    except PageNotAnInteger:
        all_ch2 = paginator.page(1)
    except EmptyPage:
        all_ch2 = paginator.page(paginator.num_pages)

    context = {
        'all_ch1': all_ch2,

    }


    return render(request, 'channels.html', context)

def contact(request):
    if 'verify' in request.POST:
        otp_val =request.POST.get('otp_val')
        otp1 =request.session.get('otp')
        name2 =request.session.get('name1')
        email2 =request.session.get('email1')
        query2 =request.session.get('query1')

        if int(otp_val)==int(otp1):
            Query.objects.create(name=name2,email=email2,query=query2)
            messages.success(request,"Your Query has been sent successfully!")
            # print('bn gya account jao maza karo')
            del request.session['otp']
            del request.session['name1']
            del request.session['email1']
            del request.session['query1']


            return redirect('contact')


        else:
            messages.success(request,"OTP didn't match!")
            return render(request, 'verification.html')


    if request.method == 'POST':
        name = request.POST.get('cname')
        email = request.POST.get('cemail')
        query = request.POST.get('cquery')
        subject = 'KG News Portal OTP Verification'
        otp = random.randrange(1111, 9999)
        message = f'Thanks {name} for showing intreast in KG News Portal. Your OTP is {otp}. Please verify your otp to send your query. We will reach you soon.'
        request.session['otp'] = otp
        request.session['name1'] = name
        request.session['email1'] = email
        request.session['query1'] = query
        send_mail(subject,message,'pkhandelwal2017@gmail.com',[email])
        return render(request, 'verification.html',)

    return render(request, 'contact.html')

def portal(request, id=None):
    if not request.session.get('myemail'):
        return redirect('u_login')
    chid = request.session.get('chid')
    chdetail=Add_news_ch.objects.filter(id=id)
    request.session['chid'] = id
    state=State.objects.filter(status=True)
    all_post=ChPost.objects.filter(ch_post_id=id, status=True).order_by('-id')
    us = request.session.get('myemail')
    u = Users.objects.get(email=us)
    upro = Userprofile.objects.get(user=u)
    cat= Categories.objects.filter(status=True)
    post_id = request.COOKIES.get('post_id')
    filterform=FilterForm(request.POST or None)
    if request.method=='POST':
        srch = request.POST.get('srh')
        state2 = request.POST.get('state')
        category = request.POST.get('category')
        print(state, cat)
        if 'filter' in request.POST:
            if state2=="" and category=="":
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            elif state2=="":
                match=ChPost.objects.filter(category=category, ch_post_id=chid)
            elif category=="":
                match= ChPost.objects.filter(state=state2,  ch_post_id=chid)
            else:
                match=ChPost.objects.filter(state=state2, category=category,  ch_post_id=chid)
            dict={
                'match1':match,
                'chdetail1': chdetail,
                'state1': state,
                'us1': us,
                'u1': u,
                'upro1': upro,
                'cat1': cat,

            }

            return render(request, 'portal/filter.html', dict)
        if srch:
            match=ChPost.objects.filter(Q(title__icontains=srch) | Q(Description__icontains=srch) | Q(sub_title__icontains=srch), ch_post_id=chid)
            page = request.GET.get('page', 1)

            paginator = Paginator(match, 4)
            try:
                match1 = paginator.page(page)
            except PageNotAnInteger:
                match1 = paginator.page(1)
            except EmptyPage:
                match1 = paginator.page(paginator.num_pages)
            if match:
                dict={
                    'chdetail1': chdetail,
                    'state1': state,
                    'us1': us,
                    'u1': u,
                    'upro1': upro,
                    'cat1': cat,
                    'sr':match1
                }
                return render(request, 'portal/search.html', dict)
            else:
                dict = {
                    'chdetail1': chdetail,
                    'state1': state,
                    'us1': us,
                    'u1': u,
                    'upro1': upro,
                    'cat1': cat,
                }
                messages.error(request, 'Sorry! no result found')
                return render(request, 'portal/search.html', dict)
        else:
            return redirect('portal')
    rec_post = ChPost.objects.filter(id=post_id)
    page = request.GET.get('page', 1)

    paginator = Paginator(all_post, 6)
    try:
        all_post1 = paginator.page(page)
    except PageNotAnInteger:
        all_post1 = paginator.page(1)
    except EmptyPage:
        all_post1 = paginator.page(paginator.num_pages)


    dict={
        'all_post1':all_post1,
        'chdetail1' : chdetail,
        'state1':state,
        'us1':us,
        'u1':u,
        'upro1':upro,
        'cat1':cat,
        'rec_post1':rec_post,
        'filterform':filterform
    }
    return render(request, 'portal/portal_dash.html', dict)

def details(request, id=None):
    if not request.session.get('myemail'):
        return redirect('u_login')
    a = ChPost.objects.get(id=id)
    chid=request.session.get('chid')
    chdetail = Add_news_ch.objects.filter(id=chid)
    state = State.objects.filter(status=True)
    us = request.session.get('myemail')
    u = Users.objects.get(email=us)
    upro = Userprofile.objects.get(user=u)
    cat = Categories.objects.filter(status=True)
    post_id = request.COOKIES.get('post_id')
    if request.method=='POST':
        srch = request.POST['srh']
        if srch:
            match=ChPost.objects.filter(Q(title__icontains=srch) | Q(Description__icontains=srch) | Q(sub_title__icontains=srch), ch_post_id=chid)
            page = request.GET.get('page', 1)

            paginator = Paginator(match, 4)
            try:
                match1 = paginator.page(page)
            except PageNotAnInteger:
                match1 = paginator.page(1)
            except EmptyPage:
                match1 = paginator.page(paginator.num_pages)
            if match:
                dict={
                    'chdetail1': chdetail,
                    'state1': state,
                    'us1': us,
                    'u1': u,
                    'upro1': upro,
                    'cat1': cat,
                    'sr':match1
                }
                return render(request, 'portal/search.html', dict)
            else:
                dict = {
                    'chdetail1': chdetail,
                    'state1': state,
                    'us1': us,
                    'u1': u,
                    'upro1': upro,
                    'cat1': cat,
                }
                messages.error(request, 'Sorry! no result found')
                return render(request, 'portal/search.html', dict)
        else:
            return redirect('portal')

    rec_post = ChPost.objects.filter(id=post_id)
    context = {
        'a': a,
        'rec_post1':rec_post,
        'chdetail1': chdetail,
        'state1': state,
        'us1': us,
        'u1': u,
        'upro1': upro,
        'cat1': cat,
    }
    res = render(request, 'portal/news_detail.html', context)
    res.set_cookie('post_id', id)
    return res

def state_news(request, id=None):
    if not request.session.get('myemail'):
        return redirect('u_login')
    a = State.objects.filter(id=id)
    chid = request.session.get('chid')
    chdetail = Add_news_ch.objects.filter(id=chid)
    state = State.objects.filter(status=True)
    us = request.session.get('myemail')
    u = Users.objects.get(email=us)
    upro = Userprofile.objects.get(user=u)
    cat = Categories.objects.filter(status=True)
    post_id = request.COOKIES.get('post_id')
    if request.method=='POST':
        srch = request.POST['srh']
        if srch:
            match=ChPost.objects.filter(Q(title__icontains=srch) | Q(Description__icontains=srch) | Q(sub_title__icontains=srch), ch_post_id=chid)
            page = request.GET.get('page', 1)

            paginator = Paginator(match, 4)
            try:
                match1 = paginator.page(page)
            except PageNotAnInteger:
                match1 = paginator.page(1)
            except EmptyPage:
                match1 = paginator.page(paginator.num_pages)
            if match:
                dict={
                    'chdetail1': chdetail,
                    'state1': state,
                    'us1': us,
                    'u1': u,
                    'upro1': upro,
                    'cat1': cat,
                    'sr':match1
                }
                return render(request, 'portal/search.html', dict)
            else:
                dict = {
                    'chdetail1': chdetail,
                    'state1': state,
                    'us1': us,
                    'u1': u,
                    'upro1': upro,
                    'cat1': cat,
                }
                messages.error(request, 'Sorry! no result found')
                return render(request, 'portal/search.html', dict)
        else:
            return redirect('portal')
    rec_post = ChPost.objects.filter(id=post_id)
    all_post = ChPost.objects.filter(state_id=id, status=True, ch_post_id=chid).order_by('-id')
    context={
        'b' : a,
        'rec_post1':rec_post,
        'all_post1':all_post,
        'chdetail1': chdetail,
        'state1': state,
        'us1': us,
        'u1': u,
        'upro1': upro,
        'cat1': cat,
    }

    return render(request, 'portal/state_news.html', context)

def cate_news(request, id=None):
    if not request.session.get('myemail'):
        return redirect('u_login')
    chid = request.session.get('chid')
    a=Categories.objects.filter(id=id)
    all_post = ChPost.objects.filter(category_id=id, status=True, ch_post_id=chid).order_by('-id')
    chid = request.session.get('chid')
    chdetail = Add_news_ch.objects.filter(id=chid)
    state = State.objects.filter(status=True)
    us = request.session.get('myemail')
    u = Users.objects.get(email=us)
    upro = Userprofile.objects.get(user=u)
    cat = Categories.objects.filter(status=True)
    post_id = request.COOKIES.get('post_id')
    if request.method=='POST':
        srch = request.POST['srh']
        if srch:
            match=ChPost.objects.filter(Q(title__icontains=srch) | Q(Description__icontains=srch) | Q(sub_title__icontains=srch), ch_post_id=chid)
            page = request.GET.get('page', 1)

            paginator = Paginator(match, 4)
            try:
                match1 = paginator.page(page)
            except PageNotAnInteger:
                match1 = paginator.page(1)
            except EmptyPage:
                match1 = paginator.page(paginator.num_pages)
            if match:
                dict={
                    'chdetail1': chdetail,
                    'state1': state,
                    'us1': us,
                    'u1': u,
                    'upro1': upro,
                    'cat1': cat,
                    'sr':match1
                }
                return render(request, 'portal/search.html', dict)
            else:
                dict = {
                    'chdetail1': chdetail,
                    'state1': state,
                    'us1': us,
                    'u1': u,
                    'upro1': upro,
                    'cat1': cat,
                }
                messages.error(request, 'Sorry! no result found')
                return render(request, 'portal/search.html', dict)
        else:
            return redirect('portal')
    rec_post = ChPost.objects.filter(id=post_id)
    context={
        'b':a,
        'rec_post1':rec_post,
        'all_post1':all_post,
        'chdetail1': chdetail,
        'state1': state,
        'us1': us,
        'u1': u,
        'upro1': upro,
        'cat1': cat,
    }
    return render(request, 'portal/cate_news.html', context)






