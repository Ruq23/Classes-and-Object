from unicodedata import name

# class variable
class Student:

    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        # instance variables
            self.name = name
            self.age = int(age)
            self.tracks = [tracks]
            self.score = float(score)

    def change_name (self, name):
        self.name = name
        print('The student name has been updated to %s' %name)
        # print(name)

    def change_age (self, age):
        self.age = age
        print('The student age has been updated to %d' %age)
        # print(age)

    def add_track (self, track):
        # new = (self.track.append(track))
        self.track = track
        print('A new track %s has been added'%track)
          
        
    def get_score(self):
        print( self.score )
       


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

#Expected methods


Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
