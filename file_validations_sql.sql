desc file_valiation_request

FILE_NAME           VARCHAR2(100)  
NO_OF_RECORDS       NUMBER         
STATUS              VARCHAR2(30)   
RULE_COMMENTS       VARCHAR2(4000) 
CREATED_DT          DATE           
CREATED_BY          VARCHAR2(30)   
ERROR_MESSAGE       VARCHAR2(4000) 

desc file_validation_rule

FILE_NAME         VARCHAR2(100)  
COLUMN_NAME       VARCHAR2(100)  
RULE              VARCHAR2(4000) 
CREATED_DT        DATE           
CREATED_BY        VARCHAR2(30)

desc rule_config

Name            Null? Type          
--------------- ----- ------------- 
FILE_NAME             VARCHAR2(30)  
FILE_TYPE             VARCHAR2(30)  
FILE_LOCATION         VARCHAR2(100) 
DELIMITER             VARCHAR2(1)   
SOURCE                VARCHAR2(100) 
CREATED_DT            DATE          
CREATED_BY            VARCHAR2(30)  
VALIDATION_TYPE       VARCHAR2(30)  
ACTIVE_IND            VARCHAR2(1)   
