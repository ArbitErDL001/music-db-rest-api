CREATE DATABASE music_db;
USE music_db;

CREATE TABLE songs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(200) NOT NULL,
  artist VARCHAR(150) NOT NULL,
  genre VARCHAR(100),
  year INT
);

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(150) NOT NULL UNIQUE,
  password VARCHAR(64) NOT NULL
);

INSERT INTO songs (title, artist, genre, year) VALUES
('As the World Caves In','Matt Maltese','Indie Pop',2017),
('Clementine','Grentperez','Indie Pop',2021),
('Choose Your Fighter','Ava Max','Pop',2023),
('Freaks','Jordan Clarke','Indie Pop',2018),
('I Think They Call This Love','Unknown Artist','Pop',2020),
('Ikuyo','Kyle','Hip Hop',2018),
('Lose Yourself','Eminem','Hip Hop',2002),
('Love Machine','Jamie Page','Pop',2020),
('Me and My Broken Heart','Rixton','Pop',2014),
('Multo','Cup of Joe','OPM',2022),
('No Surprises','Radiohead','Alternative Rock',1997),
('Rolling in the Deep','Adele','Soul',2010),
('Shape of You','Ed Sheeran','Pop',2017),
('Stairway to Heaven','Led Zeppelin','Rock',1971),
('The Man Who Cant Be Moved','The Script','Pop Rock',2008),
('This December','Rick Montenegro','Pop',2021),
('Uhaw','Dilaw','OPM',2023),
('Violets Tale','Ren','Indie',2022),
('Wonderwall','Oasis','Britpop',1995),
('Yours','Jake Scott','Pop',2018);


