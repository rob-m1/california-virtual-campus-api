# California Virtual Campus API
A simple API for the California Virtual Campus platform.
---

There are two classes within this API:

``` 
course {
    college_name
    class_name
    class_symbol
    C_ID
    course_description
    prereqs
    sections            # Holds a list of courseSection objects
}
```

---

``` 
courseSection {
    semester
    duration
    section
    format
    zeroTextbookCost
    time
    prof
    currSeatCount
    tuition
    sectionNote
}
```
---
Methods:

```
getCourseContentByID(id:int)
```

Returns a course object with the corresponding ID on https://search.cvc.edu/courses/{id}

## License
This project is also licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0). See LICENSE for more details.