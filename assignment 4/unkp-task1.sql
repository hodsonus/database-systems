CREATE TRIGGER UNKPTASK1
    AFTER INSERT ON SIGHTINGS
    FOR EACH ROW
    WHEN NEW.PERSON NOT IN (SELECT NAME FROM MEMBERS)
    BEGIN
        SELECT RAISE(IGNORE);
        -- print 'Error: Insert into the SIGHTINGS table references a person that is not found in the database.'
    END;