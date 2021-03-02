def privileges(method_name):
    print("Run " + method_name + " method as: \n1 --> Administrator \n2 --> User")
    answer = input("Your Answer: ")
    while answer != '1' and answer != '2':
        print("Invalid answer. Please try again.")
        answer = input("Your answer: ")
    return answer
