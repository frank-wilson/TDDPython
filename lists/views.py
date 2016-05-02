from django.shortcuts import redirect, render
from lists.models import Item, List

# TODO: Adjust model so that items are associated with different lists
# TODO: Add unique URLs for each list
# TODO: Add URLs for adding a new item to an existing list via POST
def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'items': items})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))
