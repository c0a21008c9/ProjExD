import tkinter as tk
import tkinter.messagebox as tkm


def button_click(event):
    btn = event.widget
    num=btn["text"]
    if num=="=":
        eqn=entry.get()
        res=eval(eqn)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    else:
        entry.insert(tk.END,num)


    #tkm.showinfo("",f"{num}のボタンがクリックされました")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓")
    root.geometry("300x600")

    entry= tk.Entry(root,  justify="right",width=10,font=("Times New Roman",40))
    entry.grid(row=0, column=0, columnspan=3)

    r,c=1,0
    for i,num in enumerate([i for i in range(9,-1,-1)]+["+","="]):
        btn = tk.Button(root, text=f"{num}", width=4, height=2,font=("Times New Roman",30))
        btn.bind("<1>",button_click)
        btn.grid(row=r,column=c)
        c+=1
        if (i+1)%3 ==0:
            r+=1
            c=0
    root.mainloop()