import tkinter as tk
import tkinter.simpledialog as sd
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
        
        extra_frame = tk.Frame(root)
        extra_frame.pack(fill="both", expand=False, pady=5)

        tk.Button(extra_frame, text="물가계산", font=("Arial", 12), command=self.inflation_calc).pack(side="left", expand=True, fill="both", padx=5)

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
    
    def inflation_calc(self):
        try:
            value = float(sd.askstring("물가 계산기", "현재 금액(원):"))
            rate = float(sd.askstring("물가 계산기", "연 물가 상승률(%):"))
            years = int(sd.askstring("물가 계산기", "몇 년 후?"))

            adjusted = value / ((1 + rate / 100) ** years)
            mb.showinfo("계산 결과", f"{years}년 후 실질 가치: 약 {int(adjusted)}원")
        except:
            mb.showerror("에러", "입력이 잘못되었습니다.")




