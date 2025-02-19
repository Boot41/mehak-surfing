import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import EmployeeList from './pages/EmployeeList';
import AssignmentList from './pages/AssignmentList';
import EmployeeProfile from './pages/EmployeeProfile';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <Navbar />
        <div className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
          <Routes>
            <Route path="/" element={<EmployeeList />} />
            <Route path="/assignments" element={<AssignmentList />} />
            <Route path="/employee/:id" element={<EmployeeProfile />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
