def contar_vogais(texto):
    vogais = 'aeiouAEIOU'
    contador = 0
    for l in texto:
        if l in vogais:
            contador +=1
    return contador


texto = input ("Digite")
print (contar_vogais(texto))
