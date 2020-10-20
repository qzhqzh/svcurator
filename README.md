# SVCurator
SVCurator is a Python flask based web app that allows users to manually curate putative structural variants from the Ashkenazim Jewish Trio son (NIST RM 8391). The web app displays svviz read aligned images and boxplot images as well as IGV images representing over 1200 putative structural variants. For each variant, questions and a comment section were included to describe the size and accuracy of the putative structural variant. 


SVCurator can be accessed here: [SVCurator](http://www.svcurator.com/), and registration via Google OAuth is required to access the app. 

## Documentation
More information on SVCurator can be found in the following publication:

[A crowdsourced set of curated structural variants for the human genome](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007933)

PloS Computational Biology
(June 19 2020)


## Toturial

1. Setting a github OAuth App

  * set callback URL: http://127.0.0.1:5000/github_login
  * get Client ID and Client Secret for app.py
  * change the code of getting user information

2. Init database

  * backup migrations dir and remove it.

  * migrate commands
    ```angular2
    flask db init
    flask db migrate
    flask db upgrade 
    ```
  
  * import variants data
    
    `variant2.sql`
 
3. FAQ

1. 是否有必要使用一个全新的数据库？
  项目中提供了示例数据库 db_form_responses.db, 可以满足 google 账号验证的需要。
  但是，该需要注意的是该数据库中 User 表记录的字段是 google_id
  
  如果希望创建全新的数据库，可以参考 ** 2. Init database ** 部分的做法。
  
2. 出现匿名用户（Anonymous users）找不到 variants 的错误
  原因是 github 的获取用户信息方式与 google 获取用户方式不同，需要对改部分的代码进行修改
  
3. 出现变异不存在错误
  原因是当使用自建的全新数据库的时候，因为没有导入变异数据，所以报错。
  
4. 图片不存在的问题
  不重要
