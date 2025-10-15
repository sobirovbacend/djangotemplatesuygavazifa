# # print("salom")
# class Myclass:
#     def __init__(self,name,age,phone):
#         self.name = name
#         self.age = age
#         self.phone=phone
#
#
#     def func(self):
#         return print(f"{self.name},{self.phone}{self.age}")
#
# ob = Myclass("Salohiddin","18","998900070101")
# ob.func()

# =====================================================================================================================

# bu quyidagi kod decorator mavzusiga tegishli qoidasi
# decorator-bu funksiyaning logikasiga tegmasdan undan oldin undan keyin nimadir bajarish shu decorator deyiladi.
# def myfunc(func):
#     def ichkifunc():
#         print("salom funksiya ishlashni boshladi")
#         func()
#         print("salom ishlab boldi")
#
#     return ichkifunc
#
# @myfunc
# def run():
#     print("logikasiga tegmasdan undan oldin va undan keyin qoidani yozib ketyapmiz")
# run()

# =====================================================================================================================
# OOP MAVZUSI
# OOPNI ASOSIY 4TA TAMOYILI BOR BULLAR QUYIDA:
# 1-INHERTANCE
# 2-POLIMORFIZM
# 3-INKAPSULIYATSIYA
# 4-ABSTRAKSIYA
# ENDI BULAR NIMA?

# 1-INHERTANCE-BU VORISLIK MEROS OLISH 1TA CLASS BOSHQASIDAN  XUSUSIYAT VA METODLARNI MEROS QILIB OLADI
# MISOL

# Bu kod:
#
# Inheritance (meros olish) ni ko‘rsatadi
#
# Polymorphism (ko‘p shakllilik) ni ham amalda ko‘rsatadi
#
# Obyekt (cat) It klassidan yaratilgan
# polymorphism, ya’ni bir xil metod nomi, lekin turlicha ishlash.
# It esa Havvon klassining barcha xususiyatlarini olgan

# class Havvon:
#     def __init__(self,name,age):
#         self.name =  name
#         self.age = age
#
#
#     def ovozi(self):
#         print("hayvon ovoz chiqaryapti")
#
# # endi hayvon degan cllas bor biz voris olamiz shu classdan
#
#
# class It(Havvon):
#     def ovozi(self):
#         print("gaf gaf")
#
# cat = It("sharik","6")
# print(cat.name,cat.age)
# cat.ovozi()

# agar farzand klass oz konstruktoriga qoshimcha atribut
# qoshmoqchi bolsa ota classdagi kodni takror yozmasdan SUPER() YORDAMIDA CHAQIRILADI
# QUYIDAGI KODNI KO'RISHIMIZ MUMKIN

# =====================================================================================================================
#
# class Hayvon:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"ismi{self.name} yoshi{self.age}")
#
# class It(Hayvon):
#     def __init__(self,name,age,turi):
#         super().__init__(name,age)
#         self.turi = turi
#
#     def info(self):
#         print(f"ismi:{self.name} yoshi:{self.age} turi:{self.turi}")
#
#     def ovozi(self):
#         print("gaf gaf")
#
# # obyekt yaratamiz
# it = It("alabay","7","ovchi yirtqich it")
# it.info()
# it.ovozi()
#
# PYTHON BIR NECHTA MEROS OLISH USUL BOR BULAR QUYIDA
# 1-SINGLE
# 2-MULTILEVEL
# 3-MULTIPLE
# 4-Hierarchical
# 5-Hybrid
# ------------------------------------------------------
# 1. Single Inheritance (Oddiy meros olish)
# Bitta ota klassdan bitta farzand klass meros oladi.
# class Hayvon:
#     pass
#
# class It(Hayvon):
#     pass

# It — faqat Hayvondan meros oladi.

# 2. Multilevel Inheritance (Ko‘p bosqichli meros olish)
# Har bir klass o‘zidan oldingisidan meros oladi.
# class Hayvon:
#     pass
#
# class It(Hayvon):
#     pass
#
# class OvchiIt(It):
#     pass

# OvchiIt → Itdan, It esa → Hayvondan meros oladi.

# 3. Multiple Inheritance (Ko‘p ota meros olish)
#  Bitta klass bir nechta ota klassdan meros oladi.
# class Hayvon:
#     pass
#
# class Aql:
#     pass
#
# class It(Hayvon, Aql):
#     pass

# It ikkala klassning ham xususiyatlarini oladi.

# 4. Hierarchical Inheritance (Ierarxik meros olish)
#  Bitta ota klassdan bir nechta farzandlar meros oladi.
# class Hayvon:
#     pass
#
# class It(Hayvon):
#     pass
#
# class Mushuk(Hayvon):
#     pass
# It va Mushuk — bitta ota (Hayvon) dan meros olgan ikki farzand.

# 5.Hybrid Inheritance (Aralash meros olish)
# Yuqoridagi turlarning aralashmasi, masalan:
# class Hayvon:
#     pass
#
# class It(Hayvon):
#     pass
#
# class Mushuk(Hayvon):
#     pass
#
# class OvchiIt(It, Mushuk):
#     pass
#
# bu yerda OvchiIt ham multiple, ham hierarchical merosni birlashtirgan.#
# =====================================================================================================================
#   2- POLIMORFIZM
# Polymorphism (Ko‘p shakllilik) nima?
#
# Polymorphism — bu “bir xil nomdagi metod yoki funksiya turli klasslarda turlicha ishlashi” degani.
#
# Ya’ni, bir xil nom — turlicha xatti-harakat.
# class Hayvon:
#     def ovozi(self):
#         print("Hayvon ovoz chiqaryapti")
#
# class It(Hayvon):
#     def ovozi(self):
#         print("Gaf gaf")
#
# class Mushuk(Hayvon):
#     def ovozi(self):
#         print("Miyov miyov")
#
# # Polymorphism amalda:
# for hayvon in [It(), Mushuk(), Hayvon()]:
#     hayvon.ovozi()
# Har biri ovozi() metodini chaqirdi, lekin har bir klassda u o‘ziga xos tarzda ishladi.
# Shuning uchun bu — polimorfizm.
# ====================================================================================================================
#  3-INKAPSULIYATSIYA
# Qoida
# Encapsulation - bu ma’lumotlar va metodlarni bitta birlikda saqlash imkoniyati.
# # Ya’ni class yaratganimizda biz inkapsulatsiyadan foydalangan bo’lamiz.
# # Chunki bir class da biz ham attribut, ham metodlardan foydalanamiz:
#
# Ma’lumotlar bu - obyekt malumoti
# Metodlar- bu classning ichida yozilgan funksiya metod  bu metod shu obyektning malumoti bilan ishlaydi
# Ya’ni:
#
# Ma’lumotlar (data) — bu self.name, self.age kabi obyekt atributlari.
#
# Metodlar (methods) — bu shu atributlar bilan ishlovchi funksiyalar (def ichida).

# class Talaba:
#     def __init__(self, ism, yosh):
#         self.ism = ism       # ma'lumot (atribut)
#         self.yosh = yosh     # ma'lumot (atribut)
#
#     def info(self):          # metod
#         print(f"Ism: {self.ism}, Yosh: {self.yosh}")
#
# # Obyekt yaratamiz
# t1 = Talaba("Salohiddin", 18)
# t1.info()
# ism, yosh → ma’lumotlar (data)
#
# info() → metod (shu ma’lumotlar bilan ishlaydi)
# → barchasi bitta klass ichida, ya’ni inkapsulyatsiya amalga oshgan.

# # Data/information hiding - Obyektdagi data member(attribut) larni yashirish.
# # Bunga Access Modifierlar orqali erishamiz.
#
# # - **Public Member**: Classdan tashqarida ishlatsa bo’ladigan
# # - **Private Member**: Faqat class ichida ishlatsa bo’ladigan
# # - **Protected Member**: Classda va unda voris olgna sub-class larda ishlatsa bo’ladigan
#
# # Public Member
# class Worker:
#     # constructor
#     def __init__(self, name, salary):
#         # public data members
#         self.name = name
#         self.salary = salary
#
#     # public instance methods
#     def show(self):
#         # accessing public data member
#         print("Name: ", self.name, 'Salary:', self.salary)
# #
#
# # creating object of a class
# emp = Worker('ALI', 10000)
# print(emp.name)
#
#
# # accessing public data members
# # print("Name: ", emp.name, 'Salary:', emp.salary)
#
# # calling public method of the class
# # emp.show()
#
#
# # Private Member
# # Variable ni faqat class ichida ishlatilishi uchun uni e’lon qilayotganda
# # nomi oldidan double underscore qo’yamiz: __salary
#
# class Worker:
#     # constructor
#     def __init__(self, name, salary):
#         # public data member
#         self.name = name
#         # private member
#         self.__salary = salary
#
#     def get_selery(self):
#         return self.__salary
# #
# #
# # # creating object of a class
# emp = Worker('ALI', 10000)

#
#
# # Private memberdan tashqarida foydalanishning 2 usuli bor:
# #
# # 1) private memberga murojaat qiladigan maxsus public metod yaratish
# #
# # 2) name mangling dan foydalanish
#
# # public metod yaratish:
# class Worker:
#     # constructor
#     def __init__(self, name, salary):
#         # public data member
#         self.name = name
#         # private member
#         self.__salary = salary
#
#     # public instance methods
#     def show(self):
#         # private members are accessible from a class
#         print("Name: ", self.name, 'Salary:', self.__salary)
#
#
# # creating object of a class
# emp = Worker('ALI', 10000)
# print(emp)


# calling public method of the class
# emp.show()


# # Name mangling - bu usul orqali quyidagi sintaksisdan foydalanib public va protected
# # memberlarga to’g’ridan to’g’ri murojaat qila olamiz:
#
# # ObyektNomi._ClassNomi.__PrivateMemberNomi
# #
# class Worker:
#     # constructor
#     def __init__(self, name, salary):
#         # public data member
#         self.name = name
#         # private member
#         self.__salary = salary


# creating object of a class
# emp = Worker('ALI ', 10000)
# print(emp)

# print('Name:', emp.name)
# print('Name:', emp.__salary)
# direct access to private member using name mangling
# print('Salary ======== :', emp._Worker__salary)

#
# ### **Protected Member**
#
# # Variable ni class va undan voris olgan class lar ishlatilishi uchun uni
# # e’lon qilayotganda nomi oldidan underscore qo’yamiz: _salary
#
# # base class
# class Company:
#     def __init__(self):
#         # Protected member
#         self._project = "NLP"
#     def show(self):
#         pass


# com1 = Company()
# com1._project ="test"
# print(com1._project)
#
#
# # child class
# class Worker(Company):
#     def __init__(self, name):
#         self.name = name
#         self.__age = 25
#         Company.__init__(self)
#
#     def show(self):
#         print("Employee name :", self.name)
#         # Accessing protected member in child class
#         print("Working on project :", self._project)
#
#
# c = Worker("Jessa")
#
# c.show()
#
# # Direct access protected data member
# print('Project:', c._project)

# ====================================================================================================================
# ABSTRAKSIYA

# Abstraction (abstraktsiya) obyektga yo'naltirilgan dasturlashning (OOP)
# asosiy tamoyillaridan biri
# bo‘lib, murakkab tizimni soddalashtirish uchun muhim bo‘lgan
# xususiyat va funksiyalarni ajratib olishni ta'minlaydi. Abstraktsiya orqali
# foydalanuvchiga faqat kerakli ma'lumotlar taqdim etiladi, qolgan murakkabliklar yashiriladi.
#
# Python'da abstractionni amalga oshirish uchun Abstract
# Base Class (ABC) va @abstractmethod dekoratoridan foydalaniladi.


# Python'da abstraction qanday ishlaydi?
# Abstraktsiya Abstract Base Classlar (ABC) yordamida amalga oshiriladi.
# ABC — bu boshqa klasslar uchun asosiy interfeysni belgilaydigan klass.
# Abstract klass o‘zining aniqlanmagan metodlarini (abstract metodlar)
# voris klasslar tomonidan amalga oshirilishini talab qiladi.
#
# Abstract klasslar to‘g‘ridan-to‘g‘ri obyekt sifatida ishlatilmaydi.


# Abstract klassning asosiy xususiyatlari:
# Abstract klassni yaratish uchun abc modulidan foydalaniladi.
# Abstract klass ichidagi abstract metodlar voris klasslar tomonidan
# majburiy amalga oshirilishi kerak.
# Abstract klassning abstract bo‘lmagan metodlari ham bo‘lishi mumkin.


# from abc import ABC, abstractmethod


# Abstract Base Class
# class Transport(ABC):
#     @abstractmethod
#     def harakatlanish(self):
#         """Bu metod har bir transport vositasi uchun aniqlanishi kerak"""
#         pass
#
#     @abstractmethod
#     def yoqilgi_turi(self):
#         """Yoqilg‘i turini aniqlovchi abstract metod"""
#         pass


# Voris klasslar
# class Mashina(Transport):
#     pass
#
#
# class Samolyot(Transport):
#     def harakatlanish(self):
#         return "Samolyot havoda uchadi"
#
#     def yoqilgi_turi(self):
#         return "Reaktiv yonilg‘i"
#
#
# # Voris klasslardan foydalanish
# mashina = Mashina()
# samolyot = Samolyot()
# mashina.yoqilgi_turi()
# # print(mashina.harakatlanish())  # Mashina yo'lda yuradi
# # print(mashina.yoqilgi_turi())  # Benzin
#
# print(samolyot.harakatlanish())  # Samolyot havoda uchadi
# print(samolyot.yoqilgi_turi())  # Reaktiv yonilg‘i

# Abstract klassning asosiy xususiyatlari:

# Abstract klassni yaratish uchun abc modulidan foydalaniladi.

# Abstract klass ichidagi abstract metodlar voris
# klasslar tomonidan majburiy amalga oshirilishi kerak.

# Abstract klassning abstract bo‘lmagan metodlari ham bo‘lishi mumkin.

#### Abstract klass farqi

# Abstract klassda esa metodlar to‘liq aniqlanmagan bo‘ladi.
# Bunda metodning faqat nomi va qoidasi aniqlanadi, lekin qanday
# bajarilishi (mazmuni) aniqlanmaydi. Bu shuni anglatadiki, abstract
# klassdan obyekt yaratilmaydi, chunki uning ba'zi metodlari hali amalga oshirilmagan.
#
# Abstract klassning oddiy misoli:

# from abc import ABC, abstractmethod


# class Hayvon(ABC):  # Abstract klass
#     @abstractmethod
#     def ovoz_chiqar(self):
#         pass
#
#
# # ovoz_chiqar metodining qanday ishlashi aniq belgilanmagan (pass yozilgan).
# # Agar ushbu klassdan obyekt yaratmoqchi bo‘lsangiz, xato chiqadi:
#
# class It(Hayvon):  # Voris klass
#     def ovoz_chiqar(self):
#         return "Vov-vov!"
#
#
# it = It()
# print(it.ovoz_chiqar())  # Natija: Vov-vov!

# Oddiy klassni to‘liq aniqlash nimani anglatadi?
# Oddiy klassning metodlari:
#
# To‘liq ishlash kodiga ega.
# Klass obyekt sifatida to‘g‘ridan-to‘g‘ri ishlatilishi mumkin.

# Abstract klassda nima to‘liq emas?

# Abstract klassdagi metodlarda ishlash qoidasi faqat aniqlanadi,
# lekin ular qanday bajarilishi noma'lum bo‘ladi. Shu sababli,
# abstract klassdan obyekt yarata olmaysiz.
#
# Abstract metodni to‘liq aniqlash uchun voris klassda u qayta yozilishi kerak:

# Xulosa
# Oddiy klass: Metodlari to‘liq aniqlangan. Bunda har bir metod aniq funksional
# kodga ega bo‘ladi va klassdan obyekt yaratilishi mumkin.

# Abstract klass: Metodlari to‘liq aniqlanmagan. Bunday klassdan obyekt
# yaratib bo‘lmaydi. Voris klasslar abstract metodlarni to‘liq aniqlab, ularni ishlatishga yaroqli qiladi.




