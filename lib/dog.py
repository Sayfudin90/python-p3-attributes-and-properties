# lib/dog.py
class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", 
                      "French Bulldog", "Pug", "Pointer"]
    
    def __init__(self, name=None, breed=None):
        # Initialize protected attributes
        self._name = None
        self._breed = None
        
        # Set properties if provided
        if name is not None:
            self.name = name
        if breed is not None:
            self.breed = breed
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and 0 < len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
            
    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if breed in Dog.approved_breeds:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)