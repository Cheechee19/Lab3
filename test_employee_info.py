import employee_info as info

def test_age_range():
    result= info.get_employees_by_age_range(22,26)
    correct=[{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    assert(result==correct)
def test_average_salary():
    result= info.calculate_average_salary()
    total= 50000+60000+56000+70000+65000+60000
    average=total/6
    assert(result == average)
def test_employee_dept():
    result= info.get_employees_by_dept("Engineering")
    correct= [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    assert(result==correct)
