-- Schema: CREATE TABLE "raindrops" ("number" INT, "sound" TEXT);
-- Task: update the raindrops table and set the sound based on the number.
UPDATE raindrops
SET sound = CASE 
            WHEN number % 105 = 0 THEN "PlingPlangPlong"
            WHEN number % 21 = 0 THEN "PlingPlong"
            WHEN number % 35 = 0 THEN "PlangPlong"
            WHEN number % 15 = 0 THEN "PlingPlang"
            WHEN number % 7 = 0 THEN "Plong"
            WHEN number % 5 = 0 THEN "Plang"
            WHEN number % 3 = 0 THEN "Pling"
            ELSE number
            END
