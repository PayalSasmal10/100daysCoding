import time
print("Welcome to Cartoon quize !")
user = input("May I know your name : \n")
print("Hi", user, "Let's get started\n")

chos_cart = input("Are you a fan of Doraemon or Shinchan: ")
score = 0
total = 10
if chos_cart.lower() == "doraemon":
    print("Wow, You have choosen Doraemon, Let's see how much do you know about Doraemon Cartoon\n")
    time.sleep(5)
    ans = input(
        "1. What is the color of Dorami, Doraemon's sister? \na. Pink \nb. Yellow \nc. Blue \nd. Black \n")
    if ans.lower() == "b" or ans.lower() == "yellow":
        score += 1
        print("Your answer is correct ")
    else:
        print("your answer is wrong")

    ans = input(
        "2. What is Gian's Passion? \na. Singing  \nb. Dancing \nc. Irritating \nd. Studying \n")
    if ans.lower() == "a" or ans.lower() == "singing":
        score += 1
        print("Your answer is correct ")
    else:
        print("your answer is wrong \n")
        if score == "0":
            print("No worry !, Lets play more quize \n")

    ans = input(
        "3. What does Doraemon makes scared? \na. Gian  \nb. Dorami \nc. Nobita's Mom \nd. Rat \n")
    if ans.lower() == "d" or ans.lower() == "rat":
        score += 1
        print("Your answer is correct ")
    else:
        print("your answer is wrong \n")

    ans = input(
        "4. Who is Doraemon Best friend? \na. Shizuka \nb. Gian \nc. Nobita \nd. Suneo \n")
    if ans.lower() == "c" or ans.lower() == "nobita":
        score += 1
        print("Your answer is correct\n")
    else:
        print("your answer is wrong\n")

    ans = input(
        "5. What is the color of Dorami, Doraemon's sister? \na. Pink \nb. Yellow \nc. Blue \nd. Black \n")
    if ans.lower() == "b" or ans.lower() == "yellow":
        score += 1
        print("Your answer is correct\n")
    else:
        print("your answer is wrong\n")

    ans = input(
        "6. What does Doraemon love to eat? \na. Chocolate \nb. Doracake \nc. Cookies \nd. None of the above \n")
    if ans.lower() == "b" or ans.lower() == "doracake":
        score += 1
        print("Your answer is correct\n")
    else:
        print("your answer is wrong\n")

    ans = input(
        "7. Which gadget of Doraemon helps to go anywhere? \na. Animated Door \nb. Anywhere Cycle \nc. Bamboo Copter \nd. Anywgere Door \n")
    if ans.lower() == "d" or ans.lower() == "anywhere door":
        score += 1
        print("Your answer is correct\n")
    else:
        print("your answer is wrong\n")

    ans = input(
        "8. Nobita has crush on _____ \na. Jackio \nb. Deki \nc. Niami \nd. Shizuka \n")
    if ans.lower() == "d" or ans.lower() == "shizuka":
        score += 1
        print("Your answer is correct\n")
    else:
        print("your answer is wrong\n")

    ans = input(
        "9. Who is the most intelligent among these? \na. Nobita \nb. Shizuka \nc. Dekisugi \nd. Suneo \n")
    if ans.lower() == "c" or ans.lower() == "dekisugi":
        score += 1
        print("Your answer is correct\n")
    else:
        print("your answer is wrong\n")

    ans = input(
        "10. Which century Doraemon come from? \na. 21st century \nb. 20th century \nc. 22nd century \nd. None of the above \n")
    if ans.lower() == "b" or ans.lower() == "yellow":
        score += 1
        print("Your answer is correct\n")
    else:
        print("your answer is wrong\n")


elif chos_cart.lower() == "shinchan":
    print("Wow, Are you crazy about Shinchan? Let's see how much do you know about Shinchan Cartoon\n")
    time.sleep(5)

    ans = input(
        "1. What is the name of Shinchan's Dog? \na. kazama \nb. Suzuki \nc. Yamaha \nd. Shiro \n")
    if ans.lower() == "d" or ans.lower() == "shiro":
        score += 1
        print("Your answer is correct\n")
    else:
        print("your answer is wrong\n")

    ans = input(
        "2. What is the vegetable that Shinchan hates to eat? \na. Garlic \nb. Beans \nc. Capsicum \nd. Carrot \n")
    if ans.lower() == "c" or ans.lower() == "capsicum":
        score += 1
        print("Your answer is correct\n")
    else:
        print("your answer is wrong\n")

    ans = input(
        "3. What is the color of the dress Shinchan's sister Himawari wears? \na. Pink \nb. Yellow \nc. Blue \nd. Black \n")
    if ans.lower() == "b" or ans.lower() == "yellow":
        score += 1
        print("Your answer is correct\n")
    else:
        print("your answer is wrong\n")

    ans = input(
        "4. Whom does Shinchan's teacher Yoshinaga marry? \na. Kazama \nb. Suzuki \nc. Ishida Junichi \nd. Yamaha \n")
    if ans.lower() == "c" or ans.lower() == "ishida junichi":
        score += 1
        print("Your answer is correct\n")
    else:
        print("your answer is wrong\n")

    ans = input(
        "5. What is the name of Shinchan's favourite action hero? \na. Action Kamen \nb. Sailor Moon \nc. James Bond \nd. Captain Shinchan\n")
    if ans.lower() == "a" or ans.lower() == "action kamen":
        score += 1
        print("Your answer is correct\n")
    else:
        print("your answer is wrong\n")

    ans = input(
        "6. What is the name of Shinchan's mom? \na. Miranda \nb. Mandy \nc. Milli \nd. Misae \n")
    if ans.lower() == "d" or ans.lower() == "misae":
        score += 1
        print("Your answer is correct\n")
    else:
        print("your answer is wrong\n")

    ans = input(
        "7. Which of the following teacher seems to be nervous? \na. Matsuzaka \nb. Yoshinaga \nc. Masumi \nd. None of the above \n")
    if ans.lower() == "c" or ans.lower() == "masumi":
        score += 1
        print("Your answer is correct\n")
    else:
        print("your answer is wrong\n")

    ans = input(
        "8. What is the name of the group created by shinchan and his friends? \na. Futaba Defence Group \nb. Kindergarden Defence Group \nc. Wasabi Defence Group \nd. Kasukabe Defence Group \n")
    if ans.lower() == "d" or ans.lower() == "kasukabe defence group":
        score += 1
        print("Your answer is correct\n")
    else:
        print("your answer is wrong\n")

    ans = input(
        "9. What is the name of Shinchan's maternal aunt? \na. Misti \nb. Masae \nc. Nanaco \nd. Matsuzaka \n")
    if ans.lower() == "b" or ans.lower() == "Masae":
        score += 1
        print("Your answer is correct\n")
    else:
        print("your answer is wrong\n")

    ans = input(
        "10. Who is Shinchan's richest friend? \na. Mitsuo \nb. Kazama \nc. Naini \nd. Misae \n")
    if ans.lower() == "b" or ans.lower() == "kazama":
        score += 1
        print("Your answer is correct\n")
    else:
        print("your answer is wrong\n")


else:
    print("Please choos the correct charecter")

print("Thank you for playing you got", score, "questions correct.")
mark = (score/total) * 100
print("Marks:", mark)
print("GoodBye")
