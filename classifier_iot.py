import csv as csv

# Call the dataset that's going to be classified
fname = raw_input('Enter input file name: ')
try:
    test_file = open(fname, 'rb')
    test_file_object = csv.reader(test_file)
    header = test_file_object.next()
except:
    print 'File does not exist:', fname            

# This is the output file used to save the results 
fname1 = raw_input('Enter output file name: ')
try:
    prediction_file = open("output.csv", "wb")
    prediction_file_object = csv.writer(prediction_file)
except:
    print 'File cannot be opened:', fname1
   
prediction_file_object.writerow(["timestamp", "safety"])
for row in test_file_object:       
    if ('0' <= row[2] < '10') \
        & ('0' <= row[3] < '15') \
        & ('0' <= row[5] < '5') \
        & ('2' <= row[9] < '60') \
        & ('45' <= row[10] < '75') \
        & ('10' <= row[11] < '15') \
        & ('20' <= row[12] < '80') \
        & ('10' <= row[14] < '40'):                          
        prediction_file_object.writerow([row[0],'0'])    # @predict 0 for safest
    elif ('10' <= row[2] < '20') \
        & ('15' <= row[3] < '30') \
        & ('5' <= row[5] < '12') \
        & ('60' <= row[9] < '85') \
        & ('75' <= row[10] < '80') \
        & ('5' <= row[11] < '10') \
        & ('80' <= row[12] < '100') \
        & ('40' <= row[14] < '60'):                           
        prediction_file_object.writerow([row[0],'1'])    # @predict 1 for danger
    else:                                                       
        prediction_file_object.writerow([row[0],'2'])    # @predict 2 for outlier
        
# Timer for algorithm cost efficiency        
        
test_file.close()
prediction_file.close()
    