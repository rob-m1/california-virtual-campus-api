import requests
from bs4 import BeautifulSoup, Tag

from .course import course
from .courseSection import courseSection

def _getPageContentFromID(id:int):
    url = f'https://search.cvc.edu/courses/{id}'
    # Send GET request to the URL
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError("Inputted ID is invalid.", id)
        return ""

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    if soup == None:
        raise ValueError("Inputted ID is invalid.", id)
        return ""
    return soup

def _parseCourse(soup):
    table = soup.find('div', attrs = {'class':'font-semibold text-sm md:text-base'})
    try:
        college_name_text = table.get_text(strip=True).strip()
    except (TypeError, AttributeError, ValueError) as e:
        college_name_text = ""
    #print(college_name_text)

    table = soup.find('h1', attrs = {'class':'text-2xl lg:text-3xl font-semibold sm:flex-grow-0 w-full'}) 
    try:
        class_name_text = table.get_text(strip=True)
        index = class_name_text.index('-')
        class_symbol = class_name_text[:index-1].strip()
        class_name_text = class_name_text[index+2:].strip()
        #print(class_symbol)
        #print(class_name_text)
    except (TypeError, AttributeError, ValueError) as e:
        class_name_text = ""
    
    table = soup.find('span', attrs = {'data-tooltip-title-value':'This is the CCC Course Identification Numbering System.'}) 
    try:
        C_ID = table.get_text(strip=True).strip()
        #print("C_ID: "+C_ID)
    except (TypeError, AttributeError, ValueError) as e:
        C_ID = ""
    
    table = soup.find('div', attrs = {'class':'course-description pb-2'}) 
    try:
        course_description = table.get_text(strip=True)
        index = course_description.index('Prerequisite:')
        prereqs = course_description[index+len("Prerequisite:")+1:]
        course_description = course_description[:index]
        index = prereqs.index('all with')
        prereqs = prereqs[:index].replace(",", "").replace(".", "").replace("and","").replace("or","").replace("-", " ")
        prereqs = prereqs.split("  ")
        for i in range(0,len(prereqs)):
            prereqs[i] = prereqs[i].strip()
        #print(course_description)
        #print(prereqs)
    except (TypeError, AttributeError, ValueError) as e:
        course_description = ""
        prereqs = []
    return course(college_name_text,class_name_text,class_symbol,C_ID,course_description,prereqs,_parseSections(soup))

def _parseSections(soup):
    table = soup.find('h3', attrs={'class':'font-semibold mb-4 border-b-2 border-c_content_text_highlight pb-2'})
    currentSem = None
    sections = []
    if table == None:
        return []
    for sem in table.parent:
        semester_text = sem.get_text(strip=True).strip()
        if(len(semester_text.replace(" ",""))==0):
            continue
        if(" - Semester" in semester_text):
            index = semester_text.index(' - Semester')
            semester_text = semester_text[:index]
            currentSem = semester_text
            continue
        if isinstance(sem, Tag):
            while True:
                section_id = sem.find('span', attrs={'class': 'text-sm font-medium section-details-crn'})
                sectionIdText = ""
                if section_id:
                    sectionIdText = section_id.get_text(strip=True)
                    section_id.extract()
                else:
                    break
                duration = sem.find('div', attrs={'class': 'w-full sm:w-auto font-semibold text-c_content_text_highlight section-details-date'})
                durationText = duration.get_text(strip=True)
                duration.extract()

                format = sem.find('button', attrs={'class': 'text-sm font-medium'})
                formatText = format.get_text(strip=True)
                format.extract()

                time = sem.find('span', attrs={'class': 'text-xs font-medium'})
                timeText = time.get_text(strip=True)
                time.extract()

                prof = sem.find('span', attrs={'class': 'text-xs font-medium section-details-professor'})
                profText = prof.get_text(strip=True)
                prof.extract()

                seatCount = sem.find('span', attrs={'class': 'seat-count-live seat-count'})
                seatCountText = seatCount.get_text(strip=True)
                seatCount.extract()
                index = seatCountText.index("available")
                seatCountText = seatCountText[:index]

                sectionNotes = sem.find('div', attrs={'class': 'text-xs section-details-notes'})
                sectionNotesText = sectionNotes.get_text(strip=True)
                sectionNotes.extract()

                tuition = sem.find('span', attrs={'class': 'font-semibold text-lg text-c_link'})
                tuitionText = tuition.get_text(strip=True)
                tuition.extract()
                index = tuitionText.index(":")
                tuitionText = tuitionText[index+2:]

                zeroTextbookCost = False
                zeroTextbookCostItem = sem.find('span', attrs={'data-tooltip-title-value': 'Zero Textbook Cost courses have no textbook-related costs or access fees for online materials.'})
                if zeroTextbookCostItem:
                    zeroTextbookCost = True
                    zeroTextbookCostItem.extract()

                foundSection = courseSection(currentSem,sectionIdText,durationText,formatText,zeroTextbookCost,timeText,profText,seatCountText,tuitionText,sectionNotesText)
                #foundSection.printAll()
                sections.append(foundSection)
    return sections

def _getCourseContentByID(id:int):
    soup = _getPageContentFromID(id)
    return _parseCourse(soup)