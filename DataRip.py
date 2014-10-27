import os, linecache

# this will not dive into sub directories
#-------CHANGE THESE VALUES-------#
# path to the folder with all the files here
folder_path = 'C:\LOCAL DATA\Development\Practice'
# desired line number, numeral, no quotes
line_number = 3
# output file name (will be same location as python script)
fname = "dataRipOutput.txt"

# make a function for all the work (reusable for other folders)
def data_rip(folder_path, line_number):
	#create storage variable for print later
	output = []
	
	# open the files
	for data_file in os.listdir(folder_path):
		# build the data_path back
		data_path = folder_path + "\\" + data_file
		# Begin caching the lines to look for
		request_line = linecache.getline(str(data_path), int(line_number))
		# Add the line to the output
		if (request_line == ''):
			output.append('folder (' + data_file + ') or no line\n')
		else:
			output.append(request_line)
		# clear the cache
		linecache.clearcache()
		
	# generate the file (will destroy old data)
	file = open(fname, 'w')
	# write the output
	file.writelines(output)
	# close up
	file.close()
	
data_rip(folder_path, line_number)

