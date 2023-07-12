print("=== Task 1 ===")
# task 1


def find_and_print(messages):
    """
    for loop
    1. 18 years old: 年紀大於 18 歲
    2. college student 判斷為 18 歲上大學
    3. legal age: 達到合法年齡 (假設為 18 歲)
    4. vote for Donald Trump 具有投票能力 (至少18歲) 
    """
    search_terms = ["18", "college student", "legal age", "vote"]
    for target in search_terms:
        for key, value in messages.items():
            if target in value:
                print(key)


find_and_print({
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning."
})


"""
---------------------------------------------------------------------------------
"""

print("=== Task 2 ===")
# task 2


def calculate_sum_of_bonus(data):
    """
    1. 獎金總和不能超過 10000 新台幣
    2. 根據表現作為發送獎金比例: below average:500、average:800、above average:1000 
    3. 根據職位職等決定發送獎金比例: CEO:1000 Engineer:800 Sales:500
    4. 根據薪水級距決定發送獎金比例: 薪水 >= 50,000: 500、薪水 < 50,000:1000
    5. John = 1000 + 800 + 1000 = 2800 
    6. Bob = 800 + 1000 + 500 = 2300
    7. Jenny =  500 + 500 + 500 = 1500
    8. total bonus = 1800 + 1500 +200 = 6600
    """
    bonus_map = {
        'performance': {
            'below average': 500,
            'average': 800,
            'above average': 1000
        },
        'role': {
            'CEO': 1000,
            'Engineer': 800,
            'Sales': 500
        }
    }
    total = 0
    USD = 30

    for employee in data['employees']:
        if isinstance(employee["salary"], int):
            salary = employee["salary"]
        elif "USD" in str(employee["salary"]):
            salary = int(employee["salary"].replace('USD', '')) * USD
        else:
            salary = int(employee["salary"].replace(',', ''))

        performance_bonus = bonus_map["performance"][employee['performance']]
        role_bonus = bonus_map["role"][employee['role']]
        salary_bonus = 500 if salary >= 50000 else 1000
        personal_total = performance_bonus + role_bonus + salary_bonus
        total += personal_total
        if total > 10000:
            print("獎金總額不能超過 10000 元")
            return
    print(total)


calculate_sum_of_bonus({
    "employees": [
        {
            "name": "John",
            "salary": "1000USD",
            "performance": "above average",
            "role": "Engineer"
        },
        {
            "name": "Bob",
            "salary": 60000,
            "performance": "average",
            "role": "CEO"
        },
        {
            "name": "Jenny",
            "salary": "50,000",
            "performance": "below average",
            "role": "Sales"
        }
    ]
})  # call calculate_sum_of_bonus function

"""
---------------------------------------------------------------------------------
"""
print("=== Task 3 ===")
# task 3


def func(*data):
    for i, name in enumerate(data):
        unique = True
        for j, other_name in enumerate(data):
            if i != j and name[1] == other_name[1]:
                unique = False
                break
        if unique:
            return print(name)
    return print("沒有")


func("彭⼤牆", "王明雅", "吳明")  # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有

"""
---------------------------------------------------------------------------------
"""
print("=== Task 4 ===")
# task 4


def get_number(index):
    if index % 2 == 0:
        return print(index // 2 * 3)
    else:
        return print(index + (index // 2 + 3))


get_number(1)  # print 4
get_number(5)  # print 10
get_number(10)  # print 15

"""
---------------------------------------------------------------------------------
"""
print("=== Task 5 ===")
# task 5


def find_index_of_car(seats, status, number):
    # 配對 seats 和 status，只保留 status 為 1 的座位
    available_seats = [seat for seat, stat in zip(seats, status) if stat == 1]

    # 如果所有座位都不可用，直接返回 -1
    if not available_seats:
        return print(-1)

    # 計算每個座位與 number 的差異，並找出最小的非負差異
    diff = [seat - number for seat in available_seats if seat - number >= 0]

    # 如果所有座位都比 number 小，直接返回 -1
    if not diff:
        return print(-1)

    # 找出與 number 最接近的座位，並返回其對應的索引
    min_diff = min(diff)
    index = seats.index(min_diff + number)

    return print(index)


find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2)  # print 4
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4)  # print -1
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4)  # print 2
