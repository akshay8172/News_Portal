from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseForbidden
from django.shortcuts import render,HttpResponse,redirect
from.models import *
from datetime import datetime
from django.urls import reverse_lazy
from django.utils.dateparse import parse_date
from .fetch_news import read_news_online
from .cat_news import *
from django.core.paginator import Paginator
from django.urls import reverse

def home(request):
    return render(request, 'NewsPortal/news_portal.html')

def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        dob = request.POST['dob']
        photo = request.FILES['photo']
        email = request.POST['email']
        phone = request.POST['phone']
        place = request.POST['place']
        pin = request.POST['pin']
        post = request.POST['post']
        password = request.POST['password']

        fs = FileSystemStorage()
        file_path = fs.save(photo.name,photo)

        login_details = Login(username=email,password=password,type='user')
        login_details.save()

        profile = User(LOGIN=login_details,name=name,gender=gender,dob=dob,photo=file_path,email=email,phone=phone,place=place,pin=pin,post=post)
        profile.save()
        return HttpResponse('''<script>alert('Registration Success');window.location='/'</script>''')
    return render(request, 'USER/user_registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            ob = Login.objects.get(username=username, password=password)
            request.session['lid'] = ob.id

            if ob.type == "admin":
                news = read_news_online_kerala()
                if news:
                    for i in news:
                        if not News.objects.filter(title=i[1], source_url=i[3]).exists():
                            ne = News()
                            ne.title = i[1]
                            ne.image_url = i[0]
                            ne.summary = i[2]
                            ne.content = i[2]
                            ne.Category = 'kerala'
                            ne.published_at = datetime.now()
                            ne.source_url = i[3]
                            ne.save()
                news=read_news_online_sports()
                if news:
                    for i in news:
                        if not News.objects.filter(title=i[1], source_url=i[3]).exists():
                            ne = News()
                            ne.title = i[1]
                            ne.image_url = i[0]
                            ne.summary = i[2]
                            ne.content = i[2]
                            ne.Category = 'sports'
                            ne.published_at = datetime.now()
                            ne.source_url = i[3]
                            ne.save()
                news = read_news_online_health()
                if news:
                    for i in news:
                        if not News.objects.filter(title=i[1], source_url=i[3]).exists():
                            ne = News()
                            ne.title = i[1]
                            ne.image_url = i[0]
                            ne.summary = i[2]
                            ne.content = i[2]
                            ne.Category = 'health'
                            ne.published_at = datetime.now()
                            ne.source_url = i[3]
                            ne.save()
                news = read_news_online_entertainment()
                if news:
                    for i in news:
                        if not News.objects.filter(title=i[1], source_url=i[3]).exists():
                            ne = News()
                            ne.title = i[1]
                            ne.image_url = i[0]
                            ne.summary = i[2]
                            ne.content = i[2]
                            ne.Category = 'entertainment'
                            ne.published_at = datetime.now()
                            ne.source_url = i[3]
                            ne.save()
                news = read_news_online_world()
                if news:
                    for i in news:
                        if not News.objects.filter(title=i[1], source_url=i[3]).exists():
                            ne = News()
                            ne.title = i[1]
                            ne.image_url = i[0]
                            ne.summary = i[2]
                            ne.content = i[2]
                            ne.Category = 'world'
                            ne.published_at = datetime.now()
                            ne.source_url = i[3]
                            ne.save()

                return HttpResponse('''<script>alert('Welcome');window.location='/AdminHome'</script>''')
            elif ob.type == "user":
                try:
                    User.objects.get(LOGIN=ob)
                    return HttpResponse('''<script>alert('Welcome');window.location='/UserHome'</script>''')
                except User.DoesNotExist:
                    return HttpResponse('''<script>alert('User profile not found. Please contact support.');window.location='/'</script>''')
            else:
                return HttpResponse('''<script>alert('Invalid');window.location='/'</script>''')

        except Login.DoesNotExist:
            return HttpResponse('''<script>alert('Invalid username or password');window.location='/'</script>''')

        except Exception as e:
            print(e)
            return HttpResponse('''<script>alert('An error occurred. Please try again later.');window.location='/'</script>''')
    return render(request, 'NewsPortal/login.html')

def AdminHome(request):
    today_news = News.objects.all()
    return render(request, 'Admin/admin_home.html', {'news': today_news})


def admin_view_news(request):
    news_list = News.objects.all().order_by('-id')
    paginator = Paginator(news_list, 16)  # Show 16 news items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Admin/view_news.html', {'page_obj': page_obj})

def admin_view_more_news(request,id):
    news = News.objects.get(id=id)
    return render(request, 'Admin/view_more_news.html',{'news':news})

from django.utils import timezone

def admin_view_new_comments(request):
    today = timezone.now().date()
    comments = Comment.objects.filter(created_at__date=today).order_by('-id')
    return render(request, 'Admin/view_new_comments.html', {'comments': comments})

def delete_comment(request,id):
    com = Comment.objects.get(id=id)
    com.delete()
    return HttpResponse('''<script>alert('Comment Deleted');window.location='/'</script>''')


def admin_view_comments(request,id):
    news = News.objects.get(id=id)
    comments = news.comments.all()
    return render(request, 'Admin/view_comments.html', {'news': news, 'comments': comments})

def admin_view_sender(request,id):
    sender = User.objects.get(id=id)
    return render(request, 'Admin/view_sender.html',{'sender':sender})

def admin_delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect(reverse_lazy('admin_view_comments', kwargs={'id': comment.NEWS.id}))

def admin_view_users(request):
    users = User.objects.all()
    return render(request, 'Admin/view_users.html',{'users':users})







def UserHome(request):
    return render(request, 'User/user_home.html')

def user_view_past_news(request):
    news = News.objects.all()
    search_date = request.GET.get('search_date')  # Date filter
    search_title = request.GET.get('search_title')  # Title filter

    # Filter news by date if a date is provided
    if search_date:
        search_date = parse_date(search_date)  # Convert string to date
        if search_date:
            news = news.filter(published_at__date=search_date)

    # Filter news by title if a title is provided
    if search_title:
        news = news.filter(title__icontains=search_title)

    return render(request, 'User/view_past_news.html', {'news': news})


def user_view_news(request):
    today_news = News.objects.filter(published_at__date=datetime.today()).order_by('-id')
    paginator = Paginator(today_news, 16)  # Show 5 news items per page
    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the specific page of news items

    return render(request, 'User/view_news.html', {'page_obj': page_obj})

def user_view_more_news(request,id):
    news = News.objects.get(id=id)
    return render(request, 'User/view_more_news.html',{'news':news})

def user_view_comments(request,id):
    news = News.objects.get(id=id)
    comments = news.comments.all()
    return render(request, 'User/view_comments.html', {'news': news, 'comments': comments})

def post_comment(request, id):
    if request.method == 'POST':
        news = News.objects.get(id=id)

        comment_text = request.POST.get('comment_text')
        user_id = request.session['lid']
        user = User.objects.get(LOGIN_id=user_id)

        comment = Comment(USER=user, NEWS=news, comment_text=comment_text,created_at=datetime.now())
        comment.save()
        return redirect(reverse_lazy('user_view_comments', kwargs={'id': news.id}))
    return redirect('/user_view_comments', id=id)


def edit_comment(request, id):
    comment = Comment.objects.get(id=id)
    if comment.USER.LOGIN.id != request.session['lid']:
        return HttpResponseForbidden("You are not allowed to edit this comment.")
    if request.method == 'POST':
        new_comment_text = request.POST.get('comment_text')
        comment.comment_text = new_comment_text
        comment.updated_at = datetime.now()
        comment.save()
        return redirect(reverse('user_view_comments', args=[comment.NEWS.id]))

def ManageProfile(request):
    profile = User.objects.get(LOGIN_id=request.session['lid'])
    return render(request, 'User/view_profile.html',{'profile':profile})

def edit_profile(request):
    profile = User.objects.get(LOGIN_id=request.session['lid'])
    if request.method == 'POST':
        profile.name = request.POST['name']
        profile.gender = request.POST['gender']
        profile.dob = request.POST['dob']
        profile.email = request.POST['email']
        profile.phone = request.POST['phone']
        profile.place = request.POST['place']
        profile.pin = request.POST['pin']
        profile.post = request.POST['post']

        if 'photo' in request.FILES:
            profile.photo = request.FILES['photo']
            profile.save()
        profile.save()
        return HttpResponse('''<script>alert('Updated');window.location='/ManageProfile'</script>''')
    return render(request, 'User/update_profile.html',{'profile':profile})

def add_notificaation(request):
    if 'submit' in request.POST:

        noification=request.POST['NOTIFICATION']
        a=Notification()
        a.notification=noification
        a.date=datetime.now().today().date()
        a.save()
        return HttpResponse('''<script>alert('Added');window.location='/add_notificaation'</script>''')
    return render(request,'admin/add notification.html')


# views.py
from django.shortcuts import render
from .models import Notification

def notification_list(request):
    notifications = Notification.objects.order_by('-date')
    return render(request, 'Admin/notification_list.html', {'notifications': notifications})

def delete_notification(request,id):
    a=Notification.objects.get(id=id)
    a.delete()
    return HttpResponse('''<script>alert('Deleted');window.location='/notifications'</script>''')


def user_notification_list(request):
    notifications = Notification.objects.order_by('-date')  # Order by latest date
    return render(request, 'User/notification_list.html', {'notifications': notifications})


def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        ll = Login.objects.get(id=request.session['lid'])
        if current_password == ll.password:
            if new_password == confirm_password:
                ll.password = confirm_password
                ll.save()
                return HttpResponse(
                    '''<script>alert('current password changed into new password');window.location='/ManageProfile'</script>''')

            else:
                return HttpResponse(
                    '''<script>alert('new password not equal to confirm password');window.location='/change_password'</script>''')
        else:
            return HttpResponse(
                '''<script>alert('current password wrong');window.location='/change_password'</script>''')
    return render(request, 'User/change_password.html')

def search_news_category(request):
    cat = request.POST['cate']
    page_obj = News.objects.filter(Category__contains=cat)
    return render(request,'User/view_news.html',{'page_obj':page_obj})