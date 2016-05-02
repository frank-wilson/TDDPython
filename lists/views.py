from django.shortcuts import redirect, render
from lists.models import Item

# TODO: Adjust model so that items are associated with different lists
# TODO: Add unique URLs for each list
# TODO: Add a URL for creating a new list via POST
# TODO: Add URLs for adding a new item to an existing list via POST
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

