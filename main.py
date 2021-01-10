"""This application was created for testing students.
You can create questions and include them in the application using questions.json file."""

import window

root = window.Root()


def begin():
    root.hello()
    while root.run:
        root.update_idletasks()
        root.update()


if __name__ == '__main__':
    begin()
