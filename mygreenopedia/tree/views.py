from django.shortcuts import render
from .models import Data
# import csv
# import os
# Create your views here.
def remove(string): 
    return string.replace(" ", "") 

def tree_list(request):
    trees = Data.objects.all()
    l = []
    k = []
    l1 = []
    l2 = []
    i=0
    zipped_data = []
    for tree in trees :
        
        image = str(tree.mostcommonname)+'.jpg'
        l1.append(tree)
        l2.append("/images/"+str(remove(image)))
        i=i+1
        if i%3 == 0 and i!=0:
            zipped_data.append(zip(l1,l2))
            l.append(l1)
            k.append(l2)
            l1 = []
            l2 = []
    # zipped_data = zip(l1,l2)
    # print(zipped_data)
    print(l)
    print(k)
    for tree in zipped_data:
        for a,b in tree:
            print(a , b)
        break
    return render(request, 'tree_list.html' , {"trees":zipped_data}) 


def tree_detail(request,t_id):
    tree = Data.objects.filter(id = t_id).first()
    
    return render (request,"tree_detail.html",{"tree":tree})




# with open('employee_birthday.txt') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             line_count += 1
#     print(f'Processed {line_count} lines.')