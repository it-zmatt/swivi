import { useState } from 'react'
import Hero from "./components/Hero";
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
	<div className="min-h-screen">
		<Hero />
	</div>
  )
}

export default App
