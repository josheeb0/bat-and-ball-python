import time
class MyClass:


    my_string = "Hello World foo"
    def print_my_var(self, count):
        time.sleep(0.2)
        return count * 2

    def print_my_string(self):
        print(self.my_string)


print ("times tables of 2")

time.sleep(1)

class_instance = MyClass()

print(class_instance.print_my_var(100))
# for my_variable in range(1, 10):
#     class_instance.print_my_var(my_variable)
#
# class_instance.print_my_string()