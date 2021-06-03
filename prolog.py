from pyswip import Prolog
prolog = Prolog()
prolog.consult("khanfamily.pl")
menu="""
Which Relation You Want to Find......?
Press :
    1  for baap                  2  for maa            3  for beta                  4  for beti
    5  for dada                  6  for dadi           7  for nana                  8  for nani
    9  for sala                  10 for sali           11 for bahu                  12 for damad
    13 for pota                  14 for poti           15 for nawasa1               16 for nawasi
    17 for sussar                18 for chachataya     19 for khala                 20 for baap dada 
"""
print(menu)
choice=int(input("Enter Your Choice : "))

if(choice==1):
    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"baap(X,{name})"):
            print(soln["X"], "is the father of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is father of : ")
        if len(list(prolog.query(f"baap(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"baap(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)  


       
elif(choice==2):

    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"maa(X,{name})"):
            print(soln["X"], "is the mother of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is mother of : ")
        if len(list(prolog.query(f"maa(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"maa(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)  


elif(choice==3):
    
    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"beta(X,{name})"):
            print(soln["X"], "is the son of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is son of : ")
        if len(list(prolog.query(f"beta(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"beta(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)
                      
elif(choice==4):
    
    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"beti(X,{name})"):
            print(soln["X"], "is the daughter of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is daughter of : ")
        if len(list(prolog.query(f"beti(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"beti(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)     
elif(choice==5):
    
    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"dada(X,{name})"):
            print(soln["X"], "is the dada of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is dada of : ")
        if len(list(prolog.query(f"dada(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"dada(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)     
elif(choice==6):
    name=input("Enter Name: ")
    for soln in prolog.query(f"dadi(X,{name})"):
        print(soln["X"], "is the dadi of",name)
    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"dadi(X,{name})"):
            print(soln["X"], "is the dadi of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is dadi of : ")
        if len(list(prolog.query(f"dadi(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"dadi(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue) 

elif(choice==7):
    
    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"nana(X,{name})"):
            print(soln["X"], "is the nana of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is nana of : ")
        if len(list(prolog.query(f"nana(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"nana(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)     
elif(choice==8):

    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"nani(X,{name})"):
            print(soln["X"], "is the nani of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is nani of : ")
        if len(list(prolog.query(f"nani(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"nani(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)      
elif(choice==9):
    
    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"sala(X,{name})"):
            print(soln["X"], "is the sala of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is sala of : ")
        if len(list(prolog.query(f"sala(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"sala(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)  

elif(choice==10):
    
    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"sali(X,{name})"):
            print(soln["X"], "is the sali of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is sali of : ")
        if len(list(prolog.query(f"sali(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"sali(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)      
elif(choice==11):
    name=input("Enter Name: ")
    for soln in prolog.query(f"bahu(X,{name})"):
        print(soln["X"], "is the bahu of",name)
    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"bahu(X,{name})"):
            print(soln["X"], "is the bahu of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is bahu of : ")
        if len(list(prolog.query(f"bahu(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"bahu(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)



elif(choice==12):
    
    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"damad(X,{name})"):
            print(soln["X"], "is the damad of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is damad of : ")
        if len(list(prolog.query(f"damad(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"damad(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)    
elif(choice==13):
    
    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"pota(X,{name})"):
            print(soln["X"], "is the pota of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is pota of : ")
        if len(list(prolog.query(f"pota(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"pota(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)     
elif(choice==14):
    
    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"poti(X,{name})"):
            print(soln["X"], "is the poti of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is poti of : ")
        if len(list(prolog.query(f"poti(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"poti(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)     
elif(choice==15):
    
    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"nawasa(X,{name})"):
            print(soln["X"], "is the nawasa of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is nawasa of : ")
        if len(list(prolog.query(f"nawasa(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"nawasa(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)     
elif(choice==16):
    
    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"nawasi(X,{name})"):
            print(soln["X"], "is the nawasi of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is nawasi of : ")
        if len(list(prolog.query(f"nawasi(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"nawasi(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)    
elif(choice==17):
    
    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"sassur(X,{name})"):
            print(soln["X"], "is the sassur of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is sassur of : ")
        if len(list(prolog.query(f"sassur(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"sassur(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)     
elif(choice==18):
      
    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"chachataya(X,{name})"):
            print(soln["X"], "is the chachataya of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is chachataya of : ")
        if len(list(prolog.query(f"chachataya(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"chachataya(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)      
elif(choice==19):
    
    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"khala(X,{name})"):
            print(soln["X"], "is the khala of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is khala of : ")
        if len(list(prolog.query(f"khala(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"khala(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)    
elif(choice==20):
    
    choice2=input("""
    Enter 'a' for simple query
    Enter 'b' for validating query
    """)
    if choice2=="a":
        name=input("Enter Name: ")
        for soln in prolog.query(f"baapdada(X,{name})"):
            print(soln["X"], "is the baapdada of",name)
    elif choice2=="b":
        fact1 ,fact2= input("fact 1 : "),input("is baapdada of : ")
        if len(list(prolog.query(f"baapdada(X,{fact2})")))==0:
            print("false")
        else:
            for soln in prolog.query(f"baapdada(X,{fact2})"):
                if(soln["X"] == fact1):
                    istrue = True 
                    break  
                else:
                    istrue = False
            print(istrue)     
    