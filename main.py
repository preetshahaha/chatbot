from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
bot = ChatBot("jarvis")

convo = [
    'hello',
    'hi',
    'howdy',
    'how are you?',
    'I am doing great these days',
    'what is your name?',
    'My name is jarvis',
    'where do you live',
    'i live in the heart of Mr. Preet',
    'how were you created',
    'I was created by a bunch of idiots for a Machine learning project',

    'thank you'
]

trainer = ListTrainer(bot)
trainer.train(convo)
# answer = bot.get_response("what is your name?")
# print(answer)
# print("Fire up Jarvis")
# while True:
#     query=input()
#     if query=='exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ", answer)

main = Tk()
main.geometry("300x350")
main.title("Welcome to the wonderful world of Jarvis")
def shoot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))

    msgs.insert(END, "Jarvis : " + str(answer_from_bot))
    textF.delete(0, END)

frame = Frame(main)
sc = Scrollbar(frame)

msgs = Listbox(frame, width=80, height = 10)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
textF = Entry(main, font=("Verdana", 15))
textF.pack(fill=X, pady=10)
btn=Button(main,text="Shoot", font=("Verdana",15), command=shoot)
btn.pack()
main.mainloop()