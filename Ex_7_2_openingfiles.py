#ex 7.2
#write a program that prompts for a file name
#then opens that file and reads through the file looking for lines
#X-DSPAM-Confidence: 0.8475
#count these lines and
#extract the floating point values from each line
#compute the average (total / count) and
#produce the output as shown below

# Use the file name mbox-short.txt as the file name
# remember a file and file handle are not the same thing
# put \n into the quotes of a string to get the string to break up

#remember that we open files with for loops
# key words here are startswith and find

count = 0
total = 0

file = input('Enter file name: ')

filehandle = open(file)

for line in filehandle:
    if line.startswith('X-DSPAM-Confidence:') :
        count = count + 1
        #now get the floating point number in the file after the :
        floatingnumber = line.find(':')
        spam = line[floatingnumber + 1: ]
        spam = spam.rstrip()  #this gets rid of any new lines \n
        spam = float(spam)

        total = total + spam


print('Average spam confidence: ', total/count)
