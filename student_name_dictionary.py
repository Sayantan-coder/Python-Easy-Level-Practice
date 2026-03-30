Name = {
    "name": "sayantan",
    "note": [
        500,
        50,
        1000,
        200,
        100,
        10,
        20,
    ],
}
for key in Name.keys():
    note_list = Name["note"]


def get_top_note(note):
    if len(note) == 1:
        return note[0]
    else:
        max = note[0]
        max_of_rest = get_top_note(note[1:])
        if max < max_of_rest:
            return max_of_rest
        else:
            return max


top_note = get_top_note(note_list)
new_dictionary = {"name": Name["name"], "top_note": top_note}
print(new_dictionary)
