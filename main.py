import json
import tkinter as tk
import tkinter.font as font
from tkinter import colorchooser

dict1 = {}  # Brackets
dict2 = {}  # Equal to
dict3 = {}  # Symbol
dict4 = {}  # Color Choose


class Calculator(tk.Frame):
    BG_DEFAULT = [
        "#101010",
        "#101010",
        "#101010",
        "#101010",
        "#101010",
        "#101010",
        "#101010",
        "#101010",
        "#101010",
        "#101010",
        "#101010",
        "#101010",
        "#202020",
        "#202020",
        "#202020",
        "#202020",
        "#202020",
        "#202020",
        "#202020",
        "#202020",
        "#202020",
        "#202020",
        "#202020",
        "#202020",
        "#353838",
        "#004080",
    ]
    FG_DEFAULT = [
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
        "#FFFFFF",
    ]

    def __init__(self, master):
        super().__init__(master)
        self.colors = self.load_colors()

        self.grid()
        self.create_widget()

    def load_colors(self, reset: bool = False) -> dict:
        colors = {"bg": self.BG_DEFAULT, "fg": self.FG_DEFAULT}

        try:
            if reset:
                raise

            with open("./config.json", "r", encoding="UTF-8") as f:
                data = json.load(f)

            if not data.get("bg") or not data.get("fg"):
                raise
            if len(data["bg"]) != len(self.BG_DEFAULT) or len(data["fg"]) != len(self.FG_DEFAULT):
                raise
            if [c for c in data["bg"] if len(c) != 7] or [c for c in data["fg"] if len(c) != 7]:
                raise

            return data
        except:
            with open("./config.json", "w", encoding="UTF-8") as f:
                json.dump(colors, f)

        return colors

    def create_widget(self):
        FONT_S = font.Font(size=10)
        FONT_M = font.Font(size=12)
        FONT_L = font.Font(size=28)

        a = 2
        b = 6
        c = 7

        self.grid(column=0, sticky="NESW")
        self.grid(column=1, sticky="NESW")
        self.grid(column=2, sticky="NESW")
        self.grid(column=3, sticky="NESW")

        self.columnconfigure(0, pad=1)
        self.columnconfigure(1, pad=1)
        self.columnconfigure(2, pad=1)
        self.columnconfigure(3)

        self.rowconfigure(2, pad=1)
        self.rowconfigure(3, pad=1)
        self.rowconfigure(4, pad=1)
        self.rowconfigure(5, pad=1)
        self.rowconfigure(6, pad=1)
        self.rowconfigure(7)

        self.text = tk.Label(self, text="0", height=2, bg=self.colors["bg"][24], fg=self.colors["fg"][24], anchor="e")
        self.text.grid(row=1, columnspan=4, sticky="we")
        self.text["font"] = FONT_L

        self.text2 = tk.Label(self, text="", height=1, bg=self.colors["bg"][24], fg=self.colors["fg"][24], anchor="e")
        self.text2.grid(row=0, columnspan=4, sticky="we")
        self.text2["font"] = FONT_S

        self.btnN = tk.Button(
            self,
            text="( )",
            font=FONT_M, bd=0,
            height=a,
            width=b,
            bg=self.colors["bg"][10],
            fg=self.colors["fg"][10],
            command=lambda: self.click("( )"),
        ).grid(row=7, column=0, sticky="")
        self.btn0 = tk.Button(
            self,
            text="0",
            font=FONT_M, bd=0,
            height=a,
            width=b,
            bg=self.colors["bg"][0],
            fg=self.colors["fg"][0],
            command=lambda: self.click("0"),
        ).grid(row=7, column=1, sticky="")
        self.btnK = tk.Button(
            self,
            text=".",
            font=FONT_M, bd=0,
            height=a,
            width=b,
            bg=self.colors["bg"][11],
            fg=self.colors["fg"][11],
            command=lambda: self.click("."),
        ).grid(row=7, column=2, sticky="")

        self.btn1 = tk.Button(
            self,
            text="1",
            font=FONT_M, bd=0,
            height=a,
            width=b,
            bg=self.colors["bg"][1],
            fg=self.colors["fg"][1],
            command=lambda: self.click("1"),
        ).grid(row=6, column=0, sticky="")
        self.btn2 = tk.Button(
            self,
            text="2",
            font=FONT_M, bd=0,
            height=a,
            width=b,
            bg=self.colors["bg"][2],
            fg=self.colors["fg"][2],
            command=lambda: self.click("2"),
        ).grid(row=6, column=1, sticky="")
        self.btn3 = tk.Button(
            self,
            text="3",
            font=FONT_M, bd=0,
            height=a,
            width=b,
            bg=self.colors["bg"][3],
            fg=self.colors["fg"][3],
            command=lambda: self.click("3"),
        ).grid(row=6, column=2, sticky="")

        self.btn4 = tk.Button(
            self,
            text="4",
            font=FONT_M, bd=0,
            height=a,
            width=b,
            bg=self.colors["bg"][4],
            fg=self.colors["fg"][4],
            command=lambda: self.click("4"),
        ).grid(row=5, column=0, sticky="")
        self.btn5 = tk.Button(
            self,
            text="5",
            font=FONT_M, bd=0,
            height=a,
            width=b,
            bg=self.colors["bg"][5],
            fg=self.colors["fg"][5],
            command=lambda: self.click("5"),
        ).grid(row=5, column=1, sticky="")
        self.btn6 = tk.Button(
            self,
            text="6",
            font=FONT_M, bd=0,
            height=a,
            width=b,
            bg=self.colors["bg"][6],
            fg=self.colors["fg"][6],
            command=lambda: self.click("6"),
        ).grid(row=5, column=2, sticky="")

        self.btn7 = tk.Button(
            self,
            text="7",
            font=FONT_M, bd=0,
            height=a,
            width=b,
            bg=self.colors["bg"][7],
            fg=self.colors["fg"][7],
            command=lambda: self.click("7"),
        ).grid(row=4, column=0, sticky="")
        self.btn8 = tk.Button(
            self,
            text="8",
            font=FONT_M, bd=0,
            height=a,
            width=b,
            bg=self.colors["bg"][8],
            fg=self.colors["fg"][8],
            command=lambda: self.click("8"),
        ).grid(row=4, column=1, sticky="")
        self.btn9 = tk.Button(
            self,
            text="9",
            font=FONT_M, bd=0,
            height=a,
            width=b,
            bg=self.colors["bg"][9],
            fg=self.colors["fg"][9],
            command=lambda: self.click("9"),
        ).grid(row=4, column=2, sticky="")

        self.btnPR = tk.Button(
            self,
            text="%",
            font=FONT_M, bd=0,
            height=a,
            width=b,
            bg=self.colors["bg"][12],
            fg=self.colors["fg"][12],
            command=lambda: self.click(" % "),
        ).grid(row=3, column=0, sticky="")
        self.btnM2 = tk.Button(
            self,
            text="x" "\u00B2",
            font=FONT_M, bd=0,
            height=a,
            width=b,
            bg=self.colors["bg"][13],
            fg=self.colors["fg"][13],
            command=lambda: self.click("\u00B2"),
        ).grid(row=3, column=1, sticky="")
        self.btnMY = tk.Button(
            self,
            text="xʸ",
            font=FONT_M, bd=0,
            height=a,
            width=b,
            bg=self.colors["bg"][14],
            fg=self.colors["fg"][14],
            command=lambda: self.click(" ^ "),
        ).grid(row=3, column=2, sticky="")

        self.btnAC = tk.Button(
            self,
            text="AC",
            font=FONT_M, bd=0,
            height=a,
            width=b,
            bg=self.colors["bg"][20],
            fg=self.colors["fg"][20],
            command=lambda: self.click(" "),
        ).grid(row=2, column=0, sticky="")
        self.btnPR = tk.Button(
            self,
            text="√",
            font=FONT_M, bd=0,
            height=a,
            width=b,
            bg=self.colors["bg"][21],
            fg=self.colors["fg"][21],
            command=lambda: self.click("√ "),
        ).grid(row=2, column=1, sticky="")
        self.btnPI = tk.Button(
            self,
            text="π",
            font=FONT_M, bd=0,
            height=a,
            width=b,
            bg=self.colors["bg"][22],
            fg=self.colors["fg"][22],
            command=lambda: self.click("3.14"),
        ).grid(row=2, column=2, sticky="")

        self.btnP = tk.Button(
            self,
            text="+",
            font=FONT_M, bd=0,
            height=a,
            width=c,
            bg=self.colors["bg"][15],
            fg=self.colors["fg"][15],
            command=lambda: self.click(" + "),
        ).grid(row=6, column=3, sticky="")
        self.btnE = tk.Button(
            self,
            text="=",
            font=FONT_M, bd=0,
            height=a,
            width=c,
            bg=self.colors["bg"][25],
            fg=self.colors["fg"][25],
            command=lambda: self.click("="),
        ).grid(row=7, column=3, sticky="")
        self.btnM = tk.Button(
            self,
            text="-",
            font=FONT_M, bd=0,
            height=a,
            width=c,
            bg=self.colors["bg"][16],
            fg=self.colors["fg"][16],
            command=lambda: self.click(" - "),
        ).grid(row=5, column=3, sticky="")
        self.btnX = tk.Button(
            self,
            text="x",
            font=FONT_M, bd=0,
            height=a,
            width=c,
            bg=self.colors["bg"][17],
            fg=self.colors["fg"][17],
            command=lambda: self.click(" * "),
        ).grid(row=4, column=3, sticky="")
        self.btnC = tk.Button(
            self,
            text="\u232B",
            font=FONT_M, bd=0,
            height=a,
            width=c,
            bg=self.colors["bg"][18],
            fg=self.colors["fg"][18],
            command=lambda: self.click("B"),
        ).grid(row=2, column=3, sticky="")
        self.btnD = tk.Button(
            self,
            text="/",
            font=FONT_M, bd=0,
            height=a,
            width=c,
            bg=self.colors["bg"][19],
            fg=self.colors["fg"][19],
            command=lambda: self.click(" / "),
        ).grid(row=3, column=3, sticky="")

    def enter_down(self, _):
        self.click("=")

    def backspace_down(self, _):
        self.backspace()

    def key_up(self, e):
        char = e.char

        if char in ["+", "-", "*", "/", "%", "^"]:
            char = f" {char} "
        elif char == "y":
            char = " ^ "
        elif char == "p":
            char = "3.14"

        self.click(char)

        if e.char == "c":
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
                self.colors = {"bg": BG_DEFAULT, "fg": FG_DEFAULT}

                with open("./config.json", "w", encoding="UTF-8") as f:
                    json.dump(self.colors, f)

                self.create_widget()
                self.text["text"] = "ColorSetup"

            if e.char == "f":
                if "c" in dict4:
                    del dict4["c"]
                    self.text["text"] = "ColorSetup"
                else:
                    self.text["text"] = "FontColorSetup"
                    dict4["c"] = "b"

    def delete(self, _):
        self.AC()

    def bracket(self, _):
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
            expr = self.text["text"].replace("\u00B2", "**2").replace(" % ", "/100").replace(" ^ ", "**").replace("√ ", "**0.5")
            self.text["text"] = str(round(eval(expr), 4))
        except (ZeroDivisionError, SyntaxError, TypeError, IndexError, UnboundLocalError):
            self.text["text"] = "ERROR"

        dict2["a"] = "b"

    def backspace(self):
        x = "+", "-", "*", "\u00B2", "/", "%", "^", "√", "."
        l1 = self.text["text"]
        l2 = l1.replace(" ", "")
        l3 = l2[:-1]
        length = len(l2)
        last_char = l2[length - 1]
        self.text["text"] = (
            l3.replace("+", " + ").replace("*", " * ").replace("-", " - ").replace("/", " / ").replace("^", " ^ ").replace("√", "√ ")
        )
        if self.text["text"] == "":  # Never blank label text
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
        last_char = l2[length - 1]
        if last_char in x:
            if btn_id in X:
                self.text["text"] = l3.replace("+", " + ").replace("*", " * ").replace("-", " - ").replace("/", " / ").replace("%", "% ")
                self.text["text"] += btn_id
        elif last_char == "\u00B2":
            if btn_id in X:
                self.text["text"] += btn_id
            else:
                return
        else:
            self.text["text"] += btn_id

    def click(self, btn_id):
        if "a" in dict4:
            if btn_id == "3.14":
                btn_id = "22"
            btn_id = (
                btn_id.replace("( )", "10")
                .replace(".", "11")
                .replace("l", "24")
                .replace(" % ", "12")
                .replace("√ ", "21")
                .replace("\u00B2", "13")
                .replace(" ^ ", "14")
                .replace(" + ", "15")
                .replace("=", "25")
                .replace(" - ", "16")
                .replace(" * ", "17")
                .replace("B", "18")
                .replace(" / ", "19")
                .replace(" ", "20")
                .replace("t", "21")
            )
            if "c" in dict4:
                self.text["text"] = "FontColorSetup"
                try:
                    my_color = colorchooser.askcolor()
                    my_color = my_color[1].strip()
                    # CHANGE COLOR LIST
                    self.create_widget()
                    self.text["text"] = "FontColorSetup"
                except AttributeError:
                    return
            else:
                self.text["text"] = "ColorSetup"
                try:
                    my_color = colorchooser.askcolor()
                    my_color = my_color[1].strip()
                    # CHANGE COLOR LIST
                    self.create_widget()
                    self.text["text"] = "ColorSetup"
                except AttributeError:
                    return

            # SAVE COLORS

        else:
            if btn_id == " ":  # All Clear
                self.AC()

            elif btn_id == "=":  # Equal To
                self.equal_to()

            elif btn_id == "B":  # BackSpace
                self.backspace()

            elif btn_id == "( )":
                x = "+", "-", "*", "\u00B2", "/", "%", "^"
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
                        last_char = l2[length - 1]
                        if last_char in x:
                            self.text["text"] += "("
                        else:
                            self.text["text"] += " * ("
                    dict1["a"] = "b"
                    if "a" in dict2:
                        del dict2["a"]

            else:  # Text
                x = " * ", "\u00B2", " / ", " % ", ".", " ^ ", "√ ", " + ", " - "
                if self.text["text"] == "0":  # If zero +=
                    if btn_id == ".":
                        self.text["text"] += btn_id
                    elif btn_id in x:
                        return
                    else:
                        self.text["text"] = btn_id

                elif "a" in dict2:  # if equal to +=
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
                        x = "+", "-", "*", "\u00B2", "/", "%", "^", ".", "√"
                        l1 = self.text["text"]
                        l2 = l1.replace(" ", "")
                        length = len(l2)
                        last_char = l2[length - 1]
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


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculator")
    root.resizable(False, False)
    root.iconbitmap("favicon.ico")

    calc = Calculator(master=root)
    calc.configure(bg="black")
    calc.bind("<Delete>", calc.delete)
    calc.bind("<(>", calc.bracket)
    calc.bind("<)>", calc.bracket)
    calc.bind("<KeyPress>", calc.key_up)
    calc.bind("<BackSpace>", calc.backspace_down)
    calc.bind("<Return>", calc.enter_down)
    calc.focus_set()
    calc.mainloop()
