from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo, ValidationError


class NameForm(FlaskForm):
    Stud_id = StringField("Student Id", validators=[DataRequired(), Length(min=8,max=8), Regexp("x\d{7}")])
    SName = StringField("Surname", validators=[DataRequired(), Length(min=4,max=45)])
    FName = StringField("firstName",validators=[DataRequired(), Length(min=4,max=45)])
    submit = SubmitField("Submit")


class DelForm(FlaskForm): 
    Stud_id = StringField("Student Id", validators=[DataRequired(), EqualTo('Stud_id1', message='student id must match'), Length(min=8,max=8), Regexp("x\d{7}") ])
    Stud_id1= StringField("Confirm Id", validators=[DataRequired(), Length(min=8,max=8), Regexp("x\d{7}") ])
    delete = SubmitField("Delete")
    submit = SubmitField("Exit")

class SinForm(FlaskForm): 
    Stud_id = StringField("Student Id", validators=[DataRequired(), Length(min=8,max=8) , Regexp("x\d{7}")])
    submit = SubmitField("Submit")
    submit1 = SubmitField("Exit")

class MoodleForm(FlaskForm):
    Stud_id = StringField("Student Id", validators=[DataRequired(), Length(min=8,max=8), Regexp("x\d{7}") ])
    Modcode = StringField("Code List",validators=[DataRequired(), Length(min=6,max=8)])
    Subname = StringField("Subject List",validators=[DataRequired(), Length(min=5,max=45)] )
    submit = SubmitField("Submit")
    submit1 = SubmitField("Exit")

class SelectFieldForm(FlaskForm):
    list = SelectField("SELECT ONE", choices=['All Student Page','All Moodle Page','Register A Student','Register A Moodle','Delete A Student','Home Page','Enter Student ID','Update' ])
    submit = SubmitField("Submit")