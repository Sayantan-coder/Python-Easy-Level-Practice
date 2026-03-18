def calculate_relationship(Name: str) -> str:
    Relationship = {
        "Abir": "father",
        "Dip": "brother",
        "Souvik": "cousin",
        "Akash": "cousin",
    }
    for name, relationship in Relationship.items():
        if Name == name:
            return relationship

    return None


relationship_belong_to = calculate_relationship("Akash")
print(f"I am your {relationship_belong_to}.")
