class Device:
    def __init__(self, brand):
        self.brand = brand

    def power_on(self):
        print(f"{self.brand} device is powering on...")

class Smartphone(Device):
    def __init__(self, brand, model, storage):
        super().__init__(brand)   # Call parent constructor
        self.model = model
        self.__storage = storage  # Encapsulated (private attribute)

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model} 📞")

    def get_storage(self):
        return f"{self.__storage}GB"

    def power_on(self):
        print(f"{self.brand} {self.model} is booting up 📱")

phone1 = Smartphone("Samsung", "S23", 256)
phone2 = Smartphone("Apple", "iPhone 14", 128)

phone1.power_on()
phone1.make_call("0799379082")
print("Storage:", phone1.get_storage())

phone2.power_on()
