
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
                groupName -> title
                groupIntroduction -> desc
                groupHeadImg -> HeadImg
                groupQRImg -> QRImg1
                groupMasterwechat -> wechat
                groupMasterQRImg -> QRImg2
                name -> contact
                phone
                qq
                username
                time

            wechatPersonal:
                industry
                area
                wechat -> wechat,title
                wechatIntroduction -> desc
                wechatHeadImg -> HeadImg
                wechatQRImg -> QRImg1,QRImg2
                name -> contact
                phone
                qq
                username
                time

            wechatThePublic:
                industry
                area
                publicName -> title
                publicId -> Id
                publicCoverImg -> CoverImg
                publicQRImg -> QRImg1,QRImg2
                introducer -> desc
                name -> contact
                phone
                qq
                username
                time

            wechatBusiness:
                industry
                area
                businessName -> title
                businessCoverImg -> CoverImg
                wechatQRImg -> QRImg1,QRImg2
                wechat
                businessDesc -> desc
                username
                time
            
            wechatArticle
                column
                articleName -> title
                articleContent -> Content
                articleCoverImg -> CoverImg
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

    GET list (获取各数据的列表，无需token)
    wechatGroup : http://111.230.233.49:8020/wechatGroup        para:page(industry,area)
    wechatPersonal : http://111.230.233.49:8020/wechatPersonal  para:page(industry,area)
    wechatThePublic : http://111.230.233.49:8020/wechatThePublic    para:page(industry,area)
    wechatBusiness : http://111.230.233.49:8020/wechatBusiness  para:page(industry,area)
    wechatArticle : http://111.230.233.49:8020/wechatArticle    para:page(industry,area)

    GET id (获取各数据的列表，无需token)
    wechatGroup : http://111.230.233.49:8020/wechatGroup/id     
    wechatPersonal : http://111.230.233.49:8020/wechatPersonal/id       
    wechatThePublic : http://111.230.233.49:8020/wechatThePublic/id
    wechatBusiness : http://111.230.233.49:8020/wechatBusiness/id
    wechatArticle : http://111.230.233.49:8020/wechatArticle/id

#### API返回状态

|操作|状态码 | 说明|状态码|说明|状态码|说明
|:----|:---- | :------|:---|:---|:---|:---


