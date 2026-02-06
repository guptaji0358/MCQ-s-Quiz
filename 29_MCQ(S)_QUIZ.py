import sys
import random
import tkinter as tk
from tkinter import messagebox

path = r"E:\Program Files\RobinData\PYTHON\RawData"
sys.path.append(path)

from MCQS_QUESTIONS_DATA import quiz_data

# ---------------- QUIZ APP ---------------- #
class QuizApp:
    def close_programme(self):
        self.root.destroy()

    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz App")
        self.root.geometry("540x450")
        self.root.resizable(False, False)
        self.set_size = 10
        self.total_sets = 5
        all_q = quiz_data.copy()

        random.shuffle(all_q)
        all_q = all_q[: self.set_size * self.total_sets]
        self.sets = [
            all_q[i:i+self.set_size]
            for i in range(0, len(all_q), self.set_size)]
        
        self.current_set = 0
        self.qno = 0
        self.score = 0

        # ---------------- UI ---------------- #
        self.count_label = tk.Label(root,font=("Arial", 11, "bold"))
        self.count_label.pack(pady=5)

        self.question_label = tk.Label(root,wraplength=500,font=("Arial", 13, "bold"),justify="left")
        self.question_label.pack(pady=10)

        self.var = tk.StringVar()

        self.options = []
        for i in range(4):
            rb = tk.Radiobutton(root,variable=self.var,indicatoron=0,width=45,
                                padx=5,pady=5,relief="ridge",selectcolor="lightblue",
                                font=("Arial", 12),
                                wraplength=460,anchor="w",justify="left")

            rb.pack(padx=25, pady=4)
            self.options.append(rb)

        self.feedback = tk.Label(root,font=("Arial", 11, "bold"))
        self.feedback.pack(pady=5)

        self.next_btn = tk.Button(root,text="Next ▶",width=12,font=("Arial", 11, "bold"),command=self.next_question)
        self.next_btn.pack(pady=10)

        self.exit_btn = tk.Button(root,text="Exit ❌",width=12,font=("Arial", 11, "bold"),fg="white",bg="red",command=self.close_programme)
        self.exit_btn.pack(pady=4)
        self.load_question()

    # ---------------- LOAD QUESTION ---------------- #
    def load_question(self):
        current_questions = self.sets[self.current_set]
        q = current_questions[self.qno]
        self.count_label.config(
            text=f"Set {self.current_set+1}/{self.total_sets} | "
                 f"Q {self.qno+1}/{self.set_size}")
        
        self.feedback.config(text="", fg="black")
        self.var.set("")
        self.question_label.config(text=q["question"])
        for i in range(4):
            self.options[i].config(text=q["options"][i],value=q["options"][i])

    # ---------------- NEXT BUTTON ---------------- #
    def next_question(self):
        selected = self.var.get()
        if selected == "":
            messagebox.showwarning("Error", "Select an option!")
            return

        correct = self.sets[self.current_set][self.qno]["answer"]

        if selected == correct:
            self.score += 1
            self.feedback.config(
                text="✅ Correct!",fg="green")

        else:
            self.feedback.config(text=f"❌ Wrong! Answer: {correct}",fg="red")
        self.root.after(1200, self.move_next)

    # ---------------- MOVE NEXT ---------------- #
    def move_next(self):
        self.qno += 1
        if self.qno == self.set_size:
            self.qno = 0
            self.current_set += 1
            if self.current_set == self.total_sets:
                self.show_result()
                return

            else:
                messagebox.showinfo("Next Set",f"Starting Set {self.current_set+1}")

        self.load_question()

    # ---------------- RESULT ---------------- #
    def show_result(self):
        messagebox.showinfo("Quiz Finished",f"Final Score: {self.score} / {self.set_size * self.total_sets}")
        self.root.destroy()

# ---------------- RUN ---------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()