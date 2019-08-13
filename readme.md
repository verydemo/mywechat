
### table
    1.database:wechat
    2.tables:
        User:
            id
            username
            passwd
            level
            valid
            name
            wechat
            wechat_name
            wechat_img
            qq
            tel
            profession
            area

        Infomation:

#### API返回状态

|状态码 | 说明|状态码|说明|状态码|说明
|:---- | :------|:---|:---|:---|:---
| A10 | login success | B10 | wrong username or password|
| A11 | register success | B11 |invalid username or password |C11|already been registered
| A12 | token expired|B12 |token invalid|C12|missing authorization|

