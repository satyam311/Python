count = 0 
while count < 5 :
    print(count)
    count +=1 


print("##################################")

print("Break Statement")

numbers = [1,2,3,4,5]
for number in numbers :
    if number == 3 :
        break
    print(number)


print("##################################")

print("Continue Statment")

numbers = [1,2,3,4,5,6,7]
for number in numbers:
    if number == 3 :
        continue

    print(number)


print("##################################")
print('In this practice exercise, we use a "for" loop to automate the analysis of a log file and identify lines containing the word "error." This demonstrates how loops can be used to process data and extract relevant information efficiently.')

log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]



for log_line in log_file : 
    if "ERROR" in log_line:
        print(log_line)

        