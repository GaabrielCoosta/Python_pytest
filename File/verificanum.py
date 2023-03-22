"""Criação das funções responsáveis pela verificação. A função retornar se os números inseridos pelo usuário correspondem ou não
a serem multiplos de 7 ou 5 """

def multiplos_ambos():
    
    try:
        a = int(input("Digite um número natural: "))
        
        if (a % 5 == 0) and (a % 7 == 0):
            resultado = print('fizzbuzz')
            return resultado
        
        else:
            resultado = print('Nuúmero digitado não é multiplo de 5 e nem de 7!')
            return resultado
    
    except TypeError as e:
        resultado = f'''Você precisa informar um número natural.
        Por favor, digite um número posito e inteiro! - {e}''' 
    return resultado 

def multiplos5():
    
    try:
        a = int(input("Digite um número natural: "))
        
        if a % 5 == 0:
            resultado = print('fizz')
            return resultado
        
        else:
            resultado = print('Número digitado não é multiplo de 5!')
            return resultado
    
    except TypeError as e:
        resultado = f'''Você precisa informar um número natural.
        Por favor, digite um número posito e inteiro! - {e}'''
    return resultado 

def multiplos7():
    
    try:
        a = int(input("Digite um número natural: "))
        
        if a % 7 == 0:
            resultado = print('buzz')
            return resultado
        else:
            resultado = print('Número digitado não é multiplo de 7!')
            return resultado
    
    except TypeError as e:
        resultado = f'''Você precisa informar um número natural.
        Por favor, digite um número posito e inteiro! - {e}''' 
    return resultado 

def multiplos_vazio():
    
    try:
        a = int(input("Digite um número natural: "))
        
        if (a % 7 != 0) and (a % 5 != 0):
            resultado = print('miss')
            return resultado
        
    
    except TypeError as e:
        resultado = f'''Você precisa informar um número natural.
        Por favor, digite um número posito e inteiro! - {e}''' 
    return resultado

multiplos5()
