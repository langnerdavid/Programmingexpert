with open("file.txt", "r+") as file:
    #score = file.read()
    #new_score = int(score) + 1
    #file.seek(0)
    #file.write(str(new_score))
    #print(file.read(7))
    number_words = 0

    file1 = file.read()

end_file = file1.replace("\n", " ").replace("-", "").replace(".", "").replace(",", "")
#file1.replace("-", " ")
#file1.replace(",", " ")
#file1.replace("/", " ")

for i in end_file:
    if i == " ":
        number_words += 1


print(number_words)