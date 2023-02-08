# Index

Índice das tarefas com o processo de resolução passo a passo.

- [Task 1](#Task1) _Start a new Django project using a sqlite database._

- [Task 2](#Task2) _Create a app and add a Finding model to store the objects described_

- [Task 3](#Task1) _Create a Django command that retrieves all the findings for a given id and stores them in the database._

- [Task 3](#Task1) _Create a Django view to list and filter findings._

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

1 - Vamos criar uma nova app dentro do nosso projecto chamada "Findings_app"
```
python .\manage.py startapp findings
```

2 - Adicionamos a nova app às ```INSTALLED_APPS```

![image](https://user-images.githubusercontent.com/73948790/217395540-42e27460-9b14-4a26-9776-b6d0ecd754b8.png)

3 - Dentro da nossa nova app no ficheiro ```models.py``` vamos criar um novo modelo chamado ```FindingsModel```, que deve conter , os seguintes campos :

       ● id -> The finding id
  
       ● target_id -> String (unique Base58 value)
  
       ● definition_id -> String (unique Base58 value)
  
       ● scans -> Array of strings (unique Base58 value)
  
       ● url -> String
  
       ● path -> String
  
       ● method -> string
   
Findings são problemas de segurança encontrados durante o scan da app/api. 

Cada finding vem com os dados recolhidos durante o scan, uma descrição da vulnerabilidade e uma sugestão de como corrigi-la.

O nosso diagrama de UML para o presente modelo, fica assim :

![image](https://user-images.githubusercontent.com/73948790/217601394-8c83a4d6-35aa-4d66-8f91-fb9b66db7ffd.png)

