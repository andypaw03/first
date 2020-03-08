def file_size(filename):
    with open(filename,"rb")as file:
        file_size=0
        for i in file:
            file_size+=len(i)
        return file_size
print(file_size("dwegf.txt"))