from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item,List

# Create your views here.

# home_page = None
# def home_page(request):
#     return HttpResponse('<html><title>To-Do list</title></html>')


# def home_page(request):
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # else:
    #     return render(request,'home.html')


def home_page(request):
        return render(request,'home.html')


def add_item(request,list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect('/lists/%d/' % (list_.id,))


def view_list(request,list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.all()
    return render(request, 'list.html', {'items':items,'list':list_})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_)
    return redirect('/lists/%d/' % (list_.id))

