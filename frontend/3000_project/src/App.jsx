import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [inputValue, setInputValue] = useState('');
  const [responseMessage, setResponseMessage] = useState('');
  const [dataresponse, setdataresponse] = useState('');


  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Prepare the data to be sent in the POST request
    const requestData = { text: inputValue };

    try {
      // Send POST request using fetch
      const response = await fetch('http://127.0.0.1:5123/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData),
      });

      // Check if the request was successful
      if (response.ok) {
        let data = await response.json();
        setdataresponse(data)
      } else {
      }
    } catch (error) {
      console.error('Error:', error);
    }

    // Reset input value after submission
    setInputValue('');
  };

  return (
    <>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <input
            type="text"
            value={inputValue}
            onChange={handleInputChange}
            placeholder="Enter text"
            className="border rounded px-3 py-2 w-full"
            required
          />
        </div>

        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
          Submit
        </button>
      </form>

      
      <h1>{dataresponse[2]}</h1>

    </>
  )
}

export default App
