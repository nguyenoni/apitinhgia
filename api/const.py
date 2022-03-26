# For a Product
from .models import Discount, Amount

def to_json_detail(objs):
    arr_result = []
    for obj in objs:
        arr_result.append(obj.to_json_fomat())

    return arr_result
# For all product
def to_json(objs):
    arr_result = []
    for obj in objs:
        arr_result.append(obj.to_dict())
    return arr_result


#for index load all data
def convert_to_obj_json(objs):
    arr_result = []
    for item in objs:
        if(Discount.objects.filter(product = item).count()>0):
            discount = Discount.objects.filter(product = item)

            obj = {
                'product': item.to_json_fomat(),
                'discount': discount[0].to_json_fomat()
            }

            arr_result.append(obj)
           
    return arr_result
def convert_all_amount_to_json(amounts):
    arr_result = []
    for item in amounts:
        arr_result.append(item.to_dict())
    return arr_result
   
def convert_amount_to_json(objs):
    arr_result = []
    ls_amouns = Amount.objects.filter(product = objs)
    obj = {
        'price_with_amount': convert_all_amount_to_json(ls_amouns)
    }
    arr_result.append(obj)
    return arr_result

def generate_discount():
    return [
        {'discount': 32000000000},
        {'discount': 16000000000},
        {'discount': 8000000000},
        {'discount': 4000000000},
        { 'discount': 2000000000},
        { 'discount': 1000000000},
        { 'discount': 500000000},
        { 'discount': 300000000},
        { 'discount': 150000000},
        { 'discount': 60000000},
        { 'discount': 30000000},
        { 'discount': 10000000}
    ]

def get_products(obj_products):
    arr_result = []
    for item in obj_products:
        discount = Discount.objects.filter(product = item)[0]

        amount = Amount.objects.filter(product = item)
    #   obj product
        obj = {
            'id' : item.id,
            'name': item.name,
            'amount': convert_all_amount_to_json(amount),
            'discount': discount.to_json_fomat()
        }
        arr_result.append(obj)
    return arr_result

def check_range_price(num, arr):
    result = False
    for index in range(len(arr)):
        next = index +1
        if (num < min(arr)):
            result = min(arr)
        if(next <= len(arr)):
            if(arr[index]<=num and num<arr[next]):
                result = arr[index]
                break
            
            elif(num== arr[index]):
                result = arr[index]
                break
            elif(num >= max(arr)):
                result = max(arr)
                break
    return result


# def fin_product(num, obj_amount):
#     result = False
#    arr = []
#    for item in obj_amount:
#        arr.append(item.name)
#    check = check_range_price(num, arr)
#    for item in obj_amount:
#        if(check == int(item.name)):
#         #    result = 


