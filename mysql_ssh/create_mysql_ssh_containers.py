#This script is to create bunch mysql containers for students. It can be modified for other containers such as LAMP as well.
#It takes in students.txt (which contains student names on every line)
#Creates a directory for them
#Creates docker container
#Gives you output.csv with information accessing the container

#Container being used in this script allows students to ssh into the container to utilize mysql. Mysql database is saved in the student directory on host side.

import os

output_list = open('output.csv','w') #where the final passwords and ports will be stored
output_list.write("Studentname,studentport,studentpassword,studentfolder\n") #CSV header
student_list = open('students.txt','r') #file with student names on every line
ssh_port = 2000 #Starting port for ssh

storage_directory = "/datastorage/" #where all the student mysql data is stored
base_command = """docker run -d -p %s:22 -v %s:/var/lib/mysql -e ROOT_PASS="%s123456" -t umrigark/centos6-ssh-mysql""" #our base command

for student_name in student_list.readlines(): #For each student name in student.txt file
    s_name = student_name.strip() #get student name
    s_storage = storage_directory+str(s_name) #generate a string for where the data will be saved
    os.system("mkdir %s" % (s_storage,)) #make a folder for the student
    os.system(base_command % (ssh_port, s_storage, s_name,)) #build a docker container with the ssh port, host directory, and password
    output_list.write("%s,%s,%s123456,%s\n" % (s_name, ssh_port, s_name, s_storage,))
    ssh_port = ssh_port + 1 #add 1 to the port so we dont reuse a port

print "Done"
print "Please look at output.csv for more information"
print "To ssh in, use the following command:"
print "ssh root@IP_ADDRESS -p PORT"