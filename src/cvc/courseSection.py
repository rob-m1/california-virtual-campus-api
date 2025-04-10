class courseSection:
    def __init__(self):
        self.duration = None
        self.section = None
        self.format = None
        self.zeroTextbookCost = None
        self.time = None
        self.Prof = None
        self.currSeatCount = None
        self.tuition = None
        self.sectionNote = None
        self.semester = None
    def __init__(self, semester, duration, section, format, zeroTextbookCost, time, prof, currSeatCount, tuition, sectionNote):
        self.duration = duration
        self.section = section
        self.format = format
        self.zeroTextbookCost = zeroTextbookCost
        self.time = time
        self.prof = prof
        self.currSeatCount = currSeatCount
        self.tuition = tuition
        self.sectionNote = sectionNote
        self.semester = semester
    def printAll(self):
        print(self.semester, self.duration, self.section, self.format, self.zeroTextbookCost, self.time, self.prof, self.currSeatCount, self.tuition, self.sectionNote)