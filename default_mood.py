def create_NewString(word="neutral") -> str:
    New_Word = "Today,I am feeling"
    if word is None:
        return New_Word + " " + word
    else:
        return New_Word + " " + word


New_String = create_NewString()
print(New_String)
