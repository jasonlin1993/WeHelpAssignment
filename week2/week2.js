console.log("=== Task 1 ===")
// task 1

function find_and_print(messages) {
    /*
    for loop
    1. 18 years old: 年紀大於 18 歲
    2. college student 判斷為 18 歲上大學
    3. legal age: 達到合法年齡 (假設為 18 歲)
    4. vote for Donald Trump 具有投票能力 (至少18歲)

    其中每一個 key 是一個名字，每一個 value 是訊息。

    */
    const searchTerms = ["18", "college student", "legal age", "vote"];
    for (let target of searchTerms) {
        for (let [key, value] of Object.entries(messages)) {
            if (value.includes(target)) {
                console.log(key);
            }
        }
    }
}

find_and_print({
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning."
});


/*
----------------------------------------------------------------------------------------------------
*/

console.log("=== Task 2 ===")
// task 2

function calculateSumOfBonus(data){ 
    /*
    1. 獎金總和不能超過 10000 新台幣
    2. 根據表現作為發送獎金比例: below average:500、average:800、above average:1000 
    3. 根據職位職等決定發送獎金比例: CEO:1000 Engineer:800 Sales:500
    4. 根據薪水級距決定發送獎金比例: 薪水 >= 50,000: 500、薪水 < 50,000:1000
    5. John = 1000 + 800 + 1000 = 2800 
    6. Bob = 800 + 1000 + 500 = 2300
    7. Jenny =  500 + 500 + 500 = 1500
    8. total bonus = 1800 + 1500 +200 = 6600
    */
    let total = 0;
    let USD = 30;
    let performance_below_average = 500;
    let performance_average = 800;
    let performance_above_average = 1000;
    let role_CEO = 1000;
    let role_Engineer = 800;
    let role_Sales = 500;
    let above_salary = 500;
    let below_salary = 1000;
    let limit_bonus = 10000; 


    for (let i = 0; i < data.employees.length; i++) {
        let personal_total = 0;
        let salary = data.employees[i].salary;
        if (typeof salary === 'string') {
            if (salary.includes('USD')) {
                salary = parseFloat(salary) * USD;
            } else {
                salary = parseFloat(salary.replace(',',''));
            }
        }

        // 根據表現作為發送獎金比例
        if (data.employees[i].performance === 'below average') {
            personal_total += performance_below_average;
        } else if (data.employees[i].performance === 'average') {
            personal_total += performance_average;
        } else {
            personal_total += performance_above_average;
        }

        // 根據職位職等決定發送獎金比例
        if (data.employees[i].role === 'CEO') {
            personal_total += role_CEO;
        } else if (data.employees[i].role === 'Engineer') {
            personal_total += role_Engineer;
        } else {
            personal_total += role_Sales;
        }

        // 根據薪水級距決定發送獎金比例
        if (salary >= 50000) {
            personal_total += above_salary;
        } else {
            personal_total += below_salary;
        }

        // 如果獎金超過限制，則使用限制金額
        if (total + personal_total > limit_bonus) {
            console.log('總獎金不可超過 10000 元');
        } else {
            total += personal_total;
        }
    }
    console.log(total);
}




calculateSumOfBonus({  
   "employees":[  
      {  
         "name":"John",  
         "salary":"1000USD",  
         "performance":"above average",  
         "role":"Engineer"  
      },  
      {  
         "name":"Bob",  
         "salary":60000,  
         "performance":"average",  
         "role":"CEO"  
      },  
      {  
         "name":"Jenny",  
         "salary":"50,000", 
         "performance":"below average",  
         "role":"Sales"  
        }  
    ]  
});

/*
----------------------------------------------------------------------------------------------------
*/

console.log("=== Task 3 ===")
// task 3

function func(...data) {
    let charCounts = {};
    for (let i = 0 ; i < data.length ; i++) {
        let char = data[i][1];
        if (charCounts[char]) {
            charCounts[char]++;
        } else {
            charCounts[char] = 1;
        }
    }

    for (let i = 0; i < data.length; i++) {
        if (charCounts[data[i][1]] === 1) {
            return console.log(data[i]);
        }
    }

    return console.log('沒有');
}

   
func("彭⼤牆", "王明雅", "吳明");  // print 彭⼤牆  
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花");  // print  林花花 
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花");  // print 沒有

/*
----------------------------------------------------------------------------------------------------
*/

console.log("=== Task 4 ===")
// task 4

function getNumber(index){  
    if ( index % 2 == 0) {
        return console.log(Math.floor(index / 2) * 3)
    } else {
        return console.log(index + (Math.floor( index / 2) + 3))
    }
 }  
 getNumber(1);  // print 4  
 getNumber(5);  // print 10  
 getNumber(10);  // print 15


 /*
----------------------------------------------------------------------------------------------------
 */

console.log("=== Task 5 ===")
// task 5

function findIndexOfCar(seats, status, number) {
    // 配對 seats 和 status，只保留 status 為 1 的座位
    let available_seats = seats.filter((seat, index) => status[index] === 1);

    // 如果所有座位都不可用，直接返回 -1
    if (available_seats.length === 0) {
        return console.log(-1);
    }

    // 計算每個座位與 number 的差異，並找出最小的非負差異
    let diff = available_seats.filter(seat => seat - number >= 0).map(seat => seat - number);

    // 如果所有座位都比 number 小，直接返回 -1
    if (diff.length === 0) {
        return console.log(-1);
    }

    // 找出與 number 最接近的座位，並返回其對應的索引
    let min_diff = Math.min(...diff);
    let index = seats.indexOf(min_diff + number);

    return console.log(index);
}

 findIndexOfCar([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2);  // print 4  
 findIndexOfCar([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4);  // print -1  
 findIndexOfCar([4, 6, 5, 8], [0, 1, 1, 1], 4);  //  print 2