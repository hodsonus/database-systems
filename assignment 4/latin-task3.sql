CREATE TRIGGER LATINTASK3
    AFTER INSERT ON SIGHTINGS
    FOR EACH ROW
    WHEN NEW.NAME NOT IN (SELECT f1.COMNAME FROM FLOWERS f1) AND
         NEW.NAME IN (SELECT f2.GENUS || ' ' ||  f2.SPECIES FROM FLOWERS f2)
    BEGIN
        UPDATE SIGHTINGS
        SET NAME = (SELECT f3.COMNAME
                    FROM FLOWERS f3
                    WHERE NEW.NAME = (f3.GENUS || ' ' ||  f3.SPECIES))
        WHERE NEW.NAME = NAME AND NEW.PERSON = PERSON AND NEW.LOCATION = LOCATION AND NEW.SIGHTED = SIGHTED;
        -- print 'Latin name, rather than common name, insertion attempted. Common name inserted.'
    END;