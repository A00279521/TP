from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for

from application import app, schooldb 
from application.models import student, moodle
from application.routes import select_list

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050 #test port dose not need to be open

    
    def create_app(self):


            app.config.update(
                SQLALCHEMY_DATABASE_URI ='sqlite:///test.db',
                LIVESERVER_PORT=self.TEST_PORT,

                DEBUG = True,
                TESTING=True
                 )
            return app



    def setUp(self):

        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)

        schooldb.create_all() #create a schema before we try to get the page
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

        self.driver.get(f'http://localhost:{self.TEST_PORT}/students')





    def tearDown(self):
        self.driver.quit()


        schooldb.drop_all()

    
    def test_server_is_up_and_running(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}/students')
        self.assertEqual(response.code, 200)

class TestAdd(TestBase):
    def submit_imput(self, case): # custom method
        self.driver.find_element_by_xpath('/html/body/dev/form/input[1]').send_keys(case)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

    def test_create(self):
        self.submit_imput("updatedvalue")

        entry= student.query.filter_by(student="updatedvalue").all()
        self.assertNotEqual(entry, None)


    def test_empty_validation(self):
        self.submit_imput('')
        self.assertIn(url_for('update_q', qid=1), self.driver.current_url)
        entry = student.query.filter_by(id=1).first()
        self.assertNotEqual(entry.student, None)
