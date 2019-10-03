# prints the day
print("Day 1")
# opens the file which is in the same directory
the_file = open("um-deliveries-20140519.txt")
#iterates through the file to clean up the lines
for line in the_file:
    #remove whitespace at end of line (newline)
    line = line.rstrip()
    #separate the string into list entries at the pipe character 
    words = line.split('|')

    #here's the issue - all three variables 
    #are set to the melon name (first index in the list)
    melon = words[0]
    count = words[0]
    amount = words[0]

    #print the report with the correct variable names
    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
#close the file
the_file.close()

#do exactly the same thing for day 2
#but use a different file
print("Day 2")
the_file = open("um-deliveries-20140520.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()

#do exactly the same thing for day 3
#but use a different file
print("Day 3")
the_file = open("um-deliveries-20140521.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    melon = words[0]
    count = words[0]
    amount = words[0]

    print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
the_file.close()
