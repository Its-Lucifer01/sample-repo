import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { motion } from 'framer-motion';
import { Tailwind } from 'tailwindcss';

const Optimization = () => {
  const [optimizationData, setOptimizationData] = useState({});

  useEffect(() => {
    axios.get('/api/optimization')
      .then(response => {
        setOptimizationData(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <motion.div
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="container mx-auto p-4 pt-6"
    >
      <h1 className="text-3xl font-bold mb-4">Optimization</h1>
      <ul>
        {optimizationData.data.map(item => (
          <motion.li
            key={item.id}
            initial={{ opacity: 0, y: 50 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.2 }}
            className="bg-white shadow-md rounded px-4 py-2 mb-4"
          >
            <p className="text-lg font-bold mb-2">{item.technique}</p>
            <p className="text-gray-600">{item.result}</p>
          </motion.li>
        ))}
      </ul>
    </motion.div>
  );
};

export default Optimization;