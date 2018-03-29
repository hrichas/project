# from flask_sqlalchemy import SQLAlchemy
# from projectApp import db


# from flask_sqlalchemy import SQLAlchemy
from projectApp import db



class Info(db.Model):
	__tablename__ = 'tbl_info'
	registration_id = db.Column(db.Integer, primary_key=True, nullable=False)
	student_name = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(20), nullable=False)
	phone_number = db.Column(db.Integer)
	documents_pdf = db.Column(db.String(100), nullable=False)

	# def __repr__(self):
	# 	return "<Info(registration_id='%d', student_name='%s', email='%s', phone_number='%d', documents_pdf='%s')>" % self.registration_id, self.student_name, self.email, self.phone_number, self.documents_pdf)


	def __init__(self, registration_id, student_name, email, phone_number, documents_pdf):
		self.registration_id = registration_id
		self.student_name = student_name
		self.email = email
		self.phone_number = phone_number
		self.documents_pdf = documents_pdf



		


