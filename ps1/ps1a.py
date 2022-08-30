# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 20:30:46 2022

@author: isabela Cristina
"""
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

monthly_salary = float(annual_salary/12)    #obtendo o salario mensal
portion_down_payment = 0.25                 #porcentagem de pagamento inicial da casa
current_savings = 0                         #montante atual reservado
down_payment = total_cost * portion_down_payment
#valor de entrada da casa
portion_saved = portion_saved * monthly_salary
#parte da renda mensal que sera reservada
r = 0.04                                    #rendimento anual dos investimentos
total_months = 0                            #meses totais para a reserva atingir o valor
                                            #de entrada da casa
                                            
while current_savings < down_payment:       #enquanto a reserva for menor que a entrada
    investments_return = current_savings * r/12
    #investimento recebe o montante aplicado vezes a taxa de rendimento mensal
    current_savings = current_savings + investments_return + portion_saved
    #montante aplicado é incrementado com o retorno dos investimentos + parte do salario
    total_months = total_months + 1
    #o retorno dos investimentos e incremento no montante ocorre 1x por mes
    #total_months é a quantidade de meses necessarios para atingir a meta
    
print("Number of months:", total_months)