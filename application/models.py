from application import schooldb

class student(schooldb.Model):
    __tablename__ = 'student'
    stud_id = schooldb.Column(schooldb.Integer, primary_key=True)
    student_id = schooldb.Column(schooldb.String(8),unique=True )
    surname = schooldb.Column(schooldb.String(45))
    firstName = schooldb.Column(schooldb.String(45))
    moodle = schooldb.relationship('moodle', backref='studentbr')
    #joiningTables = schooldb.relationship('joiningTables', backref='students')
   
class moodle(schooldb.Model):
    __tablename = 'moodle'
    mod_id = schooldb.Column(schooldb.Integer, primary_key=True)
    moodle_id = schooldb.Column(schooldb.String(8))
    moodleName = schooldb.Column(schooldb.String(45))
    student_id = schooldb.Column(schooldb.String(8), schooldb.ForeignKey('student.student_id'), nullable=False)
    #joiningTables = schooldb.relationship('joiningTables', backref='moodle')

# class joiningTables(schooldb.Model):
#     id = schooldb.Column(schooldb.Integer, primary_key=True)
#     student_id = schooldb.Column('student.student_id', schooldb.String(10), schooldb.ForeignKey('student_id'))
#     moodle_id = schooldb.Column('moodle.moodle_id', schooldb.String(10), schooldb.ForeignKey('moodle.id'))
