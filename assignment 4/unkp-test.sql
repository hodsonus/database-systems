INSERT INTO SIGHTINGS VALUES
("Douglas dustymaiden", "Jennifer", "Double Mountain", "2008-11-28");

INSERT INTO SIGHTINGS VALUES
("Douglas dustymaiden", "Brad", "Shirley Peak", "2007-08-18");

INSERT INTO SIGHTINGS VALUES
("Douglas dustymaiden", "Donna", "Grouse Meadow", "2011-11-28");

INSERT INTO SIGHTINGS VALUES
("Douglas dustymaiden", "Maria", "Grouse Meadow", "2014-08-16");

INSERT INTO SIGHTINGS VALUES
("Douglas dustymaiden", "Joe", "Piute Peak", "2007-02-17");

SELECT *
FROM SIGHTINGS
WHERE PERSON = "Jennifer"
OR PERSON = "Brad"
OR PERSON = "Donna"
OR PERSON = "Maria"
OR PERSON = "Joe";

SELECT *
FROM MEMBERS
WHERE MEMBERSINCE IS NULL;