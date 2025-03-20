## Comandos

Verficar versão do python instalada:
````
phyton --version
````

Verficar versão do Django:
````
phyton -m django --version
````

Instalar Django:
````
phyton -m pip intall Django
````

Iniciar um novo projeto Django chamado mysite:
````
django-admin startproject mysite
````

Executar meu projeto no servidor de desenvolvimento em localhost:8000:
````
python manage.py runserver
````

Criar um Superusuario (Admin) - Django Admin:
````
python manage.py createsuperuser
````


Iniciar uma nova app chamada polls:
````
python manage.py startapp polls
````

Iniciar a Shell do Python:
````
python manage.py shell
````

Fechar o Shell do Python:
````
exit()
````

Para Atualizar os novos modelos adicionados ou alterado na classe:
````
python manage.py makemigrations
````

Para Atualizar os novos modelos adicionados ou alterado na classe especifico em apenas uma App "core":
````
python manage.py makemigrations core
````

Para Aplicar os novos modelos adicionados ou alterado na base de dados:
````
python manage.py migrate
````

Para Usar o modelo de dados no Shell, é Preciso Importar o Modelo de Dados "Usuario":
````
from core.models import Usuario
````

Declarar variavel para Buscar todos os registros da base de dados "Users":
````
users = Usuario.objects.all()
````

Declarar ou adicionar o valor da variavel "user1" "cidade":
````
user1.cidade = Lisboa
````

Localizar ou buscar apenas o Primeiro dado da tabela "User":
````
user = users.first()
````
````
user = users.objects.get(id=1)
````
````
user = Usuario.objects.first()
````


Localiozar ou buscar apenas o Ultimo dado da tabela "User
_last":
````
user_last = users.last()
````

Para se verificar a quantidade de "Usuarios" na Tabela:
````
print(users.count())
````

Para Saber a posição ou Id de um "Usuario", Lembra-se de informar a variavel "User":
````
print(user.id)
````

Mostrar ou imprimir valor da variavel, buscar valor "user":
````
print(user)
````

Para salvar as informações atribuidas em Variaveis antes de finalizar o Shell "user":
````
user.save()
````

Para deletar, apagar dados ou usuario finalizar o Shell "user":
````
user.delete()
````

Para criar um novo usuario ou id na tabela "user2":
````
user2 = Usuario.objects.create(nome = "novo usuario")
````

Para criar um novo usuario ou id na tabela "user_filter_":
````
user_filter = Usuario.objects.filter(nome__contains ="texto a procurar")
````

Para Criar novos modelos:
````
ir ate models.py e Incluir manualmente e definir suas class e variaveis, 
Ex: class Escala(models.Model):
`````

Para registrar um modelo - Django Admin (arquivo admin.py):
````
ir ate admin.py e incluir o modelo Ex: "Evento":

from django.contrib import admin
from .models import Evento

admin.site.register(Evento)
`````

Para remover e/ou modificar o User pedrão do Django Admin (arquivo admin.py) Ex: "Usuario":
````
ir ate admin.py e incluir :

admin.site.unregister(User)
admin.site.unregister(Usuario)
`````


## Dicionário de conceitos

### Full Stack Web Development
Desenvolvimento de sites e aplicações para a web, envolvendo front-end, back-end e banco de dados.

### ORM (Object-Relational Mapping)
Uma técnica que permite interagir com bancos de dados usando código em vez de SQL puro.

### SQL Injection XSS (Cross-Site Scripting)
Injeção de scripts maliciosos em páginas da web para roubar dados ou manipular usuários.

### Framework
Um conjunto de ferramentas e bibliotecas que facilita o desenvolvimento, fornecendo estrutura e funcionalidades prontas.
Acelera o desenvolvimento, padroniza código, melhora a manutenção e oferece segurança integrada.

### ComandoS Git