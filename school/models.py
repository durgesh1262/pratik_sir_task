from django.db import models
import uuid

class Student(models.Model):
    User_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    marks = models.IntegerField()
    percent = models.FloatField(blank = True, null = True)
    status = models.CharField(max_length = 50, blank = True, null = True  )
    



    def percentage(self):
        self.per = (self.marks*100)/500
        return self.per


    



  
    def CalcGrade (self):
        if self.per >= 90:
            self.Grade = 'A'
            return self.Grade
        elif self.per >= 80 and self.per < 90:
            self.Grade = 'B'
            return self.Grade

        elif self.per >= 70 and self.per < 80:
            self.Grade = 'C'
            return self.Grade
        elif self.per >= 60 and self.per < 70:
            self.Grade = 'D'
            return self.Grade
        else:
            self.Grade = 'E'
            return self.Grade
    
     def stay(self):
        if self.per >= 90:
            self.Status = 'distantion+'
            return self.Status
        elif self.per >= 80 and self.per < 90:
            self.Status = 'paas with distantion'
            return self.Status
        elif self.per >= 70 and self.per < 80:
            self.Grade = 'paas'
            return self.Grade
        elif self.per >= 60 and self.per < 70:
            self.Status = 'lastly pass'
            return self.Status
        else:
            self.Status = 'fail'
            return self.Status       

        


    def save(self, *args, **kwargs):
        if not self.percent:
            self.percent=self.percentage()
        if not self.status:
            self.status= self.CalcGrade()
            if not self.status:
            self.status= self.stay()
        return super().save(*args, **kwargs)
       
       
    
    def __str__(self):
        return self.name        

    # def save(self, *args, **kwargs):
        
    #     calculate = self.calculate()
    #     self.status = calculate()
    #     super(Student, self).save(*args, **kwargs)    

    

 





     
        
     
    
   


       



    


    

    







   

# Create your models here.
