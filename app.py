from flask import Flask, request, jsonify, make_response
import mysql.connector
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

# ---------------- DATABASE CONNECTION ----------------
def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

# ---------------- XML FORMATTER ----------------
def dict_to_xml(data):
    root = ET.Element("songs")
    for item in data:
        song = ET.SubElement(root, "song")
        for key, value in item.items():
            ET.SubElement(song, key).text = str(value)
    return ET.tostring(root)