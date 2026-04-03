def DNA_to_RNA(dna: str) -> str:
    rna = ""
    for char in dna:
        if char == "A":
            char = "U"
            rna += char
        elif char == "T":
            char = "A"
            rna += char
        elif char == "G":
            char = "C"
            rna += char
        else:
            char = "G"
            rna += char
    return rna


print(DNA_to_RNA("ATTAGCGCGATATACGCGTAC"))
print(DNA_to_RNA("CGATATA"))
print(DNA_to_RNA("GTCATACGACGTA"))
