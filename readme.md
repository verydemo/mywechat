
### table
    1.database:wechat
    2.tables:
        User:
            id
            username
            passwd
            level
            valid
            wechat
            qq
            tel

        Infomation:
            wechatGroup:
                industry
                area
                groupName
                groupIntroduction
                groupHeadImg
                groupQRImg
                groupMasterwechat
                groupMasterQRImg
                name
                phone
                qq
                username

            wechatPersonal:
                industry
                area
                wechat
                wechatIntroduction
                wechatHeadImg
                wechatQRImg
                name
                phone
                qq
                username

            wechatThePublic:
                industry
                area
                publicName
                publicId
                publicCoverImg
                publicQRImg
                introducer
                name
                phone
                qq
                username

            wechatBusiness:
                industry
                area
                groupName
                groupIntroduction
                groupHeadImg
                groupQRImg
                groupMasterwechat
                groupMasterQRImg
                name
                phone
                qq
                username

#### API返回状态

|操作|状态码 | 说明|状态码|说明|状态码|说明
|:----|:---- | :------|:---|:---|:---|:---
|登录|A10 | login success | B10 | wrong username or password|
|注册|A11 | register success | B11 |invalid username or password |C11|already been registered
|权限|A12 | token expired|B12 |token invalid|C12|missing authorization|

