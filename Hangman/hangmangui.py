import tkinter as tk
from hangman import Hangman

hm = Hangman()
def newGame():
    hm.reset()
    lblWord.set(hm.printWord())
    resultText.set('')
    guessesText.set('')
    guessEl.config(state= "normal")

def guess(ev):
    letter = guessEl.get()
    guessEl.delete(0, tk.END)
    resultText.set(hm.checkLetter(letter))
    lblWord.set(hm.printWord())
    guessesText.set(', '.join(hm.guessed_letters))
    if hm.guessed_word():
        resultText.set('Congratulations, you guessed "{}" correctly! Press "New Game" to start again!'.format(hm.curWord.capitalize()))
        guessEl.config(state= "disabled")
    if hm.wrongGuesses > hm.max_wrong_guesses:
        guessEl.config(state= "disabled")
        resultText.set('Out of guesses! The word was "{}". Press "New Game" to start again! '.format(hm.curWord.capitalize()))

gui = tk.Tk()
gui.title('Hangman')
gui.geometry("1000x500")
tk.Label(gui, text="Guess").grid(row=0)
resultText = tk.StringVar()
tk.Label(gui, textvariable=resultText).grid(row=2)
guessesText = tk.StringVar()
tk.Label(gui, textvariable=guessesText).grid(row=3)
guessEl = tk.Entry(gui)
guessEl.grid(row=0, column=1)
guessEl.bind('<Return>', guess)


lblWord = tk.StringVar()
tk.Label(gui, textvariable=lblWord,font=('consolas 24 bold')).grid(row=0, column=3 ,columnspan=6,padx=10)
tk.Button(gui, text="New\nGame", command=lambda:newGame(), font=("Helvetica 10 bold")).grid(row=3, column=8)

newGame()
gui.mainloop()