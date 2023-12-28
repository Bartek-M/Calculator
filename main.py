import tkinter as tk
import base64
import tkinter.font as font
from tkinter import colorchooser

dict1 = {} # Brackets
dict2 = {} # Equal to
dict3 = {} # Symbol
dict4 = {} # Color Choose

try:
    file = open("file.txt", "r")
    f = file.readlines()
    my_list = []
    for line in f:
        my_list.append(line.strip())
    for i in range(len(my_list)):
        b = my_list[i]
        b = b.encode("UTF-8")
        b = base64.b64decode(b)
        b = b.decode("UTF-8")
        my_list[i] = b
        if len(my_list[i]) != 7:
            raise
    if len(my_list) != 26:
        raise

    with open("file1.txt", "r") as f:
        my_listf = [line.strip() for line in f.readlines()]
        
    for i in range(len(my_listf)):
        b = my_listf[i]
        b = b.encode("UTF-8")
        b = base64.b64decode(b)
        b = b.decode("UTF-8")
        my_listf[i] = b
        if len(my_listf[i]) != 7:
            raise
    if len(my_listf) != 26:
        raise

except:
    my_list = [
        "#000000","#000000","#000000","#000000","#000000","#000000","#000000","#000000","#000000", "#000000","#000000","#000000", "#202020", "#202020", "#202020", "#202020", "#202020", "#202020", "#202020", "#202020", "#202020", "#202020", "#202020", "#202020", "#353838", "#004080"
    ]

    f = open("file.txt", "a")
    f.truncate(0)
    for i in range(len(my_list)):
        str = my_list[i]
        b = str.encode("UTF-8")
        b = base64.b64encode(b)
        b = b.decode("UTF-8")
        f.write(b + "\n")
    f.close()

    my_listf = [
        "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"
    ]
    f1 = open("file1.txt", "a")
    f1.truncate(0)
    for i in range(len(my_list)):
        str = my_listf[i]
        b = str.encode("UTF-8")
        b = base64.b64encode(b)
        b = b.decode("UTF-8")
        f1.write(b + "\n")
    f1.close()


class Test(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgett()
        
    def create_widgett(self):
        self.myFont1 = font.Font(size=12)
        self.myFontt1 = font.Font(size=28)
        self.myFontt2 = font.Font(size=10)

        a = 2
        b = 6
        c = 7

        self.grid(column=0, sticky="NESW")
        self.grid(column=1, sticky="NESW")
        self.grid(column=2, sticky="NESW")
        self.grid(column=3, sticky="NESW")

        self.columnconfigure(0, pad=2)
        self.columnconfigure(1, pad=2)
        self.columnconfigure(2, pad=2)
        self.columnconfigure(3, pad=2)

        self.rowconfigure(2, pad=2)
        self.rowconfigure(3, pad=2)
        self.rowconfigure(4, pad=2)
        self.rowconfigure(5, pad=2)
        self.rowconfigure(6, pad=2)
        self.rowconfigure(7, pad=2)

        self.text = tk.Label(self, text="0", height=2, width=12, bg=my_list[24], fg=my_listf[24], anchor="e")
        self.text.grid(row=1, columnspan=4, sticky="")
        self.text["font"] = self.myFontt1

        self.text2 = tk.Label(self, text="", height=1, width=33, bg=my_list[24], fg=my_listf[24], anchor="e")
        self.text2.grid(row=0, columnspan=4, sticky="")
        self.text2["font"] = self.myFontt2

        self.btnN = tk.Button(self, text="( )", font=self.myFont1, height=a, width=b, bg=my_list[10], fg=my_listf[10], command=lambda: self.click("( )")).grid(row=7, column=0, sticky="")
        self.btn0 = tk.Button(self, text="0", font=self.myFont1, height=a, width=b, bg=my_list[0], fg=my_listf[0], command=lambda: self.click("0")).grid(row=7, column=1, sticky="")
        self.btnK = tk.Button(self, text=".", font=self.myFont1, height=a, width=b, bg=my_list[11], fg=my_listf[11], command=lambda: self.click(".")).grid(row=7, column=2, sticky="")

        self.btn1 = tk.Button(self, text="1", font=self.myFont1, height=a, width=b, bg=my_list[1], fg=my_listf[1], command=lambda: self.click("1")).grid(row=6, column=0, sticky="")
        self.btn2 = tk.Button(self, text="2", font=self.myFont1, height=a, width=b, bg=my_list[2], fg=my_listf[2], command=lambda: self.click("2")).grid(row=6, column=1, sticky="")
        self.btn3 = tk.Button(self, text="3", font=self.myFont1, height=a, width=b, bg=my_list[3], fg=my_listf[3], command=lambda: self.click("3")).grid(row=6, column=2, sticky="")

        self.btn4 = tk.Button(self, text="4", font=self.myFont1, height=a, width=b, bg=my_list[4], fg=my_listf[4], command=lambda: self.click("4")).grid(row=5, column=0, sticky="")
        self.btn5 = tk.Button(self, text="5", font=self.myFont1, height=a, width=b, bg=my_list[5], fg=my_listf[5], command=lambda: self.click("5")).grid(row=5, column=1, sticky="")
        self.btn6 = tk.Button(self, text="6", font=self.myFont1, height=a, width=b, bg=my_list[6], fg=my_listf[6], command=lambda: self.click("6")).grid(row=5, column=2, sticky="")

        self.btn7 = tk.Button(self, text="7", font=self.myFont1, height=a, width=b, bg=my_list[7], fg=my_listf[7], command=lambda: self.click("7")).grid(row=4, column=0, sticky="")
        self.btn8 = tk.Button(self, text="8", font=self.myFont1, height=a, width=b, bg=my_list[8], fg=my_listf[8], command=lambda: self.click("8")).grid(row=4, column=1, sticky="")
        self.btn9 = tk.Button(self, text="9", font=self.myFont1, height=a, width=b, bg=my_list[9], fg=my_listf[9], command=lambda: self.click("9")).grid(row=4, column=2, sticky="")

        self.btnPR = tk.Button(self, text="%", font=self.myFont1, height=a, width=b, bg=my_list[12], fg=my_listf[12], command=lambda: self.click(" % ")).grid(row=3, column=0, sticky="")
        self.btnM2 = tk.Button(self, text="x"u"\u00B2", font=self.myFont1, height=a, width=b, bg=my_list[13], fg=my_listf[13], command=lambda: self.click(u"\u00B2")).grid(row=3, column=1, sticky="")
        self.btnMY = tk.Button(self, text="xʸ", font=self.myFont1, height=a, width=b, bg=my_list[14], fg=my_listf[14], command=lambda: self.click(" ^ ")).grid(row=3, column=2, sticky="")

        self.btnAC = tk.Button(self, text="AC", font=self.myFont1, height=a, width=b, bg=my_list[20], fg=my_listf[20], command=lambda: self.click(" ")).grid(row=2, column=0, sticky="")
        self.btnPR = tk.Button(self, text="√", font=self.myFont1, height=a, width=b, bg=my_list[21], fg=my_listf[21], command=lambda: self.click("√ ")).grid(row=2, column=1, sticky="")
        self.btnPI = tk.Button(self, text="π", font=self.myFont1, height=a, width=b, bg=my_list[22], fg=my_listf[22], command=lambda: self.click("3.14")).grid(row=2, column=2, sticky="")

        self.btnP = tk.Button(self, text="+", font=self.myFont1, height=a, width=c, bg=my_list[15], fg=my_listf[15], command=lambda: self.click(" + ")).grid(row=6, column=3, sticky="")
        self.btnE = tk.Button(self, text="=", font=self.myFont1, height=a, width=c, bg=my_list[25], fg=my_listf[25], command=lambda: self.click("=")).grid(row=7, column=3, sticky="")
        self.btnM = tk.Button(self, text="-", font=self.myFont1, height=a, width=c, bg=my_list[16], fg=my_listf[16], command=lambda: self.click(" - ")).grid(row=5, column=3, sticky="")
        self.btnX = tk.Button(self, text="x", font=self.myFont1, height=a, width=c, bg=my_list[17], fg=my_listf[17], command=lambda: self.click(" * ")).grid(row=4, column=3, sticky="")
        self.btnC = tk.Button(self, text=u"\u232B", font=self.myFont1, height=a, width=c, bg=my_list[18], fg=my_listf[18], command=lambda: self.click("B")).grid(row=2, column=3, sticky="")
        self.btnD = tk.Button(self, text="/", font=self.myFont1, height=a, width=c, bg=my_list[19], fg=my_listf[19], command=lambda: self.click(" / ")).grid(row=3, column=3, sticky="")


    def enterdown(self, e):    
        self.click("=")
    
    def backsdown(self, e):
        self.backspace()
    
    def keyup(self, e):
        if e.char == "1":
            self.click("1")
        elif e.char == "2":
            self.click("2")
        elif e.char == "3":
            self.click("3")
        elif e.char == "4":
            self.click("4")
        elif e.char == "5":
            self.click("5")
        elif e.char == "6":
            self.click("6")
        elif e.char == "7":
            self.click("7")
        elif e.char == "8":
            self.click("8")
        elif e.char == "9":
            self.click("9")
        elif e.char == "0":
            self.click("0")
        elif e.char == "=":
            self.click("=")
        elif e.char == "+":
            self.click(" + ")
        elif e.char == "-":
            self.click(" - ")
        elif e.char == "*":
            self.click(" * ")
        elif e.char =="/":
            self.click(" / ")
        elif e.char == "%":
            self.click(" % ")
        elif e.char == ".":
            self.click(".")
        elif e.char == "^":
            self.click(" ^ ")
        elif e.char == ",":
            self.click(".")
        elif e.char == "y":
            self.click(" ^ ")
        elif e.char == "p":
            self.click("3.14")
        elif e.char == "c":
            if "c" in dict4:
                del dict4["c"]
            if "a" in dict4:
                del dict4["a"]
                self.text["text"] = "0"
            else:
                self.text["text"] = "ColorSetup"
                dict4["a"] = "b"

        if "a" in dict4:
            if e.char == "t":
                self.click("l")
            if e.char == "d":
                global my_list, my_listf
                my_listD = ["#000000","#000000","#000000","#000000","#000000","#000000","#000000","#000000","#000000",
                "#000000","#000000","#000000", "#202020", "#202020", "#202020", "#202020", "#202020", "#202020", "#202020", "#202020", 
                "#202020", "#202020", "#202020", "#202020", "#353838", "#004080"]
                my_list = my_listD
                f = open("file.txt", "a")
                f.truncate(0)
                for i in range(len(my_listD)):
                    str = my_listD[i]
                    b = str.encode("UTF-8")
                    b = base64.b64encode(b)
                    b = b.decode("UTF-8")
                    f.write(b + "\n")
                f.close()

                my_listfD = ["#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", 
                "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF", "#FFFFFF"]
                my_listf = my_listfD
                f1 = open("file1.txt", "a")
                f1.truncate(0)
                for i in range(len(my_listfD)):
                    str = my_listfD[i]
                    b = str.encode("UTF-8")
                    b = base64.b64encode(b)
                    b = b.decode("UTF-8")
                    f1.write(b + "\n")
                f1.close()

                self.create_widgett()
                self.text["text"] = "ColorSetup"

            if e.char == "f": 
                if "c" in dict4:
                    del dict4["c"]
                    self.text["text"] = "ColorSetup"
                else:
                    self.text["text"] = "FontColorSetup"
                    dict4["c"] = "b"
        
    
    def delete(self, e):
        self.AC()
    
    def brack(self, e):
        self.click("( )")

    def AC(self):
        self.text["text"] = "0"
        self.text2["text"] = ""
        if "a" in dict1:
            del dict1["a"] 
        if "a" in dict2:
            del dict2["a"]
        if "a" in dict3:
            del dict3["a"]

    def equal_to(self):
        self.text2["text"] = f"{self.text['text']} ="

        try:
            expr = self.text["text"].replace(u"\u00B2", "**2").replace(" % ", "/100").replace(" ^ ", "**").replace("√ ", "**0.5")
            self.text["text"] = str(round(eval(expr), 4))
        except (ZeroDivisionError, SyntaxError, TypeError, IndexError, UnboundLocalError):
            self.text["text"] = "ERROR"
        
        dict2["a"] = "b"

    def backspace(self):
        x = "+", "-", "*", u"\u00B2", "/", "%", "^", "√", "."
        l1 = self.text["text"]
        l2 = l1.replace(" ", "")
        l3 = l2[:-1] 
        length = len(l2)
        last_char = l2[length -1]
        self.text["text"] = l3.replace("+", " + ").replace("*", " * ").replace("-", " - ").replace("/", " / ").replace("^", " ^ ").replace("√", "√ ")
        if self.text["text"] == "": #Never blank label text
            self.text["text"] = "0"
            self.text2["text"] = ""
        if last_char in x:
            if "a" in dict3: 
                del dict3["a"]
        elif last_char == "(":
            if "a" in dict1:
                del dict1["a"]
        elif last_char == ")":
            dict1["a"] = "b"

    def change(self, btn_id):
        x = "+", "-", "*", "/", "%", "."
        X = " + ", " - ", " * ", " / ", " % ", "."
        l1 = self.text["text"]
        l2 = l1.replace(" ", "")
        l3 = l2[:-1]
        length = len(l2)
        last_char = l2[length -1]
        if last_char in x:
            if btn_id in X:
                self.text["text"] = l3.replace("+", " + ").replace("*", " * ").replace("-", " - ").replace("/", " / ").replace("%", "% ")
                self.text["text"] += btn_id
        elif last_char == u"\u00B2":
            if btn_id in X:
                self.text["text"] += btn_id
            else:
                return
        else:
            self.text["text"] += btn_id

    def click(self, btn_id):
        if "a" in dict4:
            global my_list, my_listf
            if btn_id == "3.14":
                btn_id = "22"
            btn_id = btn_id.replace("( )", "10").replace(".", "11").replace("l", "24").replace(" % ", "12").replace("√ ", "21").replace(u"\u00B2", "13").replace(" ^ ", "14").replace(" + ", "15").replace("=", "25").replace(" - ", "16").replace(" * ", "17").replace("B", "18").replace(" / ", "19").replace(" ", "20").replace("t", "21")
            if "c" in dict4:
                self.text["text"] = "FontColorSetup"
                try:
                    my_color = colorchooser.askcolor()
                    my_color = my_color[1].strip()
                    del my_listf[int(btn_id)]
                    my_listf.insert(int(btn_id), my_color)
                    self.create_widgett()
                    self.text["text"] = "FontColorSetup"
                except AttributeError:
                    return
            else:
                self.text["text"] = "ColorSetup"
                try:
                    my_color = colorchooser.askcolor()
                    my_color = my_color[1].strip()
                    del my_list[int(btn_id)]
                    my_list.insert(int(btn_id), my_color)
                    self.create_widgett()
                    self.text["text"] = "ColorSetup"
                except AttributeError:
                    return
                
                
            f = open("file.txt", "a")
            f.truncate(0)
            for i in range(len(my_list)):
                str = my_list[i]
                b = str.encode("UTF-8")
                b = base64.b64encode(b)
                b = b.decode("UTF-8")
                f.write(b + "\n")
            f.close()
                
            f1 = open("file1.txt", "a")
            f1.truncate(0)
            for i in range(len(my_listf)):
                str = my_listf[i]
                b = str.encode("UTF-8")
                b = base64.b64encode(b)
                b = b.decode("UTF-8")
                f1.write(b + "\n")
            f1.close()

        else:
            if btn_id == " ": #All Clear
                self.AC()
                
            elif btn_id == "=": #Equal To
                self.equal_to()
                
            elif btn_id == "B": #BackSpace 
                self.backspace()

            elif btn_id == "( )":
                x = "+", "-", "*", u"\u00B2", "/", "%", "^"
                if "a" in dict1:
                    self.text["text"] += ")"
                    if "a" in dict1:
                        del dict1["a"]
                else:
                    if self.text["text"] == "0":
                        self.text["text"] = "("
                    else:       
                        l1 = self.text["text"]
                        l2 = l1.replace(" ", "")
                        length = len(l2)
                        last_char = l2[length -1]
                        if last_char in x:
                            self.text["text"] += "("
                        else:
                            self.text["text"] += " * ("
                    dict1["a"] = "b"
                    if "a" in dict2:
                        del dict2["a"]
                    
            else: #Text 
                x = " * ", u"\u00B2", " / ", " % ", ".", " ^ ", "√ ", " + ", " - "
                if self.text["text"] == "0": # If zero +=
                    if btn_id == ".":
                        self.text["text"] += btn_id
                    elif btn_id in x:
                        return
                    else:
                        self.text["text"] = btn_id
        
                elif "a" in dict2: #if equal to +=
                    if btn_id in x:
                        self.text["text"] += btn_id
                        if "a" in dict2:
                            del dict2["a"]
                    else:
                        self.text["text"] = btn_id
                        if "a" in dict2:
                            del dict2["a"]
                else:
                    if btn_id in x:
                        self.change(btn_id)
                    else:
                        x = "+", "-", "*", u"\u00B2", "/", "%", "^", ".", "√"
                        l1 = self.text["text"]
                        l2 = l1.replace(" ", "")
                        length = len(l2)
                        last_char = l2[length -1]
                        if last_char in x:
                            self.text["text"] += btn_id
                        elif last_char == ")":
                            if btn_id not in x:
                                self.text["text"] += " * " + btn_id
                            else:
                                self.text["text"] += btn_id
                        else:
                            self.text["text"] += btn_id
                        if "a" in dict3:
                            del dict3["a"]

root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)
root.iconbitmap("favicon.ico")

run = Test(master=root)
run.configure(bg="black")
run.bind("<Delete>", run.delete)
run.bind("<(>", run.brack)
run.bind("<)>", run.brack)
run.bind("<KeyPress>", run.keyup)
run.bind("<BackSpace>", run.backsdown)
run.bind("<Return>", run.enterdown)
run.focus_set()
run.mainloop()