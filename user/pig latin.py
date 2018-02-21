


vowels = ['a','e','i','o','u']
user_input = input("Enter an English word: ",).lower()
index = 0

while user_input != 'quit':

    if user_input [index] in vowels:
        print(user_input+"way")


    while user_input[index] not in vowels:
            index += 1
            if user_input[index] not in vowels:
                print("Pig Latin form: "+user_input[index:]+user_input[:index]+"ay")

    user_input = input("Enter an English word: ",).lower()
    index = 0





        
