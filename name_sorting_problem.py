def get_name(students: dict) -> list:
    name_list = []
    for name in students.values():
        name_list.append(name.lower())
    return sorted(name_list)


print(
    get_name(
        {
            "student1": "sayantan",
            "student2": "Sourish",
            "student3": "Debasish",
            "student4": "Proloy",
            "student5": "Souvik",
        }
    )
)
