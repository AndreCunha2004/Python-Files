# Este programa é para revisar os comandos que aprendi até agora.
# Iremos cadastrar um pessoa, com diversas características e trabalhar alguns conceitos.


# Prompt
print("Follow according to your profile!\n")

# 1º Passo - Características simples
name = input("What's your name? ")
age = int(input("Type your age: "))
height = float(input("Type your height: "))
hobby = input("What's your favorite hobby? ")
dream_job = input("What's your dream job? ")


# 2º Passo - Verifica se é maior de idade
maioridade = age >= 18

if maioridade:
    print("\nCONGRATS DUDE!")
    print("You're already a man!\n")
else:
    print("\nI'm really sorry man... :(\n")

# 3º Passo - Verificar o possível cargo de acordo com a renda
salary = float(input("Whats your mensal income? $"))

if salary < 1160:
    education_level = "Middle school"
elif salary < 2900:
    education_level = "High school"
elif salary < 3664:
    education_level = "Higher education"
elif salary < 6740:
    education_level = "Master degree"
else:
    education_level = "Uknown"

# 4º Passo - Verificando outliers
answer = input(f"\nYour education level may be {education_level}. Is that correct? (Yes/No): ")

if answer.lower() != "yes":
    print("\nWow. It seems that you are an outlier...")
    if age <=18 and salary >= 3664:
        awnser = input("\nDude, tell me the secret to be rich!\n(I'm serius, type here): ")
    elif age > 18 and salary <=3664:
        awnser = input("\nDude... Don't be sad, you still have time to grow!\n(Blow off with me bro):")
    else:
        awnser = input("\nWhat a fuck are you doing, bro? ")
else:
    print("\nWell, it seems that you are on the right path!\n Don't give up...\n")

print("\nThan, thank for been pacient!\n")
# 5º Passo - Calcular quantos anos faltam pra 100 anos
years_to_100 = 100 - age

# 6º Passo -  Armazenar dados em um dicionário
Profile = {
    "Name": name,
    "Age": age,
    "Height": height,
    "Hobby": hobby,
    "Dream job": dream_job,
    "Is adult": maioridade,
    "Monthly Income": salary,
    "Education Level": education_level,
    "Years to 100": years_to_100
}

# 7º Passo - Exibir um relatório completo
print("\n--- PROFILE SUMMARY ---")
for key, value in Profile.items():
    print(f"{key}: {value}")

print("\nThanks for sharing your profile with us!")
