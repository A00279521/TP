from application import schooldb
from application.models import student, moodle

#****************DROP TABLES************************************************
schooldb.drop_all()

#***************************************************************************
schooldb.create_all()
# *********************STUDENT TABLE****************************************
listk =[["x0000012", "Johnbull", "Smith"],["x0000013", "Sean", "Roberts"],["x0000016", "Maggie", "Freeman"],["x0000018", "Theresa", "Oneil"],["x0000021", "Gabriel", "Oregon"], ["x0000028", "Malisa", "Hergeton"]]
for k in range(len(listk)):
    val= {"student_id":listk[k][0], "surname":listk[k][1], "firstName":listk[k][2]}
    studentVal= student(student_id=val["student_id"] ,surname= val["surname"],firstName=val["firstName"],)
    schooldb.session.add(studentVal)
    schooldb.session.commit()
#**********************************************************************************

# *********************MOODLE TABLE*******************************************
listmod = [["Mat100","Mathematics","x0000012"],["Eng001","English","x0000012"],["Che003","Chemistry","x0000012"],
            ["Math101","Mathematics","x0000013"],["Math100","Mathematics","x0000013"],["Che003","Chemistry","x0000013"],
            ["Eng001","English","x0000013"],["Math101","Mathematics","x0000016"],["Phy100","Physics","x0000016"],
            ["Bio102","Biology","x0000016"],["Eng001","English","x0000016"],["Che003","Chemistry","x0000016"],
            ["Math100","Mathematics","x0000018"],["Phy100","Physics","x0000018"],["Math101","Mathematics","x0000021"],
            ["Bio102","Biology","x0000021"],["Che003","Chemistry","x0000021"],["Eng001","English","x0000021"],
            ["Math101","Mathematics","x0000028"],["Bio102","Biology","x0000028"]]
for k in range(len(listmod)):
    valmod= {"moodle_id":listmod[k][0], "moodleName":listmod[k][1], "studentbr":listmod[k][2]}
    moodVal= moodle(moodle_id=valmod["moodle_id"] ,moodleName= valmod["moodleName"],student_id=valmod["studentbr"],)
    schooldb.session.add(moodVal)
    schooldb.session.commit()

