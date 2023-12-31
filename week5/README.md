### 要求二: 建立資料庫和資料表
透過終端機 Command Line 介⾯ ，連結到 MySQL 伺服器中進⾏管理，完成以下動作
1. 建立⼀個新的資料庫，取名字為 website 。

    ![Test Image](picture/task2-1.png)

2. 在資料庫中，建立會員資料表，取名字為 member 。資料表必須包含以下欄位設定：

      | 欄位名稱 | 資料型態 | 額外設定 | 用途說明 |
      | -------- | -------- | -------- | --------|
      | id | bigint  | 主鍵、自動選擇  | 獨立編號 |
      | name | varchar(255)  | 不可為空值  | 姓名 |
      | username | varchar(255)  | 不可為空值  | 帳戶名稱 |
      | password  | varchar(255)  | 不可為空值  | 帳戶密碼 |
      | follower_count  | int unsigned  | 不可為空值，預設為 0  | 追蹤者數量 |
      | time  | datetime  | 不可為空值，預設為當前時間  | 註冊時間 |
    
      ![Test Image](picture/task2-2.png)
      ![Test Image](picture/task2-3.png)
  
---

### 要求三: SQL CRUD
利⽤要求⼆建立的資料庫和資料表，寫出能夠滿⾜以下要求的 SQL 指令：

- 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。

    ![Test Image](picture/task3-1.png)

  接著繼續新增⾄少 4 筆隨意的資料。

    ![Test Image](picture/task3-2.png)

    ![Test Image](picture/task3-3.png)

- 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。

    ![Test Image](picture/task3-4.png)

- 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由 近到遠排序。

    ![Test Image](picture/task3-5.png)

- 使⽤ SELECT 指令取得 member 資料表中第 2 到第 4 筆共三筆資料，並按照 time 欄 位，由近到遠排序。 ( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )

     ![Test Image](picture/task3-6.png)

- 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。

    ![Test Image](picture/task3-7.png)

- 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

    ![Test Image](picture/task3-8.png)

- 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改 成 test2。

    ![Test Image](picture/task3-9.png)

---

### 要求四: SQL Aggregate Functions
利⽤要求⼆建立的資料庫和資料表，寫出能夠滿⾜以下要求的 SQL 指令：

- 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。

  ![Test Image](picture/task4-1.png)

- 取得 member 資料表中，所有會員 follower_count 欄位的總和。

  ![Test Image](picture/task4-2.png)

- 取得 member 資料表中，所有會員 follower_count 欄位的平均數。

  ![Test Image](picture/task4-3.png)

---

### 要求五: SQL JOIN
1. 在資料庫中，建立新資料表紀錄留⾔資訊，取名字為 message 。資料表中必須包含以 下欄位設定：
   
  | 欄位名稱 | 資料型態 | 額外設定 | 用途說明 |
  | -------- | -------- | -------- | --------|
  | id | bigint  | 主鍵、自動選擇  | 獨立編號 |
  | member_id | bigint  | 不可為空值,外鍵對應 member 資料表中的 id  | 留言者會員編號 |
  | content | varchar(255)  | 不可為空值  | 留言內容 |
  | like_count  | int unsigned  | 不可為空值，預設為 0  | 按讚的數量 |
  | time  | datetime  | 不可為空值，預設為當前時間  | 留言時間 |

  ![Test Image](picture/task5-1.png)

  ![Test Image](picture/task5-2.png)

-  使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者的姓名。

  ![Test Image](picture/task5-3.png)

- 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有 留⾔，資料中須包含留⾔者的姓名。

  ![Test Image](picture/task5-4.png)

- 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中 欄位 username 是 test 的所有留⾔平均按讚數。

  ![Test Image](picture/task5-5.png)
