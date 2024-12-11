# 1
from collections import namedtuple
#
# Talaba = namedtuple('Talaba', ['name', 'age', 'major'])
# talabalar = [
#     Talaba("Ali", 20, "Matematika"),
#     Talaba("Sardor", 21, "Biologiya"),
#     Talaba("Gulnoza", 19, "Fyizika")
# ]
#
# for talaba in talabalar:
#     print(talaba)

# ------------------------
# 2
# Mahsulot = namedtuple('Mahsulot', ['product_name', 'price', 'quantity'])
# mahsulotlar = [
#     Mahsulot("Non", 1500, 10),
#     Mahsulot("Suv", 500, 20),
#     Mahsulot("Shokolad", 2000, 5)
# ]
#
# for mahsulot in mahsulotlar:
#     print(f"Mahsulot: {mahsulot.product_name}, Narx: {mahsulot.price}, Miqdor: {mahsulot.quantity}")

# ---------------------------------------
# 3
# Shahar = namedtuple('Shahar', ['city_name', 'country', 'population'])
# shaharlar = [
#     Shahar("Toshkent", "O'zbekiston", 2500000),
#     Shahar("London", "Angliya", 8900000),
#     Shahar("Tokio", "Yaponiya", 14000000)
# ]
#
# eng_katta_shahar = max(shaharlar, key=lambda x: x.population)
# print(f"Eng katta shahar: {eng_katta_shahar.city_name}, Aholisi: {eng_katta_shahar.population}")

# -------------------------
# 4
# Avtomobil = namedtuple('Avtomobil', ['make', 'model', 'year'])
# avtomobillar = [
#     Avtomobil("Toyota", "Camry", 2020),
#     Avtomobil("Honda", "Civic", 2022),
#     Avtomobil("Ford", "Mustang", 2021)
# ]
#
# eng_yangi_avtomobil = max(avtomobillar, key=lambda x: x.year)
# print(f"Eng yangi avtomobil: {eng_yangi_avtomobil.make} {eng_yangi_avtomobil.model}, Yili: {eng_yangi_avtomobil.year}")

# ------------------------------
# 5
# def outer_function():
#     def inner_function():
#         return "Hello world!"
#     return inner_function
# closure = outer_function()
# print(closure())

# ------------------------------------
# 6
# def salomlashish(isim):
#     def salom():
#         return f"Salom, {isim}!"
#     return salom
# salom_function = salomlashish("Otabek")
# print(salom_function())

# ------------------------------------------
# 7
# def qoshuvchi(x):
#     def add(y):
#         return x + y
#     return add
# add_5 = qoshuvchi(5)
# print(add_5(10))

# -------------------------
# 8
# def counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     return increment
#
# count_function = counter()
# print(count_function())
# print(count_function())

# ------------------------------------
# 9
# def kvadrat():
#     def calc_sq(x):
#         return x ** 2
#     return calc_sq
# kvadrat_function = kvadrat()
# print(kvadrat_function(4))

# ---------------------
# 10
# def isimlar_royxati():
#     names = []
#     def add_name(name):
#         names.append(name)
#         return names
#     return add_name
#
# names_function = isimlar_royxati()
# print(names_function("Ali"))
# print(names_function("Sardor"))

# -----------------------------
# 11
# def chegirma(foiz):
#     def apply_discount(price):
#         return price * (1 - foiz / 100)
#     return apply_discount
#
# discount_10 = chegirma(10)
# print(discount_10(10000))

# ------------------------------
# 12
# def mahsulot_kopaytuvchi():
#     count = 0
#     def multiply():
#         nonlocal count
#         count += 1
#         return count
#     return multiply
#
# product_multiplier = mahsulot_kopaytuvchi()
# print(product_multiplier())
# print(product_multiplier())

# --------------------------------
# 13
# def string_qosh():
#     s = ""
#     def add_string(new_string):
#         nonlocal s
#         s += new_string
#         return s
#     return add_string
#
# append_function = string_qosh()
# print(append_function("Salom, "))
# print(append_function("dunyo!"))

# -----------------------------
# 14
# def toq_sonlarni_qaytar():
#     def filter_odds(numbers):
#         return [num for num in numbers if num % 2 != 0]
#     return filter_odds
#
# filter_function = toq_sonlarni_qaytar()
# print(filter_function([1, 2, 3, 4, 5]))

# -------------------------------------
# 15
# def exponent_func():
#     def calculate_power(base, exp):
#         return base ** exp
#     return calculate_power
#
# power_function = exponent_func()
# print(power_function(2, 3))

# -----------------------------------
# 16
# def string_reverse():
#     def reverse(s):
#         return s[::-1]
#     return reverse
#
# reverse_function = string_reverse()
# print(reverse_function("Hello"))

# ------------------------------
# 17
# def savat():
#     items = []
#     total = 0
#
#     def add_product(product_name, price):
#         nonlocal total
#         items.append(product_name)
#         total += price
#         return total
#
#     return add_product
#
#
# cart = savat()
# print(cart("Non", 1500))
# print(cart("Suv", 500))

# -----------------------------
# 18
# def narxlar_qoshish():
#     prices = []
#
#     def add_price(price):
#         prices.append(price)
#         return prices
#     return add_price
#
# add_price_function = narxlar_qoshish()
# print(add_price_function(1500))
# print(add_price_function(2000))
