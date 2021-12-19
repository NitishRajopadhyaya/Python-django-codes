class person:

      def __init__(self,Name,Age,Address):
           self.Name=Name
           self.Age = Age
           self.Address = Address
      def eat(self):
         print(self.Name,"is eating")
          
      def walk(self):
          print(self.Name," is Walking")

      def run(self):
          print(self.Name," is Running")

      def display(self):
           print("Age And Address of",self.Name,"Is")
           print("Age=",self.Age,"Address=",self.Address)

Female=person(Name="sita",Age=25,Address="Janakapur")
Male = person(Name="Ram",Age=27,Address="Ayodhya")

Female.eat()
Female.walk()
Female.run()
print()
Female.display()

print()

Male.eat()
Male.walk()
Male.run()
print()
Male.display()

          
