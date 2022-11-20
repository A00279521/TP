from application import app, schooldb 
from application.models import student, moodle
from application.routes import select_list
from flask_testing import TestCase
from flask import request, redirect, url_for



class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI ='sqlite:///',
            DEBUG = True,
            WTF_CSRF_ENABLED=False
             )
        return app



    def setUp(self):
        schooldb.create_all()
        listk =[["x0000012", "John", "Smith"]]
        for k in range(len(listk)):
              val= {"student_id":listk[k][0], "surname":listk[k][1], "firstName":listk[k][2]}
              studentVal= student(student_id=val["student_id"] ,surname= val["surname"],firstName=val["firstName"])
              schooldb.session.add(studentVal)
        schooldb.session.commit()

        listmod = [["Eng100","English","x0000012"]]#,["Hel001","Health Education","x0000015"],["Phy003","Physics","x0000018"]]
        for k in range(len(listmod)):
               valmod= {"moodle_id":listmod[k][0], "moodleName":listmod[k][1], "studentbr":listmod[k][2]}
               moodVal= moodle(moodle_id=valmod["moodle_id"] ,moodleName= valmod["moodleName"],student_id=valmod["studentbr"],)
               schooldb.session.add(moodVal)
        schooldb.session.commit()





    def tearDown(self):
         schooldb.drop_all()


class TestReadDB(TestBase):

     def test_dbread(self):
       val1 = student.query.first()
       assert val1.student_id=='x0000012'

     def test_dbsurname(self):
       val1 = student.query.first()
       assert val1.surname=='John'


     def test_dbfirstName(self):
       val1 = student.query.first()
       assert val1.firstName=='Smith'

     def test_dbmoodle(self):
         val1 = moodle.query.all()
         for val in val1:
             assert val.moodle_id=='Eng100'
             assert val.moodleName=='English'
             assert val.student_id=='x0000012'


class TestReadURL(TestBase):

      def test_200OK(self):
           responsevar = self.client.get(url_for('start'))
           assert responsevar.status_code==200
           responsevar1 = self.client.get(url_for('read_all_student'))
           assert responsevar1.status_code==200
           responsevar2 = self.client.get(url_for('read_all_moodle'))
           assert responsevar2.status_code==200
           responsevar3 = self.client.get(url_for('register_student'))
           assert responsevar3.status_code==200
           responsevar4 = self.client.get(url_for('delstudent'))
           assert responsevar4.status_code==200
           responsevar5 = self.client.get(url_for('readstudent'))
           assert responsevar5.status_code==200
           responsevar7 = self.client.get(url_for('update'))
           assert responsevar7.status_code==200
           responsevar9 = self.client.get(url_for('register_moodle'))
           assert responsevar9.status_code==200
           responsevar10 = self.client.get(url_for('readresult' , student_id1='x0000012'))
           assert responsevar10.status_code==200
           responsevar11 = self.client.get(url_for('register_student1' , student_id1='x0000012'))
           assert responsevar11.status_code==200



      def test_2009OK(self):
           responsevar0 = self.client.get(url_for('read_all_student'))
           assert 'x0000012' in responsevar0.text
           responsevar1 = self.client.get(url_for('read_all_student'))
           assert 'John' in responsevar1.text
           responsevar2 = self.client.get(url_for('read_all_student'))
           assert 'Smith' in responsevar2.text
           responsevar3 = self.client.get(url_for('read_all_moodle'))
           assert 'Eng100' in responsevar3.text
           responsevar4 = self.client.get(url_for('read_all_moodle'))
           assert 'English' in responsevar4.text

           



