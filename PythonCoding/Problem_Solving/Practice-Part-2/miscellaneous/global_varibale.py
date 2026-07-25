global_var = 10

class Example:
    def show(self):
        global global_var
        global_var += 1
        print(global_var)

obj = Example()
obj.show()  # 11
