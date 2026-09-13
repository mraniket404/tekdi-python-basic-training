# Python Iterators


# 1. Iterator from tuple
mytuple = ("apple", "banana", "cherry")

myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


# 2. Iterator from string
mystr = "banana"

myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# 3. Using for loop
fruits = ("apple", "banana", "cherry")

for fruit in fruits:
    print("Fruit:", fruit)


# 4. Custom iterator
class MyNumbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print("Custom:", next(myiter))
print("Custom:", next(myiter))
print("Custom:", next(myiter))


# 5. Custom iterator with StopIteration
class LimitedNumbers:

    def __iter__(self):
        self.number = 1
        return self

    def __next__(self):
        if self.number <= 5:
            value = self.number
            self.number += 1
            return value
        else:
            raise StopIteration


limited = LimitedNumbers()

for number in limited:
    print("Limited:", number)