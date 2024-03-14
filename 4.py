cor_answer_1 = "нет"
cor_answer_2 = "да"
answer = input("Вы поедете на бал?: ")
if not((answer.lower() == cor_answer_1) or (answer.lower() == cor_answer_2)):
    print("Верно!")
else:
    print("Неверно!")

