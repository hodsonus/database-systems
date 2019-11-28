CREATE TRIGGER UNKPTASK1
BEFORE INSERT ON SIGHTINGS
FOR EACH ROW
BEGIN
    SELECT CASE
        WHEN NEW.PERSON NOT IN (SELECT NAME FROM MEMBERS)
            THEN RAISE(ABORT, 'Error: Insert into the SIGHTINGS table references a person that is not found in the database.')
    END;
END;