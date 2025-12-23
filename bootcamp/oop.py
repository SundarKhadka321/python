class Person:
    first_name=str
    last_name=str
    age=int
    address=str
    def get_full_name(self):
        return self.first_name +" "+  self.last_name
#initialization of class   
person_ram=Person()
#assign alue

person_ram.first_name="Ram"
person_ram.last_name="khadka"
person_ram.age=22
person_ram.address = "birendranagar, surkhet"


full_name_ram=person_ram.get_full_name()
print(full_name_ram)

person_shyam=Person()

person_shyam.first_name=("shyam")
person_shyam.last_name=("devkota")
person_shyam.age=22
person_shyam.address=("surkhet")

full_name_shyam=person_shyam.get_full_name()
print(full_name_shyam)