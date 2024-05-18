def add(x,y):
    return x + y

def sub(x,y):
  return x - y 

def mult(x,y):
  return x * y

def divi(x,y):
  return x/y 

print ("Selecione uma operação.")
print ("1. Adição.")
print ("2. Subtração.")
print ("3. Multiplicação")
print ("4. Divisão")


escolha = input("Escolha uma opção (1,2,3,4)")

if escolha in ('1','2','3','4'):
  n1 = float(input("Digite um numero:"))
  n2 = float(input("Digite outro numero:"))
  
  if escolha == '1':
    print(add(n1,n2))
  
  if escolha == '2':
    print(sub(n1,n2))
  
  if escolha == '3':
    print(mult(n1,n2))
  
  if escolha == '4':
    if n2 != 0:
      print(divi(n1,n2))

    else:
      print("Erro: divisão por 0 ")
else:
  print("Escolha invalida. Por favor, escolha uma opção valida (1,2,3,4)")
