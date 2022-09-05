# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 17:16:46 2022

@author: isabela Cristina
"""

annual_salary = float(input("Enter the starting salary: "))
monthly_salary = float(annual_salary/12)
total_cost = 1000000                        #preço total da casa
semi_annual_raise = 0.07                    #aumento semestral
portion_down_payment = 0.25                 #porcentagem de pagamento inicial da casa
current_savings = 0                         #montante atual reservado
r = 0.04                                    #rendimento anual dos investimentos
total_months = 0                            #meses totais para a reserva atingir o valor
down_payment = total_cost * portion_down_payment   #valor de entrada da casa

#variaveis para bisseção                                            
epsilon = 100                           #variação máxima entre entrada e montante atual
steps = 0                               #numero de passos na bisseção
low = 0                                 #limite inferior
high = 10000                            #limite superior indicado no exercicio
guess = (high + low)//2.0               #realizando a bisseção
rate_of_savings = 0.5

def savings_calc(portion_saved):
    savings = 0
    total_months = 0
    monthly_salary = float(annual_salary/12)
    for months in range (36):       
         investments_return = savings * r/12
         #investimento recebe o montante aplicado vezes a taxa de rendimento mensal
         savings += investments_return + (monthly_salary * portion_saved)
         #montante aplicado é incrementado com o retorno dos investimentos + parte do salario
         total_months += 1
         #o retorno dos investimentos e incremento no montante ocorre 1x por mes
         #total_months é a quantidade de meses necessarios para atingir a meta
         if total_months % 6 == 0:
             monthly_salary += monthly_salary * semi_annual_raise
    return savings

#-----------------------------------
#código principal

current_savings = savings_calc(1)       #checando se o salário é suficiente
if current_savings < (down_payment - epsilon):  
    print("It is not possible to pay the down payment in three years.")

#inicio da busca por bisseção
else:                                   #achando a menor taxa de reserva do salario
    while abs(current_savings - down_payment) > epsilon:
        current_savings = savings_calc(rate_of_savings)  
    
        if current_savings < (down_payment - epsilon):
            low = guess
            
        elif current_savings > (down_payment - epsilon):
            high = guess
        guess = (high + low)//2.0
        rate_of_savings = float(guess/10000)
        steps += 1
        
    print("Best savings rate:", rate_of_savings)
    print("Steps in bisection search:", steps)        
