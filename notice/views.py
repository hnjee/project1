from django.shortcuts import render, redirect
from .models import Notice
from django.core.paginator import Paginator
from .customPager import CustomPager
# Create your views here.

def list(request, page=1, kind="title", search=""):
    # querySet
    # notice = Notice.objects.all()#select * from notice_notice
    
    # Slicing-----------------------------------
    # start = (page-1)*2
    # last = page*2
    # notice = Notice.objects.order_by("-num")[start:last] # select * from notice order by num desc

    # Paginator-----------------------------------
    # notice = Notice.objects.order_by("-num")
    # # Paginator(Qureyset,개수)
    # notice = Paginator(notice, 2)
    # # 실제 조회 
    # notice = notice.get_page(page)

    # CustomPager-----------------------------------
    customPager = CustomPager(page, kind, search)
    print("pre : ",customPager.pre)
    notice = Notice.objects.order_by("-num")
    notice = Paginator(notice, 2)
    customPager.makePage(notice.num_pages)
    notice = notice.get_page(customPager.page)
    context = {"board":"NoticeList", "list":notice,"pager":customPager}    

    return render(request, 'notice/list.html', context)

def write(request):
    if request.method=='POST':
        notice = Notice(title=request.POST['title'], writer=request.POST['writer'], contents=request.POST['contents'])
        notice.save()
        return redirect('/notice/noticeList')
    else :
        print("Write Form")
        return render(request, 'notice/write.html', {"board":"NoticeWrite"})    

def select(request, num=1):
    notice = Notice.objects.get(pk=num)
    context = {"vo":notice, "board":"NoticeSelect"}
    return render(request, 'notice/select.html', context)

def delete(request, num):
    notice = Notice(num=num)
    notice.delete()
    return redirect('notice/noticeList')

def update(request, num):
    if request.method=='POST':
        notice = Notice.objects.get(pk=num)
        notice.title = request.POST['title']
        notice.contents = request.POST['contents']
        notice.save()
        return redirect('/notice/noticeList')
    else:
        notice = Notice.objects.get(pk=num)
        context = {'vo':notice, 'board':'NoticeUpdate'}
        return render(request, 'notice/write.html', context)
