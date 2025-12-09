import sys ##The sys modeule provide various fnctiions and 
# variables that is used in manipulating various parts of 
#python runtime environment

import logger

"""Why logger.logging works but logging does not
 When you write: import logger
 Inside logger.py you have this: 
   import logging
   logging.basicConfig(...)
 
 So the logging configuration is applied to the logging module 
 inside logger.py, and when you call:
   logger.logging.info("message")
 you're using the same logging object that has already been 
 configured, so it writes to the file."""



"""Here sys provide access to system related info such as:
 1. the current traceback, 2. python interpreter state,
 3. command line arguments, 4. exception details"""

def error_message_detail(error, error_detail:sys):
    ##Here error is a parameter that will store the actual
    # exception message.

    ## error_detail:sys is the type hint telling the python
    #  and developers that error_detail should be in sys.
    #(Here python should not enforce automatically that 
    # error_detail should be in sys fornmat)
    _, _, exc_tb = error_detail.exc_info()
    ## here error_detail is a sys and sys.exc_info() gives
    #  traceback when exception occurs.
    ## Whats a traceback? A traceback is the detailed report 
    # Python generates when an error (exception) occurs.
    # It tells you:
    '''Where the error happened (file name)
    Which line number
    What function call sequence led to the error
    The type of error and message'''

    """
    _,_,exc_tb = error_detail.exc_info()

     exc_info() returns a tuple: (type, value, traceback)
     The tuple structure is:
     _	= exception type (ignored)
     _	= exception value/message (ignored)
     exc_tb = 	traceback object

     Using _ means "I don't care about this value".

     So only the traceback object (exc_tb) is needed
      because it contains file name and line number info.
    
    """
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    """
    file_name = exc_tb.tb_frame.f_code.co_filename
     This extracts the file name where the exception happened.
     Breaking it:
     1.exc_tb	=traceback object, it reprsents a linked 
     list of stackframes leading to where exception occured.
     A stack frame is a section of the call stack memory that is
     created each time a function (or subroutine, method, 
     or procedure) is called during a program's execution.

     2.tb_frame =the stack frame where the error occurred
     3.f_code	code =object (metadata about executed code)
     4.co_filename =path/name of file that raised the error
    
    """
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    """(Exception) = inheritance → this class extends 
     Python's built-in Exception class → meaning it behaves
     like a normal exception but with custom formatting."""
    
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        """super().__init__(error_message)
         Calls parent (Exception) constructor.
         Ensures that Python treats this as a real exception."""
        
        """Case: Without super().__init__(error_message)
         Your class becomes:
         
         class CustomException(Exception):
           def __init__(self, error_message):
             self.error_message = error_message
           def __str__(self):
             return self.error_message
         
         
          And you raise it:
           raise CustomException("Something went wrong")
          
          What happens?
          The error will still be raised.
          It will still print "Something went wrong" because we
          defined __str__().

          But Python’s internal exception system does NOT treat
          the error message as the built-in stored message."""
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message    
    

    """In your case (CustomException) :
    The Exception class already stores the error message,
      traceback, and integrates with Python.
    
    Using:
     super().__init__(error_message)
     is like telling Python: “Use the normal exception 
     behavior, then apply my custom formatting on top."""
    

##Checking if our custom exception si working properly:
'''if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        
        logger.logging.info("Divided by zero")
        print(e)
        raise CustomException(e, sys)'''
    
##Explanation
"""Exception:- This is the base class for almost all errors in Python.

When you write: except Exception:
 It means:
 “Catch any type of error that happens in the try block.”
 Examples it can catch:

Error Type	         Example
ZeroDivisionError	    1/0
ValueError	          int("hello")
KeyError	            dict()["missing"]
FileNotFoundError	    open("x.txt")

Since Exception is the parent class, it catches all of them.





as e: This part means:

 “Store the caught exception object in a variable named e.”
 So e now contains information about what went wrong.
 Full Meaning: except Exception as e:
 💡 Means: Catch ANY error that happens in the try block and 
 save the details of that error in a variable called e.
"""