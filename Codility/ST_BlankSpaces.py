def has_even_spaces(phrase):
    count = 0
    phrase = phrase.strip()
    if len(phrase) == 0:
        return False 
    for c in phrase:
        if c == ' ':
            count += 1
    return count % 2 == 0

print(has_even_spaces("Paco y Luis")) #True
print(has_even_spaces("Paco  y Luis")) #False
print(has_even_spaces(" Paco y  Luis ")) #False
print(has_even_spaces("")) #False
print(has_even_spaces("      ")) #False