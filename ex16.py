def validar_senha(senha):
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tamanho_ok = len(senha) >= 8

    if tamanho_ok and tem_numero and tem_maiuscula:
        return "Senha Top"
    else:
        return "Senha Fraca"
    
print(validar_senha('abc12324A'))