import tkinter as tk
import tkinter.messagebox as mb


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            easter_eggs = {
                "1004": "😇 천사가 나타났습니다. 뾰로롱!",
                "7777": "🍀 럭키한 하루 되세요!",
                "4444": "밤길 조심하세요..."
            }

            if self.expression in easter_eggs:
                mb.showinfo("💡 이스터에그 발견!", easter_eggs[self.expression])
                self.expression = ""
            else:
                try:
                    self.expression = str(eval(self.expression))
                except Exception:
                    self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



