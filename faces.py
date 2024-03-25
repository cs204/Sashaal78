def convert(s):
    s = s.replace(":)", "🙂")
    s = s.replace(":(", "🙁")
    return(s)
def replace():
    a = input()
    b = convert(a)
    print(b)
replace()
