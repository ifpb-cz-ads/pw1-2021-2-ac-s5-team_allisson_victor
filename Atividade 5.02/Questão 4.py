casa = int(input("Informe o valor da casa:"))
salario = int(input("Informe a miseria recebida mensalmente:"))
anos = int(input("Em quantos anos deseja pagar?"))  
trinta = salario*0.30
meses = anos * 12
parcelas =casa/meses

if parcelas < trinta:
    print ("O valor das parcelas serão de:", parcelas,)
else:
    print("O valor das parcelas excede 30% do valor do seu salario")
    