# Raisig and handeling an exception
# This will print an error

try:
    x = 7 / 0
except Exception as e:
    print(e)

#But we if do below we will get the error
x = 7 / 0

# Finally block
try:
    x = 7 / 0
except Exception as e:
    print(e)
finally:
    print("Bye Bye")