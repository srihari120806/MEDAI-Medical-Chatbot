def medical_bot():
    n=input("enter your name :")
    x=int(input("enter your age :"))
    print("HI , my dear friend",n)
    j=int(input("""
1. Male
2. Female
3. prefer not to say"""))

    if j==1 or j==3:
        def hp(x):
            if x<=5:
                print("""paracetamol 250mg

Side Effects:
In some cases, taking high doses of paracetamol or using
it for prolonged periods can lead to more severe side effects,
including liver damage or failure.Overdosing on paracetamol
can be dangerous and may require immediate medical attention.""")
            elif x>5 and x<=15:
                print("""paracetamal 500

Side Effects:
In some cases, taking high doses of paracetamol or using
it for prolonged periods can lead to more severe side effects,
including liver damage or failure.Overdosing on paracetamol
can be dangerous and may require immediate medical attention.""")
            elif x>15:
                print("""paracetamal 650

Side Effects:
In some cases, taking high doses of paracetamol or using
it for prolonged periods can lead to more severe side effects,
including liver damage or failure.Overdosing on paracetamol
can be dangerous and may require immediate medical attention.""")

        print("""
1.Head Ache
2.Stomach Ache
3.Cold And Cough
4.Ear Problem
5.Eye Infection
6.Painkiller
7.Vomiting
8.Chest pain
9.Breathing problem
10.Fever
11.Seasonal Allergies
12.Throat Infection
13.Joint And Body Pain(Internal)
14.Exit""")
        while True:
            ch=int(input("Enter your choice:"))
            if ch==1:
                hp(x)
            elif ch==14:
                break
            else:
                print("Option available in the original project")
        print("Thank You!")


def first_aid():
    print("""
1.Stopped Heart
2.Bleeding
3.Choking
4.Burns
5.Blisters
6.Sprains
7.Nosebleeds
8.Bee Sting
9.First Aid Kit List
10.exit""")
    while True:
        ch=int(input("enter your choice"))
        if ch==10:
            break
        else:
            print("First-aid information is included in the full source project.")
    print("Thank You!")


def boss():
    def bmi():
        w=int(input("enter your weight in kg"))
        h=int(input("enter your height in cm"))
        h1=h/100
        h2=h1**2
        bmi=(w/h2)
        print("your bmi is ",bmi)
        if bmi<19:
            print("underweight !!!")
            print("please eat healthy food :)")
        elif bmi >= 19 and bmi <24:
            print("congrats .....")
            print("you have a good health")
        else:
            print("oops ! over weight")
            print("please stay fit and healthy")

    while True:
        ch=int(input("""
1.Check BMI
2.Exit
enter your choice"""))
        if ch==1:
            bmi()
        elif ch==2:
            break
        else:
            print("Invalid choice")


while True:
    ch=int(input("""
1.Medical bot
2.First aid tips
3.BMI calculator
4.Exit
enter your choice"""))
    if ch==1:
        medical_bot()
    elif ch==2:
        first_aid()
    elif ch==3:
        boss()
    elif ch==4:
        break
    else:
        print("Invalid choice")
print("Thank You!")