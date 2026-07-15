class programmer:
    company = "Microsoft"
    def __init__(self, name, lang, salary):
        self.name = name
        self.lang = lang
        self.salary = salary

emp1 = programmer("John", "Python", 50000)
emp2 = programmer("Vivek", "python", 500000)
print(emp1.name)
print(emp2.lang)