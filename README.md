# shop_price_list

Этот проект был создан по заказу и представляет собой интернет-магазин без страницы "Подробнее".
## Функции и системмы

- Система динамического меню
- Система авторизации/регистрации
- Система оптовых цен
- Динамический блок "Контакты"
- Корзина
- Заказы
- Мини-блог (новости)
- Фильтр цен
- Сортировка

## фреймворки и библиотеки 
- Bootstrap 5
- Django
- django-crispy-forms
- django-mptt
- django-mptt-admin

## Как включить систему VIP?
Необходимо добавить группу VIP, стоимость товара можно указать при добовление товара.

## Запуск 
0. pip install -r requirements.txt
1. python manage.py createsuperuser - Создаст администратора с нужными параметрами
2. python manage.py runserver - запустить локальный сервер средствами Django
