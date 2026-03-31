class Employee:
    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname

    def get_fullname(self):
        full_name = self.firstname + " " + self.lastname
        return full_name

    def get_email(self):
        email = self.firstname + "." + self.lastname + "@company.com"
        return email.lower()


e1 = Employee("sayantan", "banerjeee")
e2 = Employee("Debasish", "Ghosh")
e3 = Employee("Proloy", "Maity")

print(e1.get_fullname())
print(e2.get_email())
print(e2.firstname)
