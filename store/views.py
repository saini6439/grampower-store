from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.defaultfilters import length

from .models import Store,PostImage, StoreOpening

# view for add store details
@login_required(login_url='login')
def create_store_view(request):
    template_name='store/create_store.html'
    if request.method == 'POST':
        name = request.POST.get('name')
        length = request.POST.get('length')
        cover = request.FILES.get('cover')
        about = request.POST.get('about')
        products = request.POST.get('products')
        lang = request.POST.get('long')
        lot = request.POST.get('lat')
        sunday_from_hour = request.POST.get('sundayfrom_hour')
        monday_from_hour = request.POST.get('mondayfrom_hour')
        tuesday_from_hour = request.POST.get('tuesdayfrom_hour')
        wednesday_from_hour = request.POST.get('wednesdayfrom_hour')
        thrusday_from_hour = request.POST.get('thrusdayfrom_hour')
        friday_from_hour = request.POST.get('fridayfrom_hour')
        saturday_from_hour = request.POST.get('saturdayfrom_hour')
        sunday_to_hour = request.POST.get('sundayto_hour')
        monday_to_hour = request.POST.get('mondayto_hour')
        tuesday_to_hour = request.POST.get('tuesdayto_hour')
        wednesday_to_hour = request.POST.get('wednesdayto_hour')
        thrusday_to_hour = request.POST.get('thrusdayto_hour')
        friday_to_hour = request.POST.get('fridayto_hour')
        saturday_to_hour = request.POST.get('saturdayto_hour')
        store = Store.objects.create(
            name=name,
            about=about,
            cover=cover,
            products = products,
            lang = lang,
            lot = lot

        )

        for file_num in range(0, int(length)):
            PostImage.objects.create(
                store=store,
                images=request.FILES.get(f'images{file_num}')
            )
        StoreOpening.objects.create(
            store=store,
            sunday_from_hour=sunday_from_hour,
            monday_from_hour = monday_from_hour,
            tuesday_from_hour = tuesday_from_hour,
            wednesday_from_hour = wednesday_from_hour,
            thrusday_from_hour = thrusday_from_hour,
            friday_from_hour = friday_from_hour,
            saturday_from_hour = saturday_from_hour,
            sunday_to_hour = sunday_to_hour,
            monday_to_hour = monday_to_hour,
            tuesday_to_hour = tuesday_to_hour,
            wednesday_to_hour = wednesday_to_hour,
            thrusday_to_hour = thrusday_to_hour,
            friday_to_hour = friday_to_hour,
            saturday_to_hour = saturday_to_hour
        )

    return render(request, template_name)

# view details of a store
@login_required(login_url='login')
def detail_store_view(request, id):
    template_name = 'store/view_store.html'
    if id is not None:
        opening_hours =  Store.objects.get(id=id).storeopening_set.all()
        photos = Store.objects.get(id=id).postimage_set.all()
        store_details = Store.objects.get(id=id)
        context = {
            'store_details': store_details,
            'opening_hours': opening_hours[0],
            'photos':photos,
        }
    return render(request,template_name ,context)

# view for getting all stores
@login_required(login_url='login')
def all_store_view(request):
    template_name = 'store/all_store.html'
    queryset = Store.objects.all()

    context = {
        'object_list': queryset
    }
    print(context)
    return render(request,template_name,context)

# view for delete a store
# view for delete a store
@login_required(login_url='login')
def deleteStore(request, id=None):
    template_name = 'store/delete_store.html'
    store = Store.objects.get(id=id)
    if request.method == "POST":
        store.delete()
        return redirect('/')
    context = {'item':store}
    return render(request, template_name, context)