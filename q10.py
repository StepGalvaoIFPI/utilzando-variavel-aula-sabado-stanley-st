salario = 5000
ir = 0.1
descontoIR = salario*ir
inss = 0.15 
descontoINSS = salario*inss
valor_liqquido= salario- descontoINSS-descontoIR
print(salario)
print(descontoINSS)
print(descontoIR)
print(valor_liqquido)
