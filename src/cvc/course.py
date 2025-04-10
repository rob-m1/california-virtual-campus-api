class course:
    def __init__(self):
        self.college_name = None
        self.class_name = None
        self.class_symbol = None
        self.C_ID = None
        self.course_description = None
        self.prereqs = None
        self.sections = None
    def __init__(self,college_name,class_name,class_symbol,C_ID,course_description,prereqs,sections):
        self.college_name = college_name
        self.class_name = class_name
        self.class_symbol = class_symbol
        self.C_ID = C_ID
        self.course_description = course_description
        self.prereqs = prereqs
        self.sections = sections
    def printAll(self):
        print(self.college_name,self.class_name,self.class_symbol,self.C_ID,self.course_description,self.prereqs)
        for section in self.sections:
            section.printAll()