CREATE TABLE parents (parent TEXT, child TEXT);

INSERT INTO parents VALUES
  ('ace', 'bella'),
  ('ace', 'charlie'),
  ('daisy', 'hank'),
  ('finn', 'ace'),
  ('finn', 'daisy'),
  ('finn', 'ginger'),
  ('ellie', 'finn');

CREATE TABLE dogs (name TEXT, fur TEXT, height INTEGER);

INSERT INTO dogs VALUES
  ('ace',     'long',  26),
  ('bella',   'short', 52),
  ('charlie', 'long',  47),
  ('daisy',   'long',  46),
  ('ellie',   'short', 35),
  ('finn',    'curly', 32),
  ('ginger',  'short', 28),
  ('hank',    'curly', 31);

CREATE TABLE sizes (size TEXT, min INTEGER, max INTEGER);

INSERT INTO sizes VALUES
  ('toy',      24, 28),
  ('mini',     28, 35),
  ('medium',   35, 45),
  ('standard', 45, 60);


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT chi.name
  FROM parents
  JOIN dogs AS par ON parents.parent = par.name
  JOIN dogs AS chi ON parents.child = chi.name
  ORDER BY par.height DESC;
-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT dogs.name AS name, sizes.size AS size
  FROM dogs 
  JOIN sizes ON dogs.height > sizes.min AND dogs.height <= sizes.max;


-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  SELECT tab1.child AS name1, tab2.child AS name2, s1.size AS size
  FROM parents AS tab1
  JOIN parents AS tab2 ON tab1.parent = tab2.parent AND tab1.child < tab2.child
  JOIN size_of_dogs AS s1 ON s1.name = tab1.child
  JOIN size_of_dogs AS s2 ON s2.name = tab2.child
  WHERE s1.size = s2.size;


-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT 'The two siblings, ' || siblings.name1 || ' and ' || siblings.name2 || ', have the same size: ' || siblings.size AS sent
  FROM siblings;

-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT dogs.fur ,max(height)-min(height) AS height_range
  FROM dogs
  GROUP BY fur
  HAVING max(height)<1.3*avg(height)+1 AND min(height)>0.7*avg(height);

