#pizza ={
#    'Four cheese':['cheese,chicken','tomato'],
#    'Paperroni':['kovbassas','cheese','tomato','souce']
#    }
#for p,i in pizza.items():
#    print('-------------------'*3000)
#    print(f"vi zakazali {p}:")
#    for value in i:
#        print(f"\t-{value.title()}")


#def den():
#   for p,i in students.items():
 #       print("-"*30)
#        print(f"{p} решил задачку:")
 #       for tasks in i:
 #           print(f"\t-{tasks}")
#students = {
#    'kiril':["task1","task2","task3","task4","task5","task6","task7","task8","task9"],
#    'renat':["task1","task2","task3","task4"],
#    'vanya':["task1"],
#    'yarik':["task1","task2","task3","task4","task5"],
#    }
#den()


#Info about players


def jojo():
    for p,i in players.items():
        print(f"Игрок под именем{p}:")
        players_info=f"{i['first_name']} {i['last_name']}"
        age=f"emu {i['age']}"
        ip=f"ego adress:{i['IP']}"
        country="on jivet v {i['country']}"
        print(f"\timya familiya:{players_info.title()} emu:{age} IP:{ip}strana{country} ")
players={
    'user_0':{
        'first_name':'renat',
        'last_name':'Net',
        'age':14,
        'IP':"49.15.46",
        'country':'UK'
        },
    'user_1':{
        'first_name':'vania',
        'last_name':'da',
        'age':12,
        'IP':"50.14.14",
        'country':'Japan'
        },
    'user_2':{
        'first_name':'kiril',
        'last_name':'hz',
        'age':0,
        'IP':"0.0.0",
        'country':'Azerbaigan'
        }
    }
jojo()
