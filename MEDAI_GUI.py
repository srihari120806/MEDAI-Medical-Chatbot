import tkinter as tk
from tkinter import ttk, messagebox

APP_BG = '#0b1220'
SIDEBAR = '#111a2d'
CARD = '#151f34'
CARD2 = '#1b2740'
TEXT = '#eef4ff'
MUTED = '#91a0b8'
ACCENT = '#6d9cff'
GREEN = '#48d597'
RED = '#ff6b78'

SYMPTOMS = {
    'Headache': 'Rest, hydrate and reduce screen strain. Seek medical attention for sudden severe headache, confusion, weakness, fainting or vision loss.',
    'Stomach ache': 'Rest and stay hydrated. Severe, persistent or worsening abdominal pain, repeated vomiting, blood or fainting needs medical attention.',
    'Cold & cough': 'Rest and drink fluids. Seek care for breathing difficulty, chest pain, dehydration or symptoms that worsen.',
    'Ear problem': 'Avoid inserting objects into the ear. Severe pain, discharge, injury or hearing loss should be assessed professionally.',
    'Eye irritation': 'Avoid rubbing the eye and keep hands clean. Eye pain, injury or vision changes require prompt professional assessment.',
    'Vomiting': 'Take small sips of fluid if tolerated and watch for dehydration. Repeated vomiting, blood or inability to keep fluids down needs care.',
    'Chest pain': 'Chest pain can be serious. New, severe or persistent pain, especially with breathing difficulty, sweating, fainting or pain spreading to the arm or jaw, requires emergency help.',
    'Breathing problem': 'Breathing difficulty can be an emergency. Severe or rapidly worsening difficulty, blue lips, confusion or fainting requires emergency help.',
    'Fever': 'Rest and maintain fluids while monitoring symptoms. Very high or persistent fever or severe associated symptoms should be assessed by a professional.',
    'Seasonal allergies': 'Reduce exposure to known triggers. Face or throat swelling or difficulty breathing requires emergency medical help.',
    'Throat discomfort': 'Rest and use comfortable fluids. Severe swallowing difficulty, breathing problems or dehydration should be professionally assessed.',
    'Joint / body pain': 'Rest and monitor the affected area. Significant injury, swelling, weakness, numbness or persistent severe pain should be assessed.',
}

FIRST_AID = {
    'Unresponsive person': 'Call emergency services and follow dispatcher instructions. Begin CPR if trained and appropriate.',
    'Bleeding': 'Apply firm direct pressure with clean material. Severe bleeding requires emergency medical help.',
    'Choking': 'If the person cannot cough, speak or breathe normally, use appropriate choking first-aid procedures and seek emergency help.',
    'Burns': 'Cool a minor burn with cool running water. Do not apply ice or break blisters. Seek care for serious burns.',
    'Sprains': 'Protect and rest the injured area. Seek care for severe pain or inability to use the limb.',
    'Nosebleed': 'Sit upright, lean slightly forward and pinch the soft part of the nose continuously. Seek care if bleeding is heavy or does not stop.',
    'Insect sting': 'Move away from the source and monitor symptoms. Difficulty breathing or face/throat swelling is an emergency.',
}

class MEDAIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('MEDAI • Medical Assistance Program')
        self.geometry('1050x680')
        self.minsize(900, 600)
        self.configure(bg=APP_BG)
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('TCombobox', fieldbackground=CARD2, background=CARD2, foreground=TEXT, bordercolor='#2a3958', arrowcolor=TEXT)
        self.build_shell()
        self.show_home()

    def build_shell(self):
        self.sidebar = tk.Frame(self, bg=SIDEBAR, width=220)
        self.sidebar.pack(side='left', fill='y')
        self.sidebar.pack_propagate(False)
        tk.Label(self.sidebar, text='✚', bg=SIDEBAR, fg=ACCENT, font=('Segoe UI', 28, 'bold')).pack(pady=(28, 2))
        tk.Label(self.sidebar, text='MEDAI', bg=SIDEBAR, fg=TEXT, font=('Segoe UI', 22, 'bold')).pack()
        tk.Label(self.sidebar, text='Medical Assistance', bg=SIDEBAR, fg=MUTED, font=('Segoe UI', 10)).pack(pady=(0, 28))
        self.nav_buttons = []
        for label, callback in [('⌂  Overview', self.show_home), ('♡  Symptom Guide', self.show_symptoms), ('✚  First Aid', self.show_first_aid), ('◉  BMI Calculator', self.show_bmi)]:
            b = tk.Button(self.sidebar, text=label, command=callback, anchor='w', relief='flat', bd=0, bg=SIDEBAR, fg=MUTED, activebackground=CARD2, activeforeground=TEXT, font=('Segoe UI', 11), padx=22, pady=13)
            b.pack(fill='x', padx=10, pady=2)
            self.nav_buttons.append(b)
        tk.Label(self.sidebar, text='EDUCATIONAL USE ONLY\nNot a diagnosis or prescription', bg=SIDEBAR, fg='#71809a', font=('Segoe UI', 8), justify='left').pack(side='bottom', anchor='w', padx=22, pady=24)
        self.main = tk.Frame(self, bg=APP_BG)
        self.main.pack(side='right', fill='both', expand=True)
        self.header = tk.Frame(self.main, bg=APP_BG)
        self.header.pack(fill='x', padx=34, pady=(26, 12))
        self.title_label = tk.Label(self.header, text='', bg=APP_BG, fg=TEXT, font=('Segoe UI', 24, 'bold'))
        self.title_label.pack(side='left')
        tk.Label(self.header, text='●  INFORMATIONAL MODE', bg=APP_BG, fg=GREEN, font=('Segoe UI', 9, 'bold')).pack(side='right', pady=8)
        self.content = tk.Frame(self.main, bg=APP_BG)
        self.content.pack(fill='both', expand=True, padx=34, pady=(0, 28))

    def clear(self, title):
        self.title_label.config(text=title)
        for w in self.content.winfo_children(): w.destroy()

    def card(self, parent, **kwargs):
        return tk.Frame(parent, bg=CARD, highlightbackground='#243452', highlightthickness=1, bd=0, **kwargs)

    def show_home(self):
        self.clear('Good day 👋')
        hero = self.card(self.content)
        hero.pack(fill='x', pady=(4, 16))
        tk.Label(hero, text='Your health information\nstarts here.', bg=CARD, fg=TEXT, font=('Segoe UI', 30, 'bold'), justify='left').pack(anchor='w', padx=28, pady=(25, 8))
        tk.Label(hero, text='Choose a module to explore general health guidance, first-aid basics or calculate BMI.', bg=CARD, fg=MUTED, font=('Segoe UI', 11)).pack(anchor='w', padx=28, pady=(0, 24))
        grid = tk.Frame(self.content, bg=APP_BG); grid.pack(fill='both', expand=True)
        modules = [('♡', 'Symptom Guide', 'General guidance and red-flag information', self.show_symptoms, ACCENT), ('✚', 'First Aid', 'Quick educational first-aid references', self.show_first_aid, RED), ('◉', 'BMI Calculator', 'Calculate BMI and view its screening category', self.show_bmi, GREEN)]
        for i, (icon, name, desc, cmd, color) in enumerate(modules):
            c = self.card(grid); c.grid(row=0, column=i, sticky='nsew', padx=(0 if i == 0 else 7, 7 if i < 2 else 0))
            grid.columnconfigure(i, weight=1); grid.rowconfigure(0, weight=1)
            tk.Label(c, text=icon, bg=CARD, fg=color, font=('Segoe UI', 25, 'bold')).pack(anchor='w', padx=22, pady=(24, 8))
            tk.Label(c, text=name, bg=CARD, fg=TEXT, font=('Segoe UI', 15, 'bold')).pack(anchor='w', padx=22)
            tk.Label(c, text=desc, bg=CARD, fg=MUTED, font=('Segoe UI', 10), wraplength=210, justify='left').pack(anchor='w', padx=22, pady=(7, 18))
            tk.Button(c, text='Open module  →', command=cmd, relief='flat', bg=CARD2, fg=TEXT, activebackground='#263858', activeforeground=TEXT, padx=14, pady=9).pack(anchor='w', padx=22, pady=(0, 22))

    def show_symptoms(self):
        self.clear('Symptom Guide')
        top = self.card(self.content); top.pack(fill='x', pady=(4, 14))
        tk.Label(top, text='Select a concern', bg=CARD, fg=TEXT, font=('Segoe UI', 13, 'bold')).pack(anchor='w', padx=22, pady=(18, 8))
        self.symptom_var = tk.StringVar(value=list(SYMPTOMS)[0])
        box = ttk.Combobox(top, textvariable=self.symptom_var, values=list(SYMPTOMS), state='readonly', font=('Segoe UI', 11))
        box.pack(fill='x', padx=22, pady=(0, 18)); box.bind('<<ComboboxSelected>>', lambda e: self.update_symptom())
        self.symptom_result = self.card(self.content); self.symptom_result.pack(fill='both', expand=True)
        self.update_symptom()

    def update_symptom(self):
        for w in self.symptom_result.winfo_children(): w.destroy()
        name = self.symptom_var.get()
        tk.Label(self.symptom_result, text=name, bg=CARD, fg=TEXT, font=('Segoe UI', 20, 'bold')).pack(anchor='w', padx=24, pady=(24, 8))
        tk.Label(self.symptom_result, text=SYMPTOMS[name], bg=CARD, fg='#b8c5d9', font=('Segoe UI', 11), wraplength=760, justify='left').pack(anchor='w', padx=24, pady=(0, 20))
        tk.Label(self.symptom_result, text='⚠  If symptoms are severe, new, rapidly worsening or concerning, seek professional medical care.', bg='#2b1d28', fg='#ff9aa4', font=('Segoe UI', 10, 'bold'), wraplength=760, justify='left', padx=14, pady=12).pack(fill='x', padx=24, pady=(0, 24))

    def show_first_aid(self):
        self.clear('First Aid')
        tk.Label(self.content, text='Quick references for common situations', bg=APP_BG, fg=MUTED, font=('Segoe UI', 11)).pack(anchor='w', pady=(0, 14))
        grid = tk.Frame(self.content, bg=APP_BG); grid.pack(fill='both', expand=True)
        for i, (name, text) in enumerate(FIRST_AID.items()):
            r, c = divmod(i, 2); box = self.card(grid); box.grid(row=r, column=c, sticky='nsew', padx=(0, 7) if c == 0 else (7, 0), pady=7)
            grid.columnconfigure(c, weight=1); grid.rowconfigure(r, weight=1)
            tk.Label(box, text=name, bg=CARD, fg=TEXT, font=('Segoe UI', 13, 'bold')).pack(anchor='w', padx=20, pady=(18, 7))
            tk.Label(box, text=text, bg=CARD, fg=MUTED, font=('Segoe UI', 10), wraplength=350, justify='left').pack(anchor='w', padx=20, pady=(0, 18))

    def show_bmi(self):
        self.clear('BMI Calculator')
        wrap = tk.Frame(self.content, bg=APP_BG); wrap.pack(fill='both', expand=True)
        form = self.card(wrap); form.pack(side='left', fill='y', padx=(0, 14)); result = self.card(wrap); result.pack(side='right', fill='both', expand=True)
        tk.Label(form, text='Enter measurements', bg=CARD, fg=TEXT, font=('Segoe UI', 15, 'bold')).pack(anchor='w', padx=24, pady=(24, 18))
        tk.Label(form, text='Weight (kg)', bg=CARD, fg=MUTED).pack(anchor='w', padx=24)
        weight = tk.Entry(form, bg=CARD2, fg=TEXT, insertbackground=TEXT, relief='flat', font=('Segoe UI', 12)); weight.pack(fill='x', padx=24, pady=(5, 15), ipady=8)
        tk.Label(form, text='Height (cm)', bg=CARD, fg=MUTED).pack(anchor='w', padx=24)
        height = tk.Entry(form, bg=CARD2, fg=TEXT, insertbackground=TEXT, relief='flat', font=('Segoe UI', 12)); height.pack(fill='x', padx=24, pady=(5, 20), ipady=8)
        tk.Button(form, text='Calculate BMI', command=lambda: self.calculate_bmi(weight, height, result), bg=ACCENT, fg='white', relief='flat', font=('Segoe UI', 11, 'bold'), padx=16, pady=10).pack(fill='x', padx=24, pady=(0, 24))
        tk.Label(result, text='Your result', bg=CARD, fg=MUTED, font=('Segoe UI', 11)).pack(anchor='w', padx=28, pady=(28, 6))
        tk.Label(result, text='—', name='bmi_value', bg=CARD, fg=TEXT, font=('Segoe UI', 48, 'bold')).pack(anchor='w', padx=28)
        tk.Label(result, text='Enter your measurements to calculate.', bg=CARD, fg=MUTED, font=('Segoe UI', 11)).pack(anchor='w', padx=28, pady=4)
        tk.Label(result, text='BMI is a general screening measure and is not a diagnosis.', bg=CARD, fg='#71809a', font=('Segoe UI', 9)).pack(anchor='w', padx=28, pady=(18, 0))
        result.bmi_value = result.winfo_children()[1]
        result.bmi_caption = result.winfo_children()[2]

    def calculate_bmi(self, weight, height, result):
        try:
            w, h = float(weight.get()), float(height.get())
            if w <= 0 or h <= 0: raise ValueError
            bmi = w / ((h / 100) ** 2)
            category = 'Underweight range' if bmi < 18.5 else 'Healthy weight range' if bmi < 25 else 'Overweight range' if bmi < 30 else 'Obesity range'
            result.bmi_value.config(text=f'{bmi:.1f}')
            result.bmi_caption.config(text=category, fg=GREEN if 18.5 <= bmi < 25 else '#f4c95d')
        except ValueError:
            messagebox.showerror('Invalid input', 'Please enter valid positive numbers for weight and height.')

if __name__ == '__main__':
    MEDAIApp().mainloop()
