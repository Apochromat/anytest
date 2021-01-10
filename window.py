from tkinter import *
from tkinter import messagebox as mb
import questions

QHeap = questions.QuestionHeap()


class Root(Tk):
    def __init__(self):
        super().__init__()
        self.run = True
        self.question_number = 0
        self.title(QHeap.get_title())
        self.geometry('640x480')
        self.configure(bg="lavender")
        self.resizable(0, 0)
        self.status = Label(self, width=50, text="Готов", bg="lavender", font=("Arial", 8), anchor=W)
        self.status.place(x=0, y=460)
        self.cloth = Canvas(self, bg="lavender", width=640, height=350)
        self.cloth.grid(row=0, column=0, columnspan=3)
        self.hello_button = Button(width=25, height=2, font=("Arial", 14), text="Начать тестирование",
                                   bg="thistle1", command=self.begin_testing)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.ask_button_one = Button(width=20, height=2, font=("Arial", 12), text="",
                                     bg="#FF8674", command=self.ask_one)
        self.ask_button_two = Button(width=20, height=2, font=("Arial", 12), text="",
                                     bg="#00B5E2", command=self.ask_two)
        self.ask_button_three = Button(width=20, height=2, font=("Arial", 12), text="",
                                       bg="#6CC24A", command=self.ask_three)
        self.ask_entry_var = StringVar()
        self.ask_entry = Entry(width=25, font=("Arial", 12), textvariable=self.ask_entry_var, justify=CENTER)
        self.ask_confirm_button = Button(width=25, height=1, font=("Arial", 12), text="Ответить",
                                         bg="green2", command=self.confirm_ask)

    def on_closing(self):
        if mb.askokcancel("Выход", "Выйти?"):
            print("Выход")
            self.run = False
            self.destroy()

    def hello(self):
        self.status.configure(text="Готов")
        self.cloth.delete("question")
        self.cloth.create_text(320, 175, text=QHeap.get_hello_message(), font=("Times New Roman", 27), tag="hello")
        self.hello_button.grid(row=1, column=1, pady=30)

    def clear_hello(self):
        self.cloth.delete("hello")
        self.hello_button.grid_forget()

    def compare_answer(self):
        if QHeap.player_answer == QHeap.get_answer(self.question_number):
            QHeap.score += 1
            print("Правильно")
        else:
            print("Ошибка")
        self.testing_initiator()

    def confirm_ask(self, gtype="Entry", answer=""):
        x = 0
        while x == 0:
            if gtype == "Entry":
                try:
                    QHeap.player_answer = int(self.ask_entry_var.get())
                except ValueError:
                    mb.showerror(title="Ошибка", message="Введите натуральное число")
                    self.test_question()
                    break
            else:
                QHeap.player_answer = answer
            self.compare_answer()
            x = 1

    def begin_testing(self):
        self.clear_hello()
        self.testing_initiator()

    def result(self):
        output = "Вы завершили тестирование. \n" \
                 "Ваш результат: %i/%i очков" % (QHeap.score, QHeap.get_question_amount())
        mb.showinfo(title="Итоги", message=output)
        QHeap.score = 0
        self.question_number = 0
        self.hello()

    def testing_initiator(self):
        self.clear_questions_area()
        self.question_number += 1
        self.ask_entry_var.set("")
        if self.question_number <= QHeap.get_question_amount():
            self.test_question()
        else:
            self.result()

    def test_question(self):
        self.status.configure(text="Вопрос %i/%i" % (self.question_number, QHeap.get_question_amount()))
        if QHeap.get_type(self.question_number) == "Entry":
            self.create_entry_question(QHeap.get_question(self.question_number))
        elif QHeap.get_type(self.question_number) == "Button":
            self.create_button_question(QHeap.get_question(self.question_number))

    def clear_questions_area(self):
        self.ask_entry.grid_forget()
        self.ask_confirm_button.grid_forget()
        self.ask_button_one.grid_forget()
        self.ask_button_two.grid_forget()
        self.ask_button_three.grid_forget()
        self.cloth.delete("question")

    def create_entry_question(self, question):
        self.cloth.create_text(320, 175, text=question, font=("Times New Roman", 27), tag="question", justify=CENTER)
        self.ask_entry.grid(row=1, column=1, pady=25)
        self.ask_confirm_button.grid(row=2, column=1)

    def create_button_question(self, question):
        self.cloth.create_text(320, 175, text=question, font=("Times New Roman", 27), tag="question", justify=CENTER)
        self.ask_button_one.configure(text=QHeap.get_options(self.question_number)[0])
        self.ask_button_two.configure(text=QHeap.get_options(self.question_number)[1])
        self.ask_button_three.configure(text=QHeap.get_options(self.question_number)[2])
        self.ask_button_one.grid(row=1, column=0, pady=30)
        self.ask_button_two.grid(row=1, column=1, pady=30)
        self.ask_button_three.grid(row=1, column=2, pady=30)

    def ask_one(self):
        self.confirm_ask(gtype="Button", answer=QHeap.get_options(self.question_number)[0])

    def ask_two(self):
        self.confirm_ask(gtype="Button", answer=QHeap.get_options(self.question_number)[1])

    def ask_three(self):
        self.confirm_ask(gtype="Button", answer=QHeap.get_options(self.question_number)[2])
