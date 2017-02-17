import csv

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['Nickname','time','post','bagOfWords', 'Label'])
outputFile.close()
