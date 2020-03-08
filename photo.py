def my_copy(what,where):
    with open(what,"rb")as file:
        with open(where,"wb") as file1:
            for i in file:
                file1.write(i)
my_copy("MyAvatar.1.png","new.png")

