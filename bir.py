class CustomList:
    def __init__(self):
        self.elements = []
        self.backup = []
    
    def append(self, element):
        self.elements.append(element)
    
    def __enter__(self):
        self.backup = self.elements.copy()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.elements = self.backup
            print("Xatolik yuz berdi. Elementlar asl holatiga qaytarilmoqda.")
        else:
            print("Hech qanday xatolik yuz bermadi. Natija saqlanmoqda.")
    
    def __str__(self):
        return str(self.elements)

# Misol u-n:
custom_list = CustomList()

with custom_list as cl:
    cl.append(1)
    cl.append(2)
    cl.append(3)
    raise ValueError("Xatolik yuz berdi") 

print(custom_list)
