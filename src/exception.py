import os
import sys 
def error_message_detail(error,error_detail):
    _,_,exc_tab=error_detail.exc_info()
    file_name=os.path.split(exc_tab.tb_frame.f_code.co_filename)[1]
    error_massage="Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tab.tb_lineno,str(error)
    )
    
    return error_massage

class CustomException(Exception):
    def __init__(self, error_message,error_detail):
        super().__init__(error_message)
        self.error_message=error_message_detail(
            error_message,error_detail=error_detail
        )
    def __str__(self):
        return self.error_message
try:
    a=1/0
except Exception as e:
    print(CustomException(str(e),sys))
print("hello")