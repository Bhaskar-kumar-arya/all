
def crack () :
    password =input('enter pass : ')
    chars = "abcdefghijklmnopqrstuvwxyz@#$%^&*()_0123456789#"
    def recurse (index,path) :
        if index == len(password) : 
            if path == password : print('your pass is', path)
            return 
        #print(path,password[:len(path)])
        if path != password[:len(path)] : return
        for c in chars :
            recurse(index + 1 , path + c)
    recurse(0,'')

crack()        