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
        console.log(data)
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
    <div className='w-full h-full'>


    <div className='flex flex-col w-full h-fit mb-[3%]'>

    <h1 className='text-7xl pb-4'> AI Content Moderation System Project</h1>

    <div className='flex flex-row items-center justify-center space-x-4'>
      <h1 className='text-xl'> Eric Asante </h1>
      <h1 className='text-center'>*</h1>
      <h1 className='text-xl'> Ethan Thomas </h1>
      <h1>*</h1>
      <h1 className='text-xl'> Colin Hong </h1>
      <h1>*</h1>
      <h1 className='text-xl'> Eli Perchenok </h1>
    </div>
    </div>



    <div className='flex-1 flex  w-full flex-col items-center justify-center '>

      <form onSubmit={handleSubmit} className='border-1 border-white rounded-lg w-full space-y-4 p-4'>
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

        <button type="submit" className='w-full' >
          Submit
        </button>
        <div className='w-full'>
        <h1 className=' w-full text-center text-xl'>-- Prediction --</h1>

        <h1 className='h-12 w-full text-center text-6xl mb-4'>{dataresponse[2]}</h1>
        </div>



      </form>
      <div className='h-full w-full'>
        <h1 className='h-12 w-full text-center'>Accuracy Score: { Number((dataresponse[0] * 100).toPrecision(7))}</h1>
        <pre className='h-full w-full text-center whitespace-pre-line'>{dataresponse[1]}</pre>

        </div>
      

    </div>

    </div>


  )
}

export default App
