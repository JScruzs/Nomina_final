import re

nomina=[]
userResponses = ['si','no']
pregunta_1 = ""

def checkUserResponse(userInput):
     if pregunta_1 not in userResponses:
          print(' => Responde si o no en letra minuscula ')
          return False   
     else:
          return True

def checkIfOnlyNumbers(userInput):
     try:
          int(userInput)
     except :
          print(" => Solo se pueden ingresar numeros")
          return False
     return True

def checkIfCharachtersOnly(userInput):
     pattern = re.compile("[A-Za-z]+")
     pattern.fullmatch(userInput)
     # if found match (entire string matches pattern)
     if pattern.fullmatch(userInput) is not None:
          return True
     else:
          # if not found match
          print(" => Solo se pueden ingresar letras")
          return False

def inputUserID():
     inputNotOk = False
     documento = 0
     while not inputNotOk:
          documento=input("Escribe tu numero de documento: ")
          inputNotOk = checkIfOnlyNumbers(documento)
     return int(documento)

def inputWorkedDays():
     inputNotOk = False
     days =0
     while not inputNotOk:
          days=input("Digite el numero de dias trabajados: ")
          inputNotOk = checkIfOnlyNumbers(days)
     return int(days)

def inputName():
     inputNotOk = False
     name =""
     while not inputNotOk:
          name=input("Escribe tu primer nombre: ")
          inputNotOk = checkIfCharachtersOnly(name)
     return name

def inputSecondName():
     inputNotOk = False
     name =""
     while not inputNotOk:
          name=input("Escribe tu segundo nombre: ")
          inputNotOk = checkIfCharachtersOnly(name)
     return name

def inputSurname():
     inputNotOk = False
     name = ""
     while not inputNotOk:
          name=input("Escribe tu primer apellido: ")
          inputNotOk = checkIfCharachtersOnly(name)
     return name

def inputSecondSurname():
     inputNotOk = False
     name = ""
     while not inputNotOk:
          name=input("Escribe tu segundo apellido: ")
          inputNotOk = checkIfCharachtersOnly(name)
     return name

pregunta_1=str(input("Desea hacer su nomina si/no (responde en letras minusculas): "))

if checkUserResponse(pregunta_1):
     while (pregunta_1 == "si"):
          documento = inputUserID()
          nombres =inputName()
          secondname =inputSecondName()
          apellidos =inputSurname()
          secondsurname = inputSecondSurname()
          dias_trabajados = inputWorkedDays()
          salario=33333
          salario_base = salario*dias_trabajados
          salario_total= (salario_base-((salario_base*0.04)*2))+117100
          for i in range(1):
               nomina.append(documento)
               nomina.append(nombres)
               nomina.append(secondname)
               nomina.append(apellidos)
               nomina.append(secondsurname)
               nomina.append(salario)
               nomina.append(dias_trabajados)
               nomina.append(salario_total)

          pregunta_1 = str(input("Desea continuar si/no: "))
  
     counter =0 
     for item in nomina:
          if counter % 6 == 0:
               print("-----\n")
          print(item)
          counter += 1             

x=open("Nomina.txt","a")
x.write (str(nomina))