fid = open('text1.txt', "w")
while True:
    txt = input("Input your text:")
    fid.write(txt)
    fid.write('\n')
    if len(txt) == 0:
        break
fid.close()
