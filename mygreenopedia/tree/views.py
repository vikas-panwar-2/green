from django.shortcuts import render
from .models import Data
# import csv
# import os
# Create your views here.

def tree_list(request):
    trees = Data.objects.all()
    return render(request, 'tree_list.html' , {"trees":trees})


def tree_detail(request,t_id):
    tree = Data.objects.filter(id = t_id).first()
    print(type(tree.link1))
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