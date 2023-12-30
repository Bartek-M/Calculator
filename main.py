import json
import tkinter as tk
import tkinter.font as font
from tkinter import colorchooser


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

    HEIGHT = 2
    WIDTH = 6
    WIDTH_2 = 7

    SYMBOLS = {
        "( )": 10,
        ".": 11,
        "%": 12,
        "\u00B2": 13,
        "^": 14,
        "+": 15,
        "-": 16,
        "*": 17,
        "/": 18,
        "B": 19,
        "AC": 20,
        "√": 21,
        "t": 24,
        "=": 25,
    }

    def __init__(self, master):
        super().__init__(master)
        self.colors = self.load_colors()

        self.config = None  # None | "bg" | "fg"

        self.brackets = False
        self.equal = False

        self.grid()
        self.create_widget()

    def load_colors(self, colors={"bg": BG_DEFAULT, "fg": FG_DEFAULT}, set: bool = False) -> dict:
        try:
            if set:
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
        FONT_L = font.Font(size=24)

        DEFAULT_BTN = lambda x: {
            "font": FONT_M,
            "height": self.HEIGHT,
            "width": self.WIDTH,
            "bd": 0,
            "bg": self.colors["bg"][x],
            "fg": self.colors["fg"][x],
            "activebackground": self.colors["bg"][x],
            "activeforeground": self.colors["fg"][x],
            "cursor": "hand2",
        }

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

        self.label = tk.Label(self, text="0", font=FONT_L, height=self.HEIGHT, width=12, bg=self.colors["bg"][24], fg=self.colors["fg"][24], anchor="e")
        self.label.grid(row=1, columnspan=4, sticky="we")

        self.label_2 = tk.Label(self, text="", font=FONT_S, height=1, width=30, bg=self.colors["bg"][24], fg=self.colors["fg"][24], anchor="e")
        self.label_2.grid(row=0, columnspan=4, sticky="we")

        tk.Button(self, text="( )", **DEFAULT_BTN(10), command=lambda: self.click("( )")).grid(row=7, column=0)
        tk.Button(self, text="0", **DEFAULT_BTN(0), command=lambda: self.click("0")).grid(row=7, column=1)
        tk.Button(self, text=".", **DEFAULT_BTN(11), command=lambda: self.click(".")).grid(row=7, column=2)

        tk.Button(self, text="1", **DEFAULT_BTN(1), command=lambda: self.click("1")).grid(row=6, column=0)
        tk.Button(self, text="2", **DEFAULT_BTN(2), command=lambda: self.click("2")).grid(row=6, column=1)
        tk.Button(self, text="3", **DEFAULT_BTN(3), command=lambda: self.click("3")).grid(row=6, column=2)

        tk.Button(self, text="4", **DEFAULT_BTN(4), command=lambda: self.click("4")).grid(row=5, column=0)
        tk.Button(self, text="5", **DEFAULT_BTN(5), command=lambda: self.click("5")).grid(row=5, column=1)
        tk.Button(self, text="6", **DEFAULT_BTN(6), command=lambda: self.click("6")).grid(row=5, column=2)

        tk.Button(self, text="7", **DEFAULT_BTN(7), command=lambda: self.click("7")).grid(row=4, column=0)
        tk.Button(self, text="8", **DEFAULT_BTN(8), command=lambda: self.click("8")).grid(row=4, column=1)
        tk.Button(self, text="9", **DEFAULT_BTN(9), command=lambda: self.click("9")).grid(row=4, column=2)

        tk.Button(self, text="%", **DEFAULT_BTN(12), command=lambda: self.click(" % ")).grid(row=3, column=0)
        tk.Button(self, text="x" "\u00B2", **DEFAULT_BTN(13), command=lambda: self.click("\u00B2 ")).grid(row=3, column=1)
        tk.Button(self, text="xʸ", **DEFAULT_BTN(14), command=lambda: self.click(" ^ ")).grid(row=3, column=2)

        tk.Button(self, text="AC", **DEFAULT_BTN(20), command=lambda: self.click("AC")).grid(row=2, column=0)
        tk.Button(self, text="√", **DEFAULT_BTN(21), command=lambda: self.click("√ ")).grid(row=2, column=1)
        tk.Button(self, text="π", **DEFAULT_BTN(22), command=lambda: self.click("3.14")).grid(row=2, column=2)

        tk.Button(self, text="=", **DEFAULT_BTN(25) | {"width": self.WIDTH_2}, command=lambda: self.click("=")).grid(row=7, column=3)
        tk.Button(self, text="+", **DEFAULT_BTN(15) | {"width": self.WIDTH_2}, command=lambda: self.click(" + ")).grid(row=6, column=3)
        tk.Button(self, text="-", **DEFAULT_BTN(16) | {"width": self.WIDTH_2}, command=lambda: self.click(" - ")).grid(row=5, column=3)
        tk.Button(self, text="x", **DEFAULT_BTN(17) | {"width": self.WIDTH_2}, command=lambda: self.click(" * ")).grid(row=4, column=3)
        tk.Button(self, text="/", **DEFAULT_BTN(18) | {"width": self.WIDTH_2}, command=lambda: self.click(" / ")).grid(row=3, column=3)
        tk.Button(self, text="\u232B", **DEFAULT_BTN(19) | {"width": self.WIDTH_2}, command=lambda: self.click("B")).grid(row=2, column=3)

    def set_text(self, label, text="", add: bool = False):
        if add:
            label["text"] += text
        else:
            self.label_2["text"] = ""
            label["text"] = text

    def key_up(self, e):
        match char := e.char, self.config:
            case ("c", None) | ("f", "fg"):
                self.config = "bg"
                self.set_text(self.label, "BG Setup")
            case "c", _:
                self.config = None
                self.set_text(self.label, "0")
            case "f", "bg":
                self.config = "fg"
                self.set_text(self.label, "FG Setup")

            case "d", "bg" | "fg":
                self.colors = self.load_colors(set=True)
                self.create_widget()
                self.set_text(self.label, "BG Setup" if self.config == "bg" else "FG Setup")

            case "+" | "-" | "*" | "/" | "%" | "^", _:
                char = f" {char} "
            case "y", _:
                char = " ^ "
            case "p", _:
                char = "3.14"

        if not char or (char.strip() not in self.SYMBOLS and (not char.isdigit() or int(char) not in range(0, 10))):
            return

        self.click(char)

    def enter_down(self, _):
        self.click("=")

    def bracket_down(self, _):
        self.click("( )")

    def all_clear(self, _=None):
        self.set_text(self.label, "0")

        self.brackets = False
        self.equal = False

    def equal_to(self):
        if self.brackets:
            return
        
        calc_expr = self.label["text"]

        try:
            expr = calc_expr.replace("\u00B2", "**2").replace(" % ", "/100").replace(" ^ ", "**").replace("√ ", "**0.5")
            self.set_text(self.label, str(round(eval(expr), 4)))
        except (ZeroDivisionError, SyntaxError, TypeError, IndexError, UnboundLocalError):
            self.set_text(self.label, "ERROR")

        self.set_text(self.label_2, f"{calc_expr} =")
        self.equal = True

    def backspace(self, _=None):
        last_char = self.label["text"][-1]
        self.set_text(self.label, self.label["text"][: -3 if last_char == " " else -1])

        if self.label["text"] == "":  # Never blank label text
            self.set_text(self.label, "0")

        if last_char in ["(", ")"]:
            self.brackets = False

    def change_color(self, btn_id):
        if btn_id == "3.14":
            btn_id = 22

        btn_id = self.SYMBOLS[btn_id] if btn_id in self.SYMBOLS else int(btn_id)
        color = colorchooser.askcolor()

        if color[1] is None:
            return

        color = color[1].strip()

        del self.colors[self.config][btn_id]
        self.colors[self.config].insert(btn_id, color)

        self.create_widget()
        self.set_text(self.label, "BG Setup" if self.config == "bg" else "FG Setup")

        self.load_colors(self.colors, True)

    def click(self, btn_id):
        temp_id = btn_id.strip()

        if self.config in ["bg", "fg"]:
            return self.change_color(temp_id)

        if self.label["text"] == "ERROR" and btn_id != "AC":
            return

        if btn_id == "AC":
            return self.all_clear()
        if btn_id == "=":
            return self.equal_to()
        if btn_id == "B":
            return self.backspace()

        if btn_id == "( )":
            if self.brackets:
                self.set_text(self.label, ")", True)
                self.brackets = False
                return

            if self.label["text"] == "0":
                self.set_text(self.label, "(")
            else:
                last_char = self.label["text"][-1 if self.label["text"][-1] != " " else -2]
                self.set_text(self.label, "(" if last_char in self.SYMBOLS else " * (", True)

            self.brackets = True
            self.equal = False
            return

        if self.label["text"] == "0":
            if temp_id in self.SYMBOLS and temp_id != ".":
                return

            self.set_text(self.label, btn_id, btn_id == ".")
        elif self.equal:
            self.set_text(self.label, btn_id, temp_id in self.SYMBOLS)
            self.equal = False
        else:
            if temp_id in self.SYMBOLS:
                last_char = self.label["text"][-1 if self.label["text"][-1] != " " else -2]
                new_text, add = btn_id, True

                if last_char in ["\u00B2", "√"]:
                    new_text, add = self.label["text"][:-2] + btn_id, False
                elif last_char in self.SYMBOLS:
                    new_text, add = self.label["text"][:-3] + btn_id, False

                return self.set_text(self.label, new_text, add)

            if self.label["text"][-1] == ")" and btn_id not in self.SYMBOLS:
                return self.set_text(self.label, f" * {btn_id}", True)

            self.set_text(self.label, btn_id, True)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculator")
    root.resizable(False, False)
    root.iconphoto(False, tk.PhotoImage(file="./favicon.png"))

    calc = Calculator(master=root)
    calc.configure(bg="black")
    calc.bind("<Delete>", calc.all_clear)
    calc.bind("<(>", calc.bracket_down)
    calc.bind("<)>", calc.bracket_down)
    calc.bind("<KeyPress>", calc.key_up)
    calc.bind("<BackSpace>", calc.backspace)
    calc.bind("<Return>", calc.enter_down)
    calc.focus_set()
    calc.mainloop()
