#DO NOT USE WHILE LOOP
#Create a class, School, in the school.py f
class School:
    def __init__ (self, school):
        self.school= school
 #A school should have a roster, which should be an empty dictionary upon initialization but will be built-out to contain keys of grade levels. The value of each key will be a list of student names        
    def roster(self, roster={}):
        self._roster= roster
        return self._roster
#You should be able to add a student to the school by calling the add_student method and giving it an argument of the student's name and their grade.    
    def add_student(self, name, roster):
        if roster in self._roster:  #roster in this line is the key for the dict
            self._roster[roster].append(name) #if key exist in dict, add value of key into key list
        else:
            self._roster[roster]= [] #if key doesn't exist on else, create an empty list and append key and value in new list
            self._roster[roster].append(name)
        return self._roster #return/ end all function

#define a method called grade, which should take in an argument of a grade and return a list of all the students in that grade:
    def grade(self, grade):
        return self._roster[grade] #call your dict, then assigned the key for the values looking for within the dict
        

#Define a method called sort_roster that returns the school's roster where the strings in the student arrays are sorted alphabetically. 
    def sort_roster(self):
        #sort the students in the grades
        for grade_number in self._roster.keys():  #for any grade_number in dictionary of self._roster
            #search for that grade_number in that dictionary, sort them
            self._roster[grade_number] = sorted(self._roster[grade_number])
        #this is good
        import operator
        keys = self._roster
        return sorted(keys.items(), key=operator.itemgetter(1))
    
    def sort_roster2(self):
        sr={}
        for key, value in self._roster.items():
            sr[key]= sorted(value)
        return sr