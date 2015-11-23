import os
import glob
from django.shortcuts import render
from .menus import menu
from quinnrose.home_page_info import home_page_info
from quinnrose.featurettes import featurettes

def home_page(request):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_path = os.path.join(root_dir, 'static', 'images') + '/carousel-*'
    carousel_images = [
        os.path.basename(p) for p in glob.glob(image_path)
    ]
    
    context = {
        'menu': menu,
        'carousel_images': carousel_images,
        'home_page_info': home_page_info,
        'featurettes': featurettes,
    }
    return render(request,'home.html', context)

# def new_list(request):
#     form = NewListForm(data=request.POST)
#     if form.is_valid():
#         list_ = form.save(owner=request.user)
#         return redirect(list_)
#     return render(request, 'home.html', {'form': form})
# 
# def view_list(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     form = ExistingListItemForm(for_list=list_)
# 
#     if request.method == 'POST':
#         form = ExistingListItemForm(for_list=list_, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(list_)
#     return render(request,'list.html', {'list': list_, 'form': form})
# 
# def my_lists(request, email):
#     owner = User.objects.get(email=email)
#     return render(request, 'my_lists.html', {'owner': owner})

if __name__ == '__main__':
    image_path = '../static/images/carousel-*'
    carousel_images = glob.glob(image_path)
    print(carousel_images)
    