# Genetics Server
GraphQL server for queuering genetic data from an Sqlite database

## Set Up Database

```
$ sqlite3 db.sqlite3 < scripts/createdb.sql
```

## Init Database with a 23andme genome file

```
$ python initdb.py db.sqlite3 genome_*.txt
```

## Set Up Server
```
$ npm install
```

## Run Server

```
$ npm start
```

## Example Query

```
$ curl --data "query={ snps(rsid: \"rs10865306\"){rsid, position, genotype, chromosome} }" localhost:8000
```
