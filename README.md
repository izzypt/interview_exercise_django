# Índice

Índice das tarefas com o processo de resolução passo a passo.

- [Task 1](#Task1) - _Start a new Django project using a sqlite database._

- [Task 2](#Task2) - _Create a app and add a Finding model to store the objects described_

- [Task 3](#Task3) - _Create a Django command that retrieves all the findings for a given id and stores them in the database._

- [Task 3](#Task1) - _Create a Django view to list and filter findings._

<a id="Task1"></a>

# Task 1 

1 - Criar uma nova directoria para o projecto.
```
>>> mkdir probely_exercise
```
2 - Criar um ambiente virtual para o projecto de forma a manter as dependências isoladas.
```
>>> python -m venv venv
```
3 - Activar ambiente virtual
```
>>> .\venv\Scripts\activate
```
4 - Instalar Django e Django Rest Framework
```
>>> pip install Django
>>> pip install djangorestframework
```
5 - Registar as dependencias instaladas até ao momento num ficheiro chamado "requirements.txt".

```
>>> pip freeze > requirements.txt
```

6 - Iniciar o projecto Django
```
>>> django-admin startproject backend
````
7 - Adicionar 'rest_framework' às ```INSTALLED_APPS``` no ficheiro ```settings.py```

![image](https://user-images.githubusercontent.com/73948790/217391622-25aaf9a8-76b8-4e0d-adf5-03025c592e6d.png)

8 - Django vem por padrão com uma BD SQlite nas settings , vamos criar as migrações necessárias para criar as nossa tabelas base
```
>>> python manage.py makemigrations
>>> python manage.py migrate
```

<a id="Task2"></a>

# Task 2

1 - Vamos criar uma nova app dentro do nosso projecto chamada "findings"
```
python .\manage.py startapp findings
```

2 - Adicionamos a nova app às ```INSTALLED_APPS```

![image](https://user-images.githubusercontent.com/73948790/217395540-42e27460-9b14-4a26-9776-b6d0ecd754b8.png)

3 - Dentro da nossa nova app no ficheiro ```models.py``` vamos criar um novo modelo chamado ```FindingsModel```.

   Findings são problemas de segurança encontrados durante o scan da app/api. 

   Cada finding vem com os dados recolhidos durante o scan, uma descrição da vulnerabilidade e uma sugestão de como corrigi-la. 

   O nosso modelo deve conter :

       ● id -> The finding id
  
       ● target_id -> String (unique Base58 value)
  
       ● definition_id -> String (unique Base58 value)
  
       ● scans -> Array of strings (unique Base58 value)
  
       ● url -> String
  
       ● path -> String
  
       ● method -> string
   

O nosso diagrama de UML para o presente modelo, fica assim :

![image](https://user-images.githubusercontent.com/73948790/217618686-8a88d253-4701-4b3d-9640-a1e58bc00dd4.png)

Em alternativa, se o campo "scans" não fosse obrigatório no nosso ```findingsModel```, poderíamos ter criado algo como :

![image](https://user-images.githubusercontent.com/73948790/217619088-93bd1b6d-aa0d-476f-93a3-223568b67ee0.png)

O nosso modelo fica assim:
```
       from django.db import models

       # Create your models here.
       class Scan(models.Model):
           id = models.AutoField(primary_key=True)
           value = models.CharField(max_length=100, unique=True)

           def __str__(self):
               return self.value

       class FindingsModel(models.Model):
           id = models.AutoField(primary_key=True)
           target_id = models.CharField(max_length=100, unique=True)
           definition_id = models.CharField(max_length=100, unique=True)
           scans = models.ManyToManyField(Scan)
           url = models.CharField(max_length=200)
           path = models.CharField(max_length=200)
           method = models.CharField(max_length=10)

           def __str__(self):
               return self.target_id
```       
4 - Fazer as migrações e migrar os nossos novos modelos.

```
>>> python manage.py makemigrations
>>> python manage.py migrate
```

<a id="Task3"></a>

# Task 3

1 - Vamos criar uma nova directoria na nossa app ```findings``` : management/commands.
