class Name:
    def __init__(self, fname, lname):
        self.firstname = fname[0].upper() + fname[1:].lower()
        self.lastname = lname[0].upper() + lname[1:].lower()

    def get_fullname(self):
        fullname = self.firstname + " " + self.lastname
        return fullname

    def get_initials(self):
        initial = self.firstname[0] + "." + self.lastname[0]
        return initial


name1 = Name("SAYANTAN", "Banerjee")
print(name1.get_fullname())
print(name1.get_initials())
print(name1.firstname)
print(name1.lastname)
