from django.urls import path
from .views import ProductView, GetProductByIdView, AddImageArrayToProduct

urlpatterns = [
    path('', ProductView.as_view()),
    # get by id
    path('<int:pk>/', GetProductByIdView.as_view()),
    # add images to product
    path('<int:pk>/images/', AddImageArrayToProduct.as_view())
]


'''

p1 = Pessoa()
p2 = Pessoa()
#p1 e p2 sao instancias da classe Pessoa

p1.nome -> nome da instancia p1


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

        
soma (x,y):
    return x + y  

      
'''
