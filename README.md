# California Virtual Campus API
A simple API for the California Virtual Campus platform.
---

Documentation can be found at:
https://cvc-api.github.io/

Installation:
```bash
python -m pip install CaliforniaVirtualCampusAPI 
```

Update:
```bash
python -m pip install CaliforniaVirtualCampusAPI --upgrade
```

To use the package in your program, please import the package:
```python
from cvc import *
```

Uninstallation:
```bash
python -m pip uninstall CaliforniaVirtualCampusAPI 
```

## Usage
Request a particular list of courses and retrieve all of their data.

Example:
```python
from cvc import *

courseIDs = getCourseIDsBySearch("Santa Monica College", "COMP132", "CS20B", "Data Structures with C++")[0]
getCourseContentByID(courseIDs[0])
```

## License
This project is also licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0). See LICENSE for more details.

The course data used by this project is provided by California Virtual Campus and is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).