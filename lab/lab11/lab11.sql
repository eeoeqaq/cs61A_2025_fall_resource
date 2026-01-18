CREATE table newest AS
  SELECT titles.title,titles.year
  FROM titles
  ORDER BY titles.year DESC
  LIMIT 10;


CREATE table dog_movies AS 
  SELECT titles.title,principals.character
  FROM titles
  JOIN principals ON titles.tconst = principals.tconst
  WHERE principals.character LIKE '%dog%';


CREATE table leads AS 
  SELECT names.name , COUNT(*) AS lead_roles
  FROM names
  JOIN principals ON names.nconst = principals.nconst
  WHERE principals.ordering = 1 
  GROUP BY principals.nconst
  HAVING COUNT(*)>10;


CREATE table long_movies AS 
  SELECT (titles.year/10*10)||'s' AS decade,count(*) AS count
  FROM titles
  WHERE titles.runtime>180
  GROUP BY titles.year/10*10
  HAVING count(*)>0
  ;

