CREATE TABLE cats (
  name TEXT,
  breed TEXT,
  age INTEGER
);

INSERT INTO cats (name, breed, age) VALUES (
  "Minnie",
  "Tabby",
  10
);

SELECT * FROM cats;
SELECT name,breed FROM cats;
SELECT * FROM cats WHERE name IS "Minnie";
SELECT * FROM cats WHERE breed IS NOT "Spooky";
SELECT * FROM cats WHERE breed IS NOT "Spooky" AND age IS NOT 4;
SELECT * FROM cats WHERE breed IS NOT "Spooky" AND age > 5;
SELECT * FROM cats WHERE name LIKE "%nn%";
