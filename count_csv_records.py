
import csv
count = 0
with open('<csvfile.csv>', 'rb') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=',')
  # spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in spamreader:
    count = count + 1

print count
