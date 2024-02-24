
# Since the x is global the below fucniton cannot change it and once we print x we get tim
x= 'tim'
def func(name):
    x= name

print(x)

func('changed')
print(x)


# But we can use the Global keyword, we will get changes as output after the function is called

x= 'tim'
def func(name):
    global x
    x= name

print(x)
func('changed')
print(x)
