from rest_framework import generics
from .serializers import *
import pandas as pd
from django.http import JsonResponse


class StudentCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


def export_excel(request):
    stu = Student.objects.all()
    data = []
    for s in stu:
        data.append({
            'id': s.id,
            'teacher_name': s.teacher_name,
            'name': s.name,
            'email': s.email,
            'age': s.age,
            'roll': s.roll,
            'address': s.address
        })
    pd.DataFrame(data).to_excel('myexcel.xlsx', index=False)
    excel = pd.read_excel('myexcel.xlsx', index_col=0)
    print(excel)
    return JsonResponse({'status': 200})
