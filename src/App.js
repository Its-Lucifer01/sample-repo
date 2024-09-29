import React from 'react';
import { BrowserRouter, Route, Routes, Link } from 'react-router-dom';
import './App.css';
import About from './Components/About';
import Dashboard from './Components/Dashboard';
import Food_distribution from "./Components/Food_distribution";
import optimization from "./Components/optimization";

const App = () => {
  return (
    <BrowserRouter>
      <div className="bg-purple-700 text-white min-h-screen flex flex-col">
        {/* Header */}
        <header className="flex justify-between items-center p-6">
          <div className="flex items-center space-x-2">
            <div className="bg-green-500 w-8 h-8 rounded-full"></div>
            <span className="text-xl font-bold">NourishAI</span>
          </div>
          <nav className="space-x-6">
            <Link to="/" className="hover:underline">
              About
            </Link>
            <Link to="/dashboard" className="hover:underline">
              Dashboard
            </Link>
            <Link to="/food-distribution" className="hover:underline">
              Food Distribution
            </Link>
            <Link to="/optimization" className="hover:underline">
              Optimization
            </Link>
          </nav>
        </header>

        {/* Main Content Area for Routing */}
        <main className="flex-grow p-6">
          <Routes>
            <Route path="/" element={<About />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/Food_distribution" element={<Food_distribution />} />
            <Route path="/optimization" element={<optimization />} />
          </Routes>
        </main>

        {/* Footer */}
        <footer className="bg-purple-900 text-white py-8">
          <div className="text-center">
            <p>&copy; 2023 NourishAI. All rights reserved.</p>
          </div>
        </footer>
      </div>
    </BrowserRouter>
  );
}

export default App;