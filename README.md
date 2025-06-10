# Projeto E-commerce

Um projeto extremamente simples de e-commerce feito com Django 5.1.3 e Python 3.13.0

## Este projeto NÂO inclui
Abaixo uma lista de recursos que não adicionei ainda e que você pode me ajudar a adicionar.

- Combinações de variações de produto (tem apenas uma variação)
- Cupons de desconto no carrinho de compras
- Cálculo de frete
- Métodos de pagamento (MercadoPago, PayPal, PagSeguro, enfim...)

## Tutorial para iniciantes
  Abaixo uma lista de comandos para clonar e configurar este projeto na sua máquina local:

-Instalar git (Windows, Linux e Mac) e depois:
<pre> git clone https://github.com/lordrodrigoo/E-COMMERCE.git </pre>

-Para Windows:
<pre> cd django-simple-ecommerce
python -m venv venv
venv\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel --user
python -m pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate </pre>

-Para Linux:
<pre> cd django-simple-ecommerce
python3.13.0 -m venv venv
. venv/bin/activate
pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate </pre>

-Para Mac:
<pre> cd django-simple-ecommerce
python -m venv venv
. venv/bin/activate
pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate </pre>

#### Pronto!
