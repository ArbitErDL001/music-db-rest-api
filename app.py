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

# ---------------- CREATE SONG ----------------
@app.route("/songs", methods=["POST"])
def create_song():
    data = request.json
    db = get_db()
    cursor = db.cursor()

    sql = """
    INSERT INTO songs (title, artist, genre, year)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (
        data["title"],
        data["artist"],
        data.get("genre"),
        data.get("year")
    ))
    db.commit()

    return jsonify({"message": "Song added successfully"}), 201

# ---------------- READ ALL SONGS ----------------
@app.route("/songs", methods=["GET"])
def get_songs():
    output_format = request.args.get("format", "json")

    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM songs")
    songs = cursor.fetchall()

    if output_format == "xml":
        xml_data = dict_to_xml(songs)
        response = make_response(xml_data)
        response.headers["Content-Type"] = "application/xml"
        return response

    return jsonify(songs)

# ---------------- READ ONE SONG ----------------
@app.route("/songs/<int:id>", methods=["GET"])
def get_song(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM songs WHERE id = %s", (id,))
    song = cursor.fetchone()

    if not song:
        return jsonify({"error": "Song not found"}), 404

    return jsonify(song)

# ---------------- UPDATE SONG ----------------
@app.route("/songs/<int:id>", methods=["PUT"])
def update_song(id):
    data = request.json
    db = get_db()
    cursor = db.cursor()

    sql = """
    UPDATE songs
    SET title=%s, artist=%s, genre=%s, year=%s
    WHERE id=%s
    """
    cursor.execute(sql, (
        data["title"],
        data["artist"],
        data.get("genre"),
        data.get("year"),
        id
    ))
    db.commit()

    return jsonify({"message": "Song updated successfully"})