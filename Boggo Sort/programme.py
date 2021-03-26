author="Burak BOZ"
import random, time, locale
locale.setlocale(locale.LC_ALL, 'turkish')
random.random()
start = time.strftime('%S')
array = [65.12312, 4, 3, 43, 65.12312, 43, 3, 43, 65.12312, 43, 3, 43, 65.12312, 43]

def boggo_sort(x):
    global finish
    while x != sorted(x):
        random.shuffle(x)
        finish = time.strftime('%S')
    return x


print boggo_sort(array)
result = int(finish) - int(start)
print "Duration: " + str(result)