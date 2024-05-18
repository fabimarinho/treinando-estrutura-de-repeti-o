def validar_nome():
    while True:
        nome = input("Digite o nome (maior que 3 caracteres): ")
        if len(nome) > 3:
            return nome
        else:
            print("Nome inválido. O nome deve ter mais de 3 caracteres.")

def validar_idade():
    while True:
        try:
            idade = int(input("Digite a idade (entre 0 e 150): "))
            if 0 <= idade <= 150:
                return idade
            else:
                print("Idade inválida. A idade deve estar entre 0 e 150.")
        except ValueError:
            print("Idade inválida. Por favor, insira um número inteiro.")

def validar_salario():
    while True:
        try:
            salario = float(input("Digite o salário (maior que zero): "))
            if salario > 0:
                return salario
            else:
                print("Salário inválido. O salário deve ser maior que zero.")
        except ValueError:
            print("Salário inválido. Por favor, insira um número.")

def validar_sexo():
    while True:
        sexo = input("Digite o sexo ('f' ou 'm'): ").lower()
        if sexo in ['f', 'm']:
            return sexo
        else:
            print("Sexo inválido. Por favor, insira 'f' para feminino ou 'm' para masculino.")

def validar_estado_civil():
    while True:
        estado_civil = input("Digite o estado civil ('s', 'c', 'v', 'd'): ").lower()
        if estado_civil in ['s', 'c', 'v', 'd']:
            return estado_civil
        else:
            print("Estado civil inválido. Por favor, insira 's' para solteiro, 'c' para casado, 'v' para viúvo, ou 'd' para divorciado.")

def main():
    nome = validar_nome()
    idade = validar_idade()
    salario = validar_salario()
    sexo = validar_sexo()
    estado_civil = validar_estado_civil()
    
    print("\nInformações validadas com sucesso:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: {salario:.2f}")
    print(f"Sexo: {sexo}")
    print(f"Estado Civil: {estado_civil}")

if __name__ == "__main__":
    main()
