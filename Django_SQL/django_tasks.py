# Решите задачи с помощью Django ORM и SQL:
from django.db.models import Count, Sum
from models import Purchase

# Задание 1
# 1) Получить общую стоимость покупок для каждого из магазинов

purchase_info = Purchase.objects.all().values("store__name").annotate(sum_p=Sum('price'))
for store in purchase_info:
    print(f"{store['store__name']}: {store['sum_p']}")

# Задание 2
# 2) Вывести перечень всех покупок. Каждая строка должна содержать следующие данные:
#     название магазина
#     название товара
#     стоимость

purchases = Purchase.objects.all().values("store__name", "name", "price")

for i in purchases:
    print(f"Магазин: {i['store__name']}"
          f"\nНазвание: {i['name']}"
          f"\nЦена: {i['price']}\n")

# Задание 3
# 3) Выбрать покупки, цена которых больше или равна 100 руб., сгруппировать по магазинам
#     и посчитать количество таких покупок в каждом магазине.
price_100 = Purchase.objects.filter(price__gte=100).values("store__name").annotate(count=Count("id"))
for i in price_100:
    print(f"{i['store__name']}: {i['count']}")
