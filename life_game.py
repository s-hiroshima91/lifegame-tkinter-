import tkinter as tk

root = tk.Tk()
f = tk.Frame(root)
f.grid()

N = 20
arry1 = [[0] * N for i in range(N)]

class life_game():
    def __init__(self , N , *arry1):
        self.n = N
        self.arry = arry1
        self.button_name = [ "button"+str(n) for n in range(N * N) ]

    def life(self):
        arry2 = [[0] * self.n for i in range(self.n)]
        for i in range(self.n) :
            for j in range(self.n) :
                count = 0
                for k in range(3) :
                    for t in range(3) :
                        if t == 1 and k == 1 :
                            flag = self.arry[i][j]
                        else :
                            count = count + self.arry[(i + k + self.n -1 )%self.n][(j + t + self.n - 1)%self.n]
                if flag == 1 and count == 2 :
                    arry2[i][j] = 1
                elif count == 3 :
                    arry2[i][j] = 1
                else :
                    arry2[i][j] = 0
        self.arry = arry2
        return arry2

    def btn(self):
        for i in range(self.n):
            for j in range(self.n):
                button_num = i + j * self.n
                if self.arry[i][j] == 1:
                    color = "red"
                else:
                    color = "gray"
                self.button_name[button_num].config(bg =color)

    def ipt(self , event):
        button_num = int(event.widget["text"])
        i = button_num % self.n
        j = button_num// self.n
        if self.arry[i][j] == 1:
            self.arry[i][j] = 0
            event.widget.config(bg = "gray")
        else:
            self.arry[i][j] = 1
            event.widget.config(bg = "red")

def stop_func():
    global after_id
    root.after_cancel(after_id)

def start_func(*arry1):
    global after_id
    lg.life()
    lg.btn()
    after_id = root.after(100, start_func, *arry1)
    return arry1

def exit_func():
    root.destroy()

lg = life_game(N , *arry1)

for i in range(N):
    for j in range(N):
        button_num = i + j * N
        lg.button_name[button_num] = tk.Button(f , text = button_num , bg = 'gray' , width = 1 , height = 1)
        lg.button_name[button_num].grid(column=i, row=j)
        lg.button_name[button_num].bind("<ButtonPress>", lg.ipt )

button_name = "stop"
button = tk.Button(f , text = button_name , command = stop_func)
button.grid(row=N, column = N//3, columnspan = N // 3)

button_name = "start"
button = tk.Button(f , text = button_name , command = lambda:start_func(*arry1))
button.grid(row=N, column = 0 , columnspan = N//3)

button_name = "exit"
button = tk.Button(f , text = button_name , command = exit_func)
button.grid(row=N, column = (N * 2) //3, columnspan = N // 3)

root.mainloop()
