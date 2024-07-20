import tkinter as tk
import os
import google.generativeai as genai

class GeminiChat:
    def __init__(self, master):
        self.master = master
        self.master.title("AMY")
        self.master.config(bg="#000000")
        self.master.geometry("400x600")

        # Set up Gemini API key
        self.GOOGLE_API_KEY = 'AIzaSyB59rBGeRBGImIwtNUfLNRtVyWmtHwm67o'
        os.environ['GOOGLE_API_KEY'] = self.GOOGLE_API_KEY
        genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

        # Set up Gemini model
        self.modelo = genai.GenerativeModel('gemini-pro')
        self.label=tk.Label(self.master,text="Chat AMY")
        self.label.pack(padx=10,pady=10)

        self.chat_history = tk.Text(self.master, width=100, height=20, bg="#000000", fg="#ffffff",  highlightthickness=0,  highlightbackground="#000000")
        self.chat_history.pack(padx=10, pady=10)

        self.input_field = tk.Entry(self.master, width=40, font=("Helvetica", 18), bg="#ffffff", fg='#000000')
        self.input_field.pack(padx=10, pady=10)

        self.send_button = tk.Button(self.master, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=10)
        self.clear_button = tk.Button(root, text="Clear Chat", command=self.clear_chat)
        self.clear_button.pack(padx=20, pady=20)


    # def send_message(self): 
    #     user_input = self.input_field.get()
    #     self.input_field.delete(0, tk.END)

    #     # Generate response using Gemini model
    #     respuesta = self.modelo.generate_content(user_input)
    #     respuesta = respuesta.text

    #     # Display response in chat history
    #     self.chat_history.insert(tk.END, f"User: {user_input}\n")
    #     self.chat_history.insert(tk.END, f"AMY: {respuesta}\n")
    def send_message(self):
        user_input = self.input_field.get()
        self.input_field.delete(0, tk.END)

        # Generate response using Gemini model
        respuesta = self.modelo.generate_content(user_input)
        respuesta = respuesta.text

        # Display user input in chat history
        self.chat_history.insert(tk.END, f"User: {user_input}\n")

        # Display response in chat history, character by character
        self.chat_history.insert(tk.END, "AMY: ")
        for char in respuesta:
            self.chat_history.insert(tk.END, char)
            self.chat_history.update_idletasks()
            self.chat_history.after(100)  # 100ms delay
        self.chat_history.insert(tk.END, "\n")





    def clear_chat(self):
        self.chat_history.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    my_chat = GeminiChat(root)
    root.mainloop()