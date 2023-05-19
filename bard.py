import bardapi
import tkinter as tk

token = 'xxxxxx.'

class BAIChatGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BARD AI Chat")
        self.root.geometry('600x500')
        self.root.configure(bg='#222222')

        # set colors
        bg_color = '#333333'
        fg_color = '#FFFFFF'

        # create widgets
        self.question_label = tk.Label(self.root, text="Ask me a question:", fg=fg_color, bg='#222222', font=('Arial', 12))
        self.question_entry = tk.Entry(self.root, width=50, font=('Arial', 12), bg=bg_color, fg=fg_color)
        self.ask_button = tk.Button(self.root, text="Ask", command=self.ask_question, font=('Arial', 12), bg='#4CAF50', fg=fg_color)
        self.answer_label = tk.Label(self.root, text="", wraplength=450, justify='center', font=('Arial', 12), bg='#222222', fg=fg_color)
        self.textbox = tk.Text(self.root, height=16, width=70, font=('Arial', 12), bg=bg_color, fg=fg_color)
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_history, font=('Arial', 12), bg='#1976D2', fg=fg_color)
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, font=('Arial', 12), bg='#FF5722', fg=fg_color)

        # layout widgets
        self.question_label.pack(pady=(10, 5))
        self.question_entry.pack(ipady=5)
        self.ask_button.pack(pady=(5, 10))
        self.answer_label.pack(pady=(0, 10), padx=10)
        self.textbox.pack(padx=10, pady=(0, 10), fill=tk.BOTH, expand=True)
        self.clear_button.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10), fill=tk.X)
        self.exit_button.pack(side=tk.RIGHT, padx=(0, 10), pady=(0, 10), fill=tk.X)

        # set widget colors
        self.question_label.configure(bg='#222222')
        self.question_entry.configure(highlightbackground=fg_color, highlightcolor=fg_color)
        
        # bind Return key to Ask button
        self.root.bind('<Return>', lambda event: self.ask_button.invoke())

    def ask_question(self):
        input_text = self.question_entry.get()
        
        # Send an API request and get a response.
        response = bardapi.core.Bard(token).get_answer(input_text)

        answer_text = f"Question: {input_text}\nAnswer: {response['content']}\n"
        self.textbox.insert(tk.END, answer_text)
        self.question_entry.delete(0, tk.END)

    def clear_history(self):
        self.textbox.delete('1.0', tk.END)
        self.answer_label.config(text="")

    def run(self):
        self.root.mainloop()

gui = BAIChatGUI()
gui.run()
