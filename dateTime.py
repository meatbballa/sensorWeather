#use datetime object to create and manipulate date and time
#import modules from datetime
from datetime import time 
from datetime import date
from datetime import datetime

def main():

	#Create new date time object that holds current date time
	currentTime = datetime.now()
	
	print(currentTime)
	
	#Print only the time from datetime object
	print(datetime.time(currentTime))
	 
	 #Use strftime to print only the year from object
	print("Current year: ", currentTime.strftime("%Y"))
	 
	 #Use strftime to print very human readable date
	print("Current date: ", currentTime.strftime("%a, %B %d, %Y"))
											
if __name__ == "__main__":
	main()
