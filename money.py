student={
    'aziz':{'matematika':5,'ingliz tili':3},
    'azam':{'matematika':4,'ingliz tili':4},
    'vali':{'matematika':2,'ingliz tili':3.5},
    'ali':{'matematika':5,'ingliz tili':2},
}
student.update({'azamat':{'matematika':3,'ingliz tili':3}})
student.pop('aziz')
print(student)
for ism,fanlar in student.items():
    print(ism,fanlar)
    ortacha=sum(fanlar.values())/len(fanlar)
    if ortacha<3:
        print(f"{ism.title()}-siz uta olmadingiz:")
    else:
        print(f"{ism.title()}-tabriklayman uta oldingiz")
        .
ssh-keygen -t ed25519 -C "avazlapasov198@gmail.com"
"avazlapasov198@gmail.com"
