#I want to add somedata to the database using Custom Command

from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help='It will insert data to the database'

    def handle(self,*args,**kwargs):
        #logic goes here
        #add 1 data 
        dataset = [
            {'roll_no':1002 , 'name':'Sachin' , 'age':20},
            {'roll_no':1003 , 'name':'John' , 'age':21},
            {'roll_no':1004 , 'name':'Mike' , 'age':22},
            {'roll_no':1005 , 'name':'Nisba' , 'age':23},
            {'roll_no':1006 , 'name':'Koushiki' , 'age':24},
            {'roll_no':1007 , 'name':'Sakshi' , 'age':25},
            

        ]
        for data in dataset:
            # print(data['name'])
            roll_no=data['roll_no']
            existing_record=Student.objects.filter(roll_no=roll_no).exists()
            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'] , name=data['name'],age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll no:{roll_no} already exists!'))
            
        self.stdout.write(self.style.SUCCESS('Data Inserted Successfully'))