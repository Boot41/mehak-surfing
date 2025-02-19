import React, { useState, useEffect } from 'react';
import { getAssignments } from '../services/api';

function AssignmentList() {
  const [assignments, setAssignments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const data = await getAssignments();
        console.log('Assignments data:', data);
        if (Array.isArray(data)) {
          setAssignments(data);
          setError(null);
        } else {
          setError('Invalid data format received from server');
          console.error('Invalid assignments data format:', data);
        }
      } catch (err) {
        console.error('Error fetching assignments:', err);
        setError('Failed to fetch assignments. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const getStatusColor = (status) => {
    switch (status) {
      case 'IN_PROGRESS':
        return 'bg-yellow-100 text-yellow-800';
      case 'COMPLETED':
        return 'bg-green-100 text-green-800';
      case 'NOT_STARTED':
        return 'bg-gray-100 text-gray-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-gray-800"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-red-600 text-center">
          <p className="text-xl font-semibold mb-2">Error</p>
          <p>{error}</p>
        </div>
      </div>
    );
  }

  if (!assignments || assignments.length === 0) {
    return (
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-2xl font-bold text-gray-900 mb-6">Assignments</h1>
        <div className="text-center text-gray-600">No assignments found.</div>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-2xl font-bold text-gray-900 mb-6">Assignments</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {assignments.map((assignment) => (
          <div
            key={assignment.id}
            className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300"
          >
            <div className="p-6 flex flex-col h-full">
              <div className="flex justify-between items-start mb-4">
                <h2 className="text-xl font-semibold text-gray-900">
                  {assignment.title}
                </h2>
                <span
                  className={`px-2 py-1 text-xs rounded-full ${getStatusColor(
                    assignment.status
                  )}`}
                >
                  {assignment.status?.replace('_', ' ')}
                </span>
              </div>
              <p className="text-gray-600 mb-4 flex-grow">
                {assignment.description}
              </p>
              <div className="grid grid-cols-2 gap-4 mt-4 pt-4 border-t border-gray-100">
                <div className="text-sm text-gray-500">
                  <div className="font-medium text-gray-700">Start</div>
                  {assignment.start_date && new Date(assignment.start_date).toLocaleDateString()}
                </div>
                <div className="text-sm text-gray-500">
                  <div className="font-medium text-gray-700">End</div>
                  {assignment.end_date && new Date(assignment.end_date).toLocaleDateString()}
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default AssignmentList;
