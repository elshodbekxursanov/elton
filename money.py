# def hello(ism):
#     print(f'assalomu aleykum {ism}')
# hello(input("ism kiriting:"))

# def kvadrat(son):
#     print(son*son)
# kvadrat(int(input("sonni kiritng:")))

# def yosh(age):
#     year=2025
#     print(f"{year}-{age}={year-age}")
# yosh(int(input("yilingizni kiritng:")))

# son=[2,4,3,5,7]
# def kvadrat(number):
#     for n in son:
#         print(n**2)
# kvadrat(5)
#
# def open_close():
#     kod=12345678
#     def check_parol(parol):
#         return parol==kod
#     return check_parol
# sana=0
# while True:
#     user=int(input('parolni kiriting:'))
#     if user==0:
#         break
#     sana+=1
#     answer=open_close()
#     n=answer(user)
#     if n:
#         print('siz kirishingiz mumkin:')
#         break
#     else:
#         print('xato')
#     if sana==3:
#         print("yuqolllllll")
#         break

# def savdo():
#     mahsulotlar={
#         'olma':5000,
#         'anor':12000,
#         'behi':21000,
#         'olcha':10000
#     }
#     for meva,narx in mahsulotlar.items():
#         print(meva,narx)
#     jami=sum(mahsulotlar.values())
#     print(f"jami summa {jami} buldi")
#     if jami>30000:
#         print(jami-jami/100)
# savdo()

# def email_tekshir():
#     email = input("Email manzilingizni kiriting: ")
#
#     if "@" in email and "." in email:
#         print(" Email manzili to‘g‘ri.")
#     else:
#         print(" Email manzili noto‘g‘ri.")
#
# email_tekshir()
# son=[1,2,3,4,5,6,7,8,9,10,11,1,2]
# def juft():
#     for i in son:
#         if i%2==0:
#             print(i)
# juft()
#
# def oylikni_hisoblash():
#     soat=float(input('ishlagan soatingizni kiriting:'))
#     stavka=float(input(' soatlik stavkani kiriting:'))
#     oylik=soat*stavka
#     print(f"ishchining oyligi {oylik}$")
# oylikni_hisoblash()









