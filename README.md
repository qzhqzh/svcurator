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
 