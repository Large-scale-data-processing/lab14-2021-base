import logo from './logo.svg';
import './App.css';

import {
  ApolloClient,
  InMemoryCache,
  ApolloProvider,
  useQuery,
  gql
} from "@apollo/client";

const client = new ApolloClient({
  uri: '/graphql',
  cache: new InMemoryCache()
});

const HELLO_QUERY = gql`
  query GetHelloData {
    hello
  }
`;

function HelloData() {
  const { loading, error, data } = useQuery(HELLO_QUERY);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;
  let {hello} = data
  return (<p>
        {hello}
      </p>)
}

function App() {
  return (

  <ApolloProvider client={client}>
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <HelloData/>
        </header>
      </div>
  </ApolloProvider>
  );
}

export default App;
