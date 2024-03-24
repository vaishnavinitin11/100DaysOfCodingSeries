class India:
    def capital(self):
        print(f"The capital of India is New Delhi.")

    def  climate(self, city="Delhi", temp=2):
        if city == "Delhi":
            print(f"{city} has a cold climate with an average temperature of {temp}°C.")
        elif(city in ["Mumbai","Bangalore"]):
            print(f"{city} has a tropical rainforest climate. It's always hot and humid there.")

class USA:
    def capital(self):
        print(f"The capital of USA is New Washington, D.C..")

    def  climate(self, city="Delhi", temp=2):
        if city == "Delhi":
            print(f"{city} has a cold climate with an average temperature of {temp}°C.")
        elif(city in ["Mumbai","Bangalore"]):
            print(f"{city} has a tropical rainforest climate. It's always hot and humid there.")

# Testing the methods
india = India() 

DKD=input("Enter the District/City (default is Delhi) : ")