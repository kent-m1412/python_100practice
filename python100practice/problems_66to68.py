#problems66to68
class SimpleClass:
    count = 0
    def __init__(self,name):
        SimpleClass.count += 1
        self.name = name
        print(f'{self.name} created')

    @classmethod
    def print_count(cls):
        print(cls.count)
    def print_name(self):
        print(self.name)
