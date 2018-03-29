# from PyPDF2 import PdfFileReader, PdfFileWriter
# import PyPDF2
import os

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask import Flask,request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:@127.0.0.1/db_project'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/db_project'
# engine = create_engine('mysql://root:@127.0.0.1/db_project',connect_args={"encoding": "utf8"})

# Base = declarative_base()
# db.init_app(app)


db = SQLAlchemy(app)

import projectApp.routes