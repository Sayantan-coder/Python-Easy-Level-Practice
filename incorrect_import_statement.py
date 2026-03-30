def fix_import(sentence: str) -> str:
    word_list = list(sentence.split(" "))
    update_list = [word_list[2], word_list[3]] + [word_list[0], word_list[1]]
    update_sentence = " ".join(update_list)
    return update_sentence


print(fix_import("import object from module_name"))
print(fix_import("import randint from random"))
print(fix_import("import pi from math"))
