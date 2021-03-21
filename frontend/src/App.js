import React, {useState} from 'react'
import axios from 'axios'
import './App.css';


function App() {
  let [data,setData] = useState('Hello');
  axios.get('http://127.0.0.1:8000/users/user-list/',{
    headers:{
      'Content-Type':'application/json'
    }
  })
  .then(res => {
    console.log(res.data);
    setData(res.data);
  });
    return (
      <h1>{data}</h1>
    );
}

export default App;
