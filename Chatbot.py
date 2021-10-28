from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp

engine = pp.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)
def speak(word):
    engine.say(word)
    engine.runAndWait()
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
    'What is machine learning?',
    'Machine learning is the study of computer algorithms that can improve automatically through experience and by the use of data. It is seen as a part of artificial intelligence',
    'Who taught you machine learning?',
    'Professor Sejal Thakkar',
    'which language do you prefer to talk to?',
    'I was written in Python language but i talk in English Language :)',
    'who is your favorite actor?',
    'shahrukh khan',

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
main.geometry("700x450")
main.title("Welcome to the wonderful world of Jarvis")
def shoot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    speak(answer_from_bot)
    print(type(answer_from_bot))

    msgs.insert(END, "Jarvis : " + str(answer_from_bot))
    textF.delete(0, END)
    msgs.yview(END)

frame = Frame(main)
sc = Scrollbar(frame)

msgs = Listbox(frame, width=80, height = 10, yscrollcommand = sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()
textF = Entry(main, font=("Verdana", 15))
textF.pack(fill=X, pady=10)
btn=Button(main,text="Shoot", font=("Verdana",15), command=shoot)
btn.pack()
def enter_function(event):
    btn.invoke()
main.bind('<Return>', enter_function)
main.mainloop()