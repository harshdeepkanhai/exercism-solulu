-- Schema: CREATE TABLE "grains" ("task" TEXT, "square" INT, "result" INT);
-- Task: update the grains table and set the result based on the task (and square fields).
UPDATE grains
SET result = CASE 
            WHEN task = 'single-square' THEN POW(2,square - 1) 
            ELSE POW(2,64)
            END
