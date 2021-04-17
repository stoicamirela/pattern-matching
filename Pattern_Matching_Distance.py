from fuzzywuzzy import fuzz

file1 = open('text.txt', 'r')
text_original = file1.read()
file2 = open('citat.txt', 'r')
citat = file2.read()

ratio = fuzz.ratio(text_original, citat)
print("Similaritatea per intregul sir de caractere folosind ratio", ratio)
partial_ratio = fuzz.partial_ratio(text_original, citat)
print("Aici va lua in considerare doar cuvintele din al doilea argument:", partial_ratio)
token_set = fuzz.token_set_ratio(text_original, citat)
print("similar cu partial ratio, in cazul cel mai probabil in care lungimile sirurilorf difera", token_set)

for i in text_original:
    if i == citat[0]:
        print("indexul de start din textul original este:", text_original.index(i))
    if i == citat[-1]:
        print("indexul de stop din textul original este: ", text_original.index(i))
        break

file1.close()
file2.close()
