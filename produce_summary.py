""" function to read each report"""
def print_melons_report(day,file):
    print(f"Day{day}")          #prints day number
    text = open(file)           #opens the file into variable 
    
    for line in text:           #loops through file by line
        line = line.rstrip()    #strips right white space
        words = line.split('|') #creates doc strings at | 
        #creates meaningful value for variables below
        melon = words[0]        
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    text.close()                #closes file


print_melons_report(1, "um-deliveries-day-1.txt")
print_melons_report(2, "um-deliveries-day-2.txt")
print_melons_report(3, "um-deliveries-day-3.txt")

