import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { UserCircleIcon, BriefcaseIcon } from '@heroicons/react/24/outline';
import { getEmployees } from '../services/api';

function EmployeeList() {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchEmployees = async () => {
      try {
        setLoading(true);
        const data = await getEmployees();
        console.log('Fetched employees:', data);
        if (Array.isArray(data)) {
          setEmployees(data);
          setError(null);
        } else {
          setError('Invalid data format received from server');
        }
      } catch (err) {
        console.error('Error fetching employees:', err);
        setError('Failed to fetch employees. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchEmployees();
  }, []);

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

  if (!employees || employees.length === 0) {
    return (
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-2xl font-bold text-gray-900 mb-6">Employees</h1>
        <div className="text-center text-gray-600">No employees found.</div>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-2xl font-bold text-gray-900 mb-6">Employees</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {employees.map((employee) => (
          <Link
            key={employee.id}
            to={`/employee/${employee.id}`}
            className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300"
          >
            <div className="p-6">
              <div className="flex items-start justify-between mb-4">
                <div className="flex items-center">
                  <UserCircleIcon className="h-12 w-12 text-gray-700 mr-4" />
                  <div>
                    <h2 className="text-xl font-semibold text-gray-900">
                      {employee.user?.first_name} {employee.user?.last_name}
                    </h2>
                    <p className="text-gray-600">{employee.designation}</p>
                  </div>
                </div>
              </div>
              
              <div className="mt-4 space-y-3">
                <div className="flex items-center text-sm text-gray-500">
                  <BriefcaseIcon className="h-5 w-5 mr-2" />
                  <span>{employee.organization?.name}</span>
                </div>
                <div className="flex items-center text-sm text-gray-500">
                  <span className="px-2 py-1 text-xs rounded-full bg-gray-100">
                    {employee.employee_type?.replace('_', ' ')}
                  </span>
                </div>
              </div>

              <div className="mt-4 pt-4 border-t border-gray-100">
                <div className="text-sm text-gray-500">
                  <span className="font-medium text-gray-700">Joined: </span>
                  {employee.date_joined && new Date(employee.date_joined).toLocaleDateString()}
                </div>
              </div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}

export default EmployeeList;
