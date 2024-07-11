
"""
Alura: ▼
from django.http import JsonResponse
from django.views import View

class MinhaAPI(View):
    def get(self, request):
        return JsonResponse({'message': 'Olá mundo!'})
"""

# import django
# print(django.get_version())
# 5.0.7

"""
Terminal: ▼
uvicorn main:app --reload
"""

"""
Testes Navegador: ▼
127.0.0.1:8000/api/hello
"""