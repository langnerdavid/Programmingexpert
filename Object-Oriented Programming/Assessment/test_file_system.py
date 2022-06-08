s = "/dir1/dir2/dir3"
split = s.split("/")
split2 = s[1:].split("/")
split3 = s[1:].strip("/")
print(split3)
print(split)
print(split[:-1])
print(split2)
print(split2[:-1]) #split2 is the correct way -->path to the directory that needs to be added

