# parsing json in a separate json file
import json

# This is the way to read or write file
with open('D:\\Python Study Docs\\course.json') as file:
    # load() will be used while reading json content from any external json file and returns dictionary
    data = json.load(file)
    print(data)
    print(type(data))
    # print(type(data['courses']))
    print(data['courses'][1]['title'])
    print(data['dashboard']['website'])

    # test the value of title = RPA from course.json file
    # remember, each values from the courses list can be dynamically changed. So we need to use loop to check the
    # actual existence of the title first
    for course in data['courses']:
        # print(course)
        if course['title'] == "RPA":
            print(course['price'])
            assert course['price'] == 45


