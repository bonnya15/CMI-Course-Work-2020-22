SELECT MAX(lettergrade) 
FROM registration r,grade g WHERE r.rid = g.rid 
AND r.cid = "RSV" GROUP BY lettergrade;

SELECT sname FROM student s, registration r,grade g 
WHERE s.rollno = g.rollno AND r.rid = g.rid AND r.semester = "Oct-Nov" AND g.lettergrade = 'F';

SELECT MAX (cidcount) 
FROM (SELECT COUNT(cid) cidcount 
FROM registration 
GROUP BY cid);

UPDATE course c, registration r
SET cid = "SQL"
WHERE c.cid = r.cid AND cid = "RSV";

INSERT INTO course values("RSV2","RDBMS, SQL and Visualization 2");

INSERT INTO registration(cid, year, semester, rollno) values("RSV2",2021,"Feb-Mar", "MDS201905");