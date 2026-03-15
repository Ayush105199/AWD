import csv
from django.core.management.base import BaseCommand
# from dataentry.models import Student
from django.apps import apps
import datetime

#Proposed Command = python manage.py exportdata


class Command(BaseCommand):
    help='Export data from the database to a CSV file'

    def  add_arguments(self,parser):
        parser.add_argument('model_name',type=str,help='Model Name')



    def handle(self,*args,**kwargs):
        #fetch the data from the database
        model_name=kwargs['model_name'].capitalize()

        #search through all the installed apps for the model
        model=None
        for app_config in apps.get_app_configs():
            try:
                model=apps.get_model(app_config.label,model_name)
                break #stop executing once the model is found
            except LookupError:
                pass
        if not model:
            self.stderr.write(f'Model {model_name} could not found')
            return
             

        data=model.objects.all()
        
        # students=Student.objects.all()
        # print(students)

        #generate the timestamp of current date and time 
        
        timestamp=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        
        #define the CSV file name/path
        file_path =f'Exported_{model_name}_data_{timestamp}.csv'
        # file_path=f'exported_students_data_{timestamp}.csv'
        print(file_path)

        #Open the CSV file and write the data

        with open(file_path, 'w',newline='') as file :
            writer=csv.writer(file)
            # write the csv header 
            # writer.writerow(['Roll No','Name','Age'])
            #we want to print the field name of the model that we are trying to export
            #_meta.field is api provided by django to fetch header
            writer.writerow([field.name for field in model._meta.fields])

            # write data rows
            # for student in students:
            #     writer.writerow([student.roll_no,student.name,student.age])

            for dt in data:
                writer.writerow([getattr(dt , field.name) for field in model._meta.fields])
        self.stdout.write(self.style.SUCCESS('Data exported successfully!'))
                 

