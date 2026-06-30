-- Schema: CREATE TABLE "darts" ("x" REAL, "y" REAL, score INTEGER);
-- Task: update the darts table and set the score based on the x and y values.

UPDATE darts 
SET score = CASE 
            WHEN POW(x,2) + POW(y,2) > 100 THEN 0
            WHEN POW(x,2) + POW(y,2) > 25 THEN  1
            WHEN POW(x,2) + POW(y,2) > 1 THEN  5
            ELSE 10
            END;