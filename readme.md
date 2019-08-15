
### table
    1.database:wechat
    2.tables:
        User:
            id
            username
            password
            level
            valid
            wechat
            qq
            tel
            time

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
                time

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
                time

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
                time

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
                time
            
            wechatArticle
                column
                articleName
                articleContent
                articleCoverImg
                username
                time

### API
    POST
    register : http://111.230.233.49:8020/register
    login : http://111.230.233.49:8020/login
    wechatGroup : http://111.230.233.49:8020/wechatGroup
    wechatPersonal : http://111.230.233.49:8020/wechatPersonal
    wechatThePublic : http://111.230.233.49:8020/wechatThePublic
    wechatBusiness : http://111.230.233.49:8020/wechatBusiness
    wechatArticle : http://111.230.233.49:8020/wechatArticle

    GET (获取各数据的列表,无需参数，无需token)
    wechatGroup : http://111.230.233.49:8020/wechatGroup
    wechatPersonal : http://111.230.233.49:8020/wechatPersonal
    wechatThePublic : http://111.230.233.49:8020/wechatThePublic
    wechatBusiness : http://111.230.233.49:8020/wechatBusiness
    wechatArticle : http://111.230.233.49:8020/wechatArticle


#### API返回状态

|操作|状态码 | 说明|状态码|说明|状态码|说明
|:----|:---- | :------|:---|:---|:---|:---


