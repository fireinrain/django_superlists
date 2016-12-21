from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item

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
    if request.method == 'POST':

        item = Item()
        item.text = request.POST.get('item_text','')
        item.save()
        return redirect('/lists/the-only-list-in-the-world/')
    else:
        items = Item.objects.all()
        return render(request,'home.html',{'items':items})

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})