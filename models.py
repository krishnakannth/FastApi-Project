from mongoengine import StringField, IntField, Document, ListField


class Employee(Document):
    name = StringField(max_length=100)
    age = IntField()
    teams = ListField()
    emp_id = IntField()

