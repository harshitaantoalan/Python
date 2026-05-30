
class Pet:
    def __init__(self, name, health):
        self.name = name
        self.__health = health   # Private attribute

    def show_info(self):
        print(f"Pet Name: {self.name}")
        print(f"Health Level: {self.__health}")

    def care_action(self):
        print(f"{self.name} needs general care.")

    # Setter Method
    def set_health(self, new_health):
        if new_health >= 0 and new_health <= 100:
            self.__health = new_health
            print(f"{self.name}'s health updated to {self.__health}.")
        else:
            print("Health must be between 0 and 100.")



class Dog(Pet):
    def care_action(self):   
        print(f"{self.name} needs a walk and some playtime.")



class Cat(Pet):
    def care_action(self):   
        print(f"{self.name} needs grooming and quiet rest.")



class Rabbit(Pet):
    def care_action(self):   
        print(f"{self.name} needs fresh carrots and a clean cage.")



pets = [Dog, Cat, Rabbit]

print("===== My Pet Care Dashboard =====")

for pet in pets:
    pet.show_info()
    pet.care_action()
    print()



print("Updating pets health")


Dog.set_health(90)
Cat.set_health(80)
Rabbit.set_health(70)



for pet in pets:
    pet.show_info()
    print()