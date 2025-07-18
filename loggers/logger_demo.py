import logging


logger = logging.getLogger(__name__) #creating a class logger from class get logger function
##inititating two handlers, one for console and one for file
console_handler = logging.StreamHandler() #obj(console_handler) created from class(Streamhandler)
file_handler = logging.FileHandler("app_demo.log", mode = 'a', encoding="utf-8") ##obj created from class

#this was handlers inititated, now add them to logger

logger.addHandler(console_handler)
logger.addHandler(file_handler)
# print(logger.handlers) ##this will show all the current handlers added into this
logger.warning("--First_log--")

#this was simply adding handlers
#now, adding formatters to handlers

formatter = logging.Formatter("{asctime} - {levelname} - {message}" , style="{" , datefmt="%Y-%m-%d %H:%M",)
#object created
console_handler.setFormatter(formatter) #format added to this specific handler

logger.warning("STAY CALM")

##.addHandler is a method of Logger, .setFormatter is method of Handler

#SO BASICALLY 
#1> create a class for logging.getlogger function
#2> create handler objects with different handlings using handler_name = logging.StreamHandler or such
#3>add that handler into created class logger.addHandler(handler_name)
#4>now create a formatter object by formatter_name=logging.Formatter(...)
#5>add these formatters to specific handlers using handler_name.setFormatter(formatter_name)
#6> SIMPLE CUSTOM LOGGER SET AND DONE   

#adding level to a logger
logger.setLevel("INFO")
#Now that class logger's level is set to info, if i set any handler's level below info to debug, it wont work, 
console_handler.setLevel("DEBUG") #won't work
# Note: You define the lowest allowed log level on the logger itself. Handlers can’t show logs lower than the defined log level of the logger they’re connected to.
# With this behavior in mind, it can be helpful during development to set your logger’s log level to DEBUG and let each handler decide their lowest log level:
#handlers can never log levels below their logger’s log level. Instead, handlers log any level above the set log level.