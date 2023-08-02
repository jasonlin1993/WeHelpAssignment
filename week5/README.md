### 要求二: 建立資料庫和資料表
透過終端機 Command Line 介⾯ ，連結到 MySQL 伺服器中進⾏管理，完成以下動作
1. 建立⼀個新的資料庫，取名字為 website 。

  ![Test Image](picture/task2-1.png)

2.在資料庫中，建立會員資料表，取名字為 member 。資料表必須包含以下欄位設定：

  | 欄位名稱 | 資料型態 | 額外設定 | 用途說明 |
  | -------- | -------- | -------- | --------|
  | id | bigint  | Cell 1C  | Cell 1C |
  | name | varchar(255)  | Cell 1C  | Cell 1C |
  | username | varchar(255)  | Cell 1C  | Cell 1C |
  | password  | varchar(255)  | Cell 1C  | Cell 1C |
  | follower_count  | int unsigned  | Cell 1C  | Cell 1C |
  | time  | datatime  | Cell 1C  | Cell 1C |

  
