# creat Dictionaries 

students = {
    "Alice": {
        "age": 18,
        "grade": "A",
        "subjects": ["Math", "Science", "English"]
    },
    "Bob": {
        "age": 17,
        "grade": "B",
        "subjects": ["History", "Geography", "Math"]
    },
    "Charlie": {
        "age": 16,
        "grade": "A",
        "subjects": ["Science", "English", "Art"]
    },
    "David": {
        "age": 19,
        "grade": "C",
        "subjects": ["Biology", "Chemistry", "Physics"]
    },
    "Eva": {
        "age": 17,
        "grade": "A",
        "subjects": ["Math", "Computer Science", "English"]
    },
    "Frank": {
        "age": 18,
        "grade": "B",
        "subjects": ["History", "Geography", "Literature"]
    },
    "Grace": {
        "age": 16,
        "grade": "A",
        "subjects": ["Math", "Biology", "Chemistry"]
    },
    "Harry": {
        "age": 17,
        "grade": "C",
        "subjects": ["History", "Art", "English"]
    },
    "Ivy": {
        "age": 16,
        "grade": "B",
        "subjects": ["Math", "Physics", "Geography"]
    },
    "Jack": {
        "age": 18,
        "grade": "A",
        "subjects": ["Computer Science", "English", "History"]
    }
}



# get method to get data 

get_Method = students.get("Ivy")
print(get_Method)




# Keys method 

keys_Method = students.keys()
print(keys_Method)




# value class 

value_Method = students.values()
print(value_Method)