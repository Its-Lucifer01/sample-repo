import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { FaChartLine, FaUsers, FaCog, FaClipboardList } from 'react-icons/fa';
import { FiTrendingUp } from 'react-icons/fi';
import axios from 'axios';
import chart from 'chart.js';

const Dashboard = () => {
  const [revenueTrend, setRevenueTrend] = useState([]);
  const [userGrowth, setUserGrowth] = useState([]);
  const [ghgEmissions, setGhgEmissions] = useState([]);
  // ...

  useEffect(() => {
    axios.get('/api/charts')
      .then(response => {
        setRevenueTrend(response.data.revenueTrend);
        setUserGrowth(response.data.userGrowth);
        setGhgEmissions(response.data.ghgEmissions);
        // ...
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      {/* Header */}
      <header className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-800">Dashboard</h1>
          <p className="text-gray-500">Welcome back, User!</p>
        </div>
        <button className="bg-blue-600 text-white px-4 py-2 rounded-lg shadow hover:bg-blue-700 transition duration-200">
          Update Data
        </button>
      </header>

      {/* Charts and Details Section */}
      <section className="mt-10 grid grid-cols-1 lg:grid-cols-2 gap-6">
        <motion.div
          className="bg-white p-6 rounded-lg shadow"
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
        >
          <h2 className="text-xl font-semibold mb-4">Revenue Trend</h2>
          <div className="h-64 bg-blue-100 rounded-lg">
            <Chart
              type="line"
              data={{
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
                datasets: [{
                  label: 'Revenue Trend',
                  data: revenueTrend,
                  backgroundColor: 'rgba (255, 99, 132, 0.2)',
                  borderColor: 'rgba(255, 99, 132, 1)',
                  borderWidth: 1
                }]
              }}
              options={{
                scales: {
                  yAxes: [{
                    ticks: {
                      beginAtZero: true
                    }
                  }]
                }
              }}
            />
          </div>
        </motion.div>

        <motion.div
          className="bg-white p-6 rounded-lg shadow"
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7 }}
        >
          <h2 className="text-xl font-semibold mb-4">User Growth</h2>
          <div className="h-64 bg-green-100 rounded-lg">
            <Chart
              type="line"
              data={{
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
                datasets: [{
                  label: 'User Growth',
                  data: userGrowth,
                  backgroundColor: 'rgba(54, 162, 235, 0.2)',
                  borderColor: 'rgba(54, 162, 235, 1)',
                  borderWidth: 1
                }]
              }}
              options={{
                scales: {
                  yAxes: [{
                    ticks: {
                      beginAtZero: true
                    }
                  }]
                }
              }}
            />
          </div>
        </motion.div>
      </section>

      {/* Sustainability Section */}
      <section className="mt-10 grid grid-cols-1 lg:grid-cols-2 gap-6">
        <motion.div
          className="bg-white p-6 rounded-lg shadow"
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
        >
          <h2 className="text-xl font-semibold mb-4">GHG Emissions</h2>
          <div className="h-64 bg-blue-100 rounded-lg">
            <Chart
              type="bar"
              data={{
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
                datasets: [{
                  label: 'GHG Emissions',
                  data: ghgEmissions,
                  backgroundColor: 'rgba(255, 99, 132, 0.2)',
                  borderColor: 'rgba(255, 99, 132, 1)',
                  borderWidth: 1
                }]
              }}
              options={{
                scales: {
                  yAxes: [{
                    ticks: {
                      beginAtZero: true
                    }
                  }]
                }
              }}
            />
          </div>
        </motion.div>

        <motion.div
          className="bg-white p-6 rounded-lg shadow"
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7 }}
        >
          <h2 className="text-xl font-semibold mb-4">Total Emissions</h2>
          <div className="h-64 bg-green-100 rounded-lg">
            <Chart
              type="bar"
              data={{
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
                datasets: [{
                  label: 'Total Emissions',
                  data: totalEmissions,
                  backgroundColor: 'rgba(54, 162, 235, 0.2)',
                  borderColor: 'rgba(54, 162, 235, 1)',
                  borderWidth: 1
                }]
              }}
              options={{
                scales: {
                  yAxes: [{
                    ticks: {
                      beginAtZero: true
                    }
                  }]
                }
              }}
            />
          </div>
        </motion.div>
      </section>
    </div>
  );
};

export default Dashboard;