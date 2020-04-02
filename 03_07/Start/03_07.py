from functools import reduce
employees = [{
    'name': 'Jane',
    'salary': 90000,
    'job_title': 'developer'
}, {
    'name': 'Bill',
    'salary': 50000,
    'job_title': 'writer'
}, {
    'name': 'Kathy',
    'salary': 120000,
    'job_title': 'executive'
}, {
    'name': 'Anna',
    'salary': 100000,
    'job_title': 'developer'
}, {
    'name': 'Dennis',
    'salary': 95000,
    'job_title': 'developer'
}, {
    'name': 'Albert',
    'salary': 70000,
    'job_title': 'marketing specialist'
}]

developers = list(filter(lambda x: x["job_title"] == "developer", employees))
non_developers = [employee for employee in employees if employee["job_title"] != "developer"]

get_sum = lambda x,y: x + y
sum_developer_salary = reduce(get_sum, [dev["salary"] for dev in developers])
sum_non_developers_salary = reduce(get_sum, [emp["salary"] for emp in non_developers ])

num_developers = len(developers)
num_non_developers = len(non_developers)

average_developer_salary = sum_developer_salary/num_developers
average_others_salary = sum_non_developers_salary/num_non_developers

print(average_developer_salary)
print(average_others_salary)
