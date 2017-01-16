DROP TABLE IF EXISTS Snp;


CREATE TABLE SNP
(
  rsid VARCHAR(255),
  chromosome VARCHAR(5),
  position INTEGER,
  genotype VARCHAR(50)
);