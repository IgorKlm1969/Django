from django.shortcuts import render


# Create your views here.
# def index(request):
#     context={
#         'user_list': [
#             {'first_name': 'Oleg',
#              'Last_name': 'Maslov',
#              'age': 31
#              }
#         ]
#     }
#     return render(request, 'mainapp/index.html', context)
#
#
# def products(request):
#     return render(request, 'mainapp/products.html')
#
#
# def contacts(request):
#     return render(request, 'mainapp/contacts.html')

def index(request):
        return render(request, 'mainapp/index.html')


def products(request):
    links_menu = [
        {'href': 'products_all', 'title': 'все'},
        {'href': 'products_home', 'title': 'дом'},
        {'href': 'products_office', 'title': 'офис'},
        {'href': 'products_modern', 'title': 'модерн'},
        {'href': 'products_classic', 'title': 'классика'},

    ]
    context = {
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')

# context = {
    #     'keys_list': [
    #         {
    #             'key1': 'value1',
    #             'key2': 'value2',
    #             'key3': 'value3',
    #         },
    #         {
    #             'key1': 'value10',
    #             'key2': 'value20',
    #             'key3': 'value30',
    #         }
    #     ]
    # }
