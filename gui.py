from tkinter import *
from tracemalloc import start
from collections import Counter

# read all the 5 letter words to a list
words = []
with open('words.txt') as f:
    for line in f:
        words.append(line.strip())

letters = ""
notletters = ""
hints = []
possible_words = []
results = []
results1 = []
results2 = []
firstletter = ""
secondletter = ""
thirdletter = ""
fourthletter = ""
fifthletter = ""


def main(a, b, c, d, e, f, g):
    global hints, possible_words, letters, notletters, firstletter, secondletter, thirdletter, fourthletter, fifthletter
    letters = a
    notletters = b
    firstletter = c
    secondletter = d
    thirdletter = e
    fourthletter = f
    fifthletter = g

    for word in words:
        contains(word)
        notcontains(word)
    results = [i for i in results1 if i not in results2]
    possible_words = knownlocation(results)
    allchars = map(lambda x: list(x), results)
    flat_list = [item for sublist in allchars for item in sublist]
    hints = list(Counter(flat_list).most_common(10))
    return hints, possible_words


def contains(word):
    if all(elem in list(word) for elem in list(letters)):
        results1.append(str(word))


def notcontains(word):
    if any(elem in list(word) for elem in list(notletters)):
        results2.append(str(word))


def knownlocation(list):
    for word in list[:]:
        if(word[0] != firstletter and len(firstletter) > 0):
            list.remove(word)
        elif(word[1] != secondletter and len(secondletter) > 0):
            list.remove(word)
        elif(word[2] != thirdletter and len(thirdletter) > 0):
            list.remove(word)
        elif(word[3] != fourthletter and len(fourthletter) > 0):
            list.remove(word)
        elif(word[4] != fifthletter and len(fifthletter) > 0):
            list.remove(word)
    return list


def clicked():
    hints, words = main(e1.get(), e2.get(), e3.get(),
                        e4.get(), e5.get(), e6.get(), e7.get())
    T1.delete('1.0', END)
    T1.insert(END, hints)
    T2.delete('0.0', END)
    T2.insert(END, words)


root = Tk()
root.title("wordle hinter :)")
root.geometry('600x500')
root.resizable(width=0, height=0)

label = Label(root, text='contains:')
label.grid(row=0, column=0, padx=15, pady=5)
e1 = Entry(root, width=25, borderwidth=2)
e1.grid(row=0, column=1, padx=5, pady=5)

label = Label(root, text='not contains:')
label.grid(row=1, column=0, padx=15, pady=5)
e2 = Entry(root, width=25, borderwidth=2)
e2.grid(row=1, column=1, padx=5, pady=5)

label = Label(root, text='first letter:')
label.grid(row=2, column=0, padx=15, pady=5)
e3 = Entry(root, width=25, borderwidth=2)
e3.grid(row=2, column=1, padx=5, pady=5)

label = Label(root, text='second letter:')
label.grid(row=3, column=0, padx=15, pady=5)
e4 = Entry(root, width=25, borderwidth=2)
e4.grid(row=3, column=1, padx=5, pady=5)

label = Label(root, text='third letter:')
label.grid(row=4, column=0, padx=15, pady=5)
e5 = Entry(root, width=25, borderwidth=2)
e5.grid(row=4, column=1, padx=5, pady=5)

label = Label(root, text='fourth letter:')
label.grid(row=5, column=0, padx=15, pady=5)
e6 = Entry(root, width=25, borderwidth=2)
e6.grid(row=5, column=1, padx=5, pady=5)

label = Label(root, text='fifth letter:')
label.grid(row=6, column=0, padx=15, pady=5)
e7 = Entry(root, width=25, borderwidth=2)
e7.grid(row=6, column=1, padx=5, pady=5)

label8 = Label(root, text='hints:')
label8.grid(row=7, column=0, padx=15, pady=5)
T1 = Text(root, height=4, width=50)
T1.grid(row=7, column=1, padx=15, pady=5)

label9 = Label(root, text='possible words:')
label9.grid(row=8, column=0, padx=15, pady=5)
T2 = Text(root, height=4, width=50)
T2.grid(row=8, column=1, padx=15, pady=5)

button1 = Button(root, text="ok", padx=15, pady=0,
                 command=lambda: clicked())
button1.grid(row=9, column=1, padx=5, pady=5)

root.mainloop()
