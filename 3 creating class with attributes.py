
#here class vechile: model,price = 1000 as attributes
class vechile:
    model = None
    price = 1000

audi = vechile()
ferrari = vechile()
audi.price = 9000
print(audi.price) # outputs 9000
print(ferrari.price) # outputs 1000 becoz we didn't set the value so it uses class value