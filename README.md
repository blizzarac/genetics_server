# graphql-nodejs-newsfeed
Example of graphql nodejs backend with newsfeed, built with hapi and sqlite

## Set Up Database

```
$ sqlite3 db.sqlite3 < scripts/createdb.sql
```

## Init Database with genome file

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
$ curl --data "query={ __schema { types { name } } }" localhost:8000
```
