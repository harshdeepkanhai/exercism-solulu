-- Schema: CREATE TABLE "leap" ( "year" INT, "is_leap" BOOL);
-- Task: update the leap table and set the is_leap based on the year field.
UPDATE leap
SET is_leap = CASE 
                WHEN year % 100 = 0 THEN year % 400 = 0 ELSE year % 4 = 0
              END
               
