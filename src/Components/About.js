import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './About.css';
import ReactDOM from 'react-dom';

const About = () => {
  const [data, setData] = useState(null); // State to store the fetched data
  const [loading, setLoading] = useState(true); // State to manage loading state

  // Function to fetch data from the Flask backend
  const fetchData = async () => {
    try {
      const response = await axios.get('http://localhost:5000/api/data'); // Replace with your Flask API endpoint
      setData(response.data);
      setLoading(false);
    } catch (error) {
      console.error("Error fetching data:", error);
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="bg-white text-gray-800">
      <main className="text-center py-20">
        <h1 className="text-5xl font-bold mb-4">Clean Energy for Everyday Life and Future</h1>
        <p className="text-lg mb-8">Our methodology opens up a better and cleaner path towards every consumer.</p>
        <button className="bg-green-500 text-white py-2 px-6 rounded font-bold transition duration-300 ease-in-out transform hover:bg-green-600 hover:scale-105 focus:outline-none focus:ring-2 focus:ring-green-300 focus:ring-opacity-50">
          Get Started
        </button>
      </main>

      <section className="flex justify-center items-center py-20 bg-gray-200">
        <div className="relative">
          <div className="absolute top-0 left-0 w-32 h-32 bg-white opacity-20"></div>
          <img src="https://www.shutterstock.com/image-photo/professional-male-bioengineer-examining-crops-on-modern-2309770999" alt="Person smiling and holding a plant" className="relative z-10 rounded-full"/>
        </div>
        <div className="ml-8 text-left">
          <h2 className="text-2xl font-bold mb-2">Safe and Better Energy Without Pollution</h2>
        </div>
      </section>

      <section className="grid grid-cols-1 sm:grid-cols-3 gap-4 py-20">
        <div className="bg-gray-300 text-black p-8 text-center">
          <h3 className="text-4xl font-bold">{data ? data.energySaved : "Loading..."}</h3>
          <p>Energy Saved</p>
        </div>
        <div className="bg-gray-300 text-black p-8 text-center">
          <h3 className="text-4xl font-bold">{data ? data.lessPollution : "Loading..."}</h3>
          <p>Less Pollution</p>
        </div>
        <div className="bg-gray-300 text-black p-8 text-center">
          <h3 className="text-4xl font-bold">{data ? data.happyClients : "Loading..."}</h3>
          <p>Happy Clients</p>
        </div>
      </section>

      <section className="grid grid-cols-1 md:grid-cols-2 gap-4 py-20">
        <div>
          <img src="https://placehold.co/600x400" alt="Beautiful landscape with mountains and lake" className="w-full h-full object-cover"/>
        </div>
        <div className="bg-gray-200 text-black p-8">
          <h2 className="text-2xl font-bold mb-4">Our Mission</h2>
          <p>Our Green Mission is to make a positive impact on the environment and the future of our planet. We are ready to help you with all setup and installation processes.</p>
        </div>
      </section>

      <footer className="bg-gray-300 text-black py-8">
        <div className="text-center">
          <p className="font-bold text-lg">SAVE FOOD</p>
        </div>
      </footer>
    </div>
  );
};

ReactDOM.render(<About />, document.getElementById('root'));

export default About;
