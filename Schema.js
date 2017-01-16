import {
  GraphQLSchema,
  GraphQLObjectType,
  GraphQLID,
  GraphQLString,
  GraphQLNonNull,
  GraphQLList
} from 'graphql';

const Snp = new GraphQLObjectType({
  name: 'Snp',
  fields: () => ({
    rsid: {
      type: GraphQLString
    },
    chromosome: {
      type: GraphQLString
    },
    position: {
      type: GraphQLString
    },
    genotype: {
      type: GraphQLString
    }
  })
});

const Query = new GraphQLObjectType({
  name: 'Query',
  fields: () => ({
    snps: {
      type: Snp,
      args: {
        rsid: {
          type: new GraphQLNonNull(GraphQLString)
        }
      },
      resolve(parent, {rsid}, {rootValue: {db}}) {
        return db.get(`
          SELECT * FROM Snp WHERE rsid = $rsid
        `, {$rsid: rsid});
      }
    }
  })
});

const Schema = new GraphQLSchema({
  query: Query
});
export default Schema;
