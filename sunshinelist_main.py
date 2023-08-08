import pandas as pd

sunshine_df = pd.read_csv(r'C:\Users\ShihabMo\OneDrive - Government of Ontario\Documents\VSC Source Code Storage\Outlook Meeting Plugin\sunshine_list_information_ops_only.csv')

#Placeholder function that receives input for program, in final version should be automated: program will interact directly with Outlook to get and process the information needed here.
def inputReceiver():
    print("Enter list of attendees, comma seperated.")
    raw_attendee_list = input()
    print("Enter length of meeting, in minutes.")
    meeting_length = input()
    attendee_list = raw_attendee_list.split(', ')
    sunshineLookup(attendee_list)

#Runs list of attendees through the Sunshine list, returns sum of salaries for all that are found, returns any names that aren't found in the Sunshine list. 
def sunshineLookup(list_of_attendees):
    

