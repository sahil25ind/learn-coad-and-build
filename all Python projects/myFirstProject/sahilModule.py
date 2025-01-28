#this is not a built-in module "sahil" created this module
import math

pi=3.14159
root2 = 1.4142
root3 = 1.7320
root5 = 2.2360
root7 = 2.6457

def square(x):
    return x**2
def cube(x):
    return x**3
def circumferenceCircle(r):
    return 2*pi*r
def areaCircle(r):
    return pi*(r**2)
def circumferenceRect(l,w):
    return 2*(l+w)
def areaRect(l,w):
    return l*w
def areaTriangle(b,h):
    return (1/2)*b*h
def hypotenious(p,b):
    return math.sqrt((p**2)+(b**2))

def main():
    print(__name__)
    print("this is the module that i created")

if __name__ == "__main__":  #so here if this file will execute directly then __name__ will be set to string "__main__"
    main()
else:
    print("this module has been executed indirectly")
    print(__name__)


words = [       # i copy pasted all this please dont hate me for this
    "Aardvark", "Albatross", "Alligator", "Alpaca", "Ant", "Anteater", "Antelope", "Armadillo",
    "Baboon", "Badger", "Barracuda", "Bat", "Bear", "Beaver", "Bee", "Bison", "Boar", "Buffalo",
    "Butterfly", "Camel", "Caribou", "Cat", "Caterpillar", "Cattle", "Chameleon", "Cheetah",
    "Chicken", "Chimpanzee", "Chinchilla", "Clam", "Cobra", "Cockroach", "Cod", "Coyote",
    "Crab", "Crane", "Crocodile", "Crow", "Deer", "Dingo", "Dog", "Dolphin", "Donkey",
    "Dove", "Dragonfly", "Duck", "Eagle", "Eel", "Elephant", "Elk", "Emu", "Falcon",
    "Ferret", "Finch", "Fish", "Flamingo", "Fox", "Frog", "Gazelle", "Gecko", "Giraffe",
    "Goat", "Goldfish", "Goose", "Gorilla", "Grasshopper", "Guinea Pig", "Hamster", "Hare",
    "Hawk", "Hedgehog", "Heron", "Hippopotamus", "Hornet", "Horse", "Human", "Hummingbird",
    "Hyena", "Iguana", "Impala", "Jaguar", "Jellyfish", "Kangaroo", "Kingfisher", "Koala",
    "Koi Fish", "Krill", "Ladybug", "Lemur", "Leopard", "Lion", "Llama", "Lobster", "Locust",
    "Lynx", "Macaw", "Magpie", "Manatee", "Mandrill", "Mantis", "Meerkat", "Mole", "Mongoose",
    "Monkey", "Moose", "Mosquito", "Narwhal", "Newt", "Nightingale", "Octopus", "Okapi",
    "Opossum", "Orangutan", "Ostrich", "Otter", "Owl", "Ox", "Oyster", "Panda", "Panther",
    "Parrot", "Peacock", "Pelican", "Penguin", "Pheasant", "Pig", "Pigeon", "Platypus",
    "Polar Bear", "Porcupine", "Porpoise", "Quail", "Quelea", "Quokka", "Rabbit", "Raccoon",
    "Ram", "Rat", "Raven", "Reindeer", "Rhinoceros", "Salamander", "Salmon", "Sandpiper",
    "Sardine", "Scorpion", "Seahorse", "Seal", "Shark", "Sheep", "Shrimp", "Skunk", "Sloth",
    "Snail", "Snake", "Sparrow", "Spider", "Squid", "Squirrel", "Starfish", "Stingray",
    "Stork", "Swallow", "Swan", "Tapir", "Tarsier", "Termite", "Tiger", "Toad", "Tortoise",
    "Toucan", "Turkey", "Turtle", "Viper", "Vulture", "Walrus", "Wasp", "Weasel", "Whale",
    "Wolf", "Wombat", "Woodpecker", "Worm", "Yak", "Zebra"
]

class Car:        #this is the way to create object in same file by creating class in same file
    def __init__(self,model,year,color,for_sale):
        self.for_sale = for_sale
        self.year = year
        self.model = model
        self.color = color
    def move(self):
        print(f"{self.model} is moving.")
    def stop(self):
        print(f"{self.model} is stoped.")
    def description(self):
        print(f"{self.year} {self.color} {self.model} {self.for_sale}")

# x = "0"
# y = "sahil kumar"
# print(f"{x}:{y}")
