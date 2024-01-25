from datetime import date
atual = date.today().year

total = 0
maior = 0
for i in range (6):
    ano = int(input(f'Informe o ano de Nascimento da {i+1}ª: '))
    idade = atual - ano
    
    if idade < 18:
        total += 1
    else:
        maior +=1
        
print(f'Temos {maior} pessoas maiores de idade na lista')    
print(f'Temos {total} pessoas da lista tem menos de 18 anos')