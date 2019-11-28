INSERT INTO SIGHTINGS VALUES
("Sky pilot", "Person X", "Grouse Meadow", "2006-08-18");

INSERT INTO SIGHTINGS VALUES
("Hoar buckwheat", "Person X", "Grouse Meadow", "2006-08-18");

INSERT INTO SIGHTINGS VALUES
("Zigadenus venenosus", "Person X", "Grouse Meadow", "2006-08-18");

INSERT INTO SIGHTINGS VALUES
("Carex limosa", "Person Y", "Grouse Meadow", "2006-08-18");

INSERT INTO SIGHTINGS VALUES
("Draperia", "Person Z", "Grouse Meadow", "2006-08-18");

SELECT *
FROM SIGHTINGS
WHERE PERSON = "Person X"
OR PERSON = "Person Y"
OR PERSON = "Person Z";