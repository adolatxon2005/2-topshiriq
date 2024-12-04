# Developed by Ibrohimova Adolatxon
import csv
 
# 2D o'zgaruvchilar ro'yxati (satr va ustunlar bilan jadval ma'lumotlari)
input_variable = [
    ['S.no','name','e-mail'],
    [1,'meesha','meesh@email.com'],
    (2,'abhilasha','ab@email.com'),
    (3,'arav','arav123@email.com')
]
 
# Example.csv joriy ishchi katalogda yaratiladi
with open ('Example.csv','w',newline = '') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ' ')
    my_writer.writerows(input_variable)
