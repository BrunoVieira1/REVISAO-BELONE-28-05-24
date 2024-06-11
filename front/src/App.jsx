import { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  function getData() {
    try {
      setTimeout(async () => {
        const response = await axios.get("http://localhost:3000/clientes");
        setData(response.data.clientes);
        setLoading(false);
        console.log(response.data.clientes);
      }, 1000);
    } catch (e) {
      console.log(e);
    }
  }
  useEffect(() => {
    getData();
  }, []);

  return (
    <div>
      <h1> Lista de clientes </h1>
      {loading && data.length <= 0 ? (
        <p> Carregando... </p>
      ) : (
        data.map((cliente) => {
          return (
            <div key={cliente.nome}>
              <p>
                {cliente.nome} {cliente.email}{" "}
              </p>
            </div>
          );
        })
      )}
    </div>
  );
}
export default App;
