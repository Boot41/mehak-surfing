import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { 
  UserCircleIcon,
  BriefcaseIcon,
  AcademicCapIcon,
} from '@heroicons/react/24/outline';
import { getEmployee } from '../services/api';

function EmployeeProfile() {
  const { id } = useParams();
  const [employeeData, setEmployeeData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchEmployeeData();
  }, [id]);

  const fetchEmployeeData = async () => {
    try {
      setLoading(true);
      const data = await getEmployee(id);
      setEmployeeData(data);
      setError(null);
    } catch (err) {
      setError('Failed to fetch employee data. Please try again later.');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  const getStatusColor = (status) => {
    switch (status) {
      case 'IN_PROGRESS':
        return 'bg-gray-200 text-gray-800 border border-gray-300';
      case 'COMPLETED':
        return 'bg-black text-white border border-gray-700';
      case 'NOT_STARTED':
        return 'bg-gray-100 text-gray-700 border border-gray-200';
      case 'ACTIVE':
        return 'bg-black text-white border border-gray-700';
      case 'PENDING':
        return 'bg-gray-200 text-gray-800 border border-gray-300';
      default:
        return 'bg-gray-100 text-gray-700 border border-gray-200';
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

  if (!employeeData) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-gray-600 text-center">
          <p className="text-xl font-semibold">Employee Not Found</p>
        </div>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="bg-white shadow-lg rounded-xl overflow-hidden">
        {/* Header Section */}
        <div className="p-6 bg-gray-100 border-b border-gray-200">
          <div className="flex items-center space-x-4">
            <UserCircleIcon className="h-16 w-16 text-gray-700" />
            <div>
              <h1 className="text-2xl font-bold text-gray-900">
                {employeeData.user.first_name} {employeeData.user.last_name}
              </h1>
              <p className="text-gray-700 font-medium">{employeeData.designation}</p>
              <p className="text-gray-600">{employeeData.organization.name}</p>
            </div>
          </div>
        </div>

        {/* Info Section - Horizontal Layout */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 p-6">
          {/* Personal Information */}
          <div className="bg-white rounded-lg p-6 border border-gray-200">
            <h2 className="text-lg font-semibold text-gray-900 flex items-center mb-4">
              <UserCircleIcon className="h-5 w-5 mr-2 text-gray-700" />
              Personal Information
            </h2>
            <dl className="grid grid-cols-2 gap-4">
              <div>
                <dt className="text-sm font-medium text-gray-500">Email</dt>
                <dd className="mt-1 text-sm text-gray-900">{employeeData.user.email}</dd>
              </div>
              <div>
                <dt className="text-sm font-medium text-gray-500">Username</dt>
                <dd className="mt-1 text-sm text-gray-900">{employeeData.user.username}</dd>
              </div>
              <div>
                <dt className="text-sm font-medium text-gray-500">Date Joined</dt>
                <dd className="mt-1 text-sm text-gray-900">
                  {new Date(employeeData.date_joined).toLocaleDateString()}
                </dd>
              </div>
              <div>
                <dt className="text-sm font-medium text-gray-500">Employment Type</dt>
                <dd className="mt-1 text-sm text-gray-900">{employeeData.employee_type.replace('_', ' ')}</dd>
              </div>
            </dl>
          </div>

          {/* Organization Details */}
          <div className="bg-white rounded-lg p-6 border border-gray-200">
            <h2 className="text-lg font-semibold text-gray-900 flex items-center mb-4">
              <BriefcaseIcon className="h-5 w-5 mr-2 text-gray-700" />
              Organization Details
            </h2>
            <dl className="grid grid-cols-2 gap-4">
              <div>
                <dt className="text-sm font-medium text-gray-500">Company</dt>
                <dd className="mt-1 text-sm text-gray-900">{employeeData.organization.name}</dd>
              </div>
              <div>
                <dt className="text-sm font-medium text-gray-500">Address</dt>
                <dd className="mt-1 text-sm text-gray-900">{employeeData.organization.address}</dd>
              </div>
              <div>
                <dt className="text-sm font-medium text-gray-500">Contact Email</dt>
                <dd className="mt-1 text-sm text-gray-900">{employeeData.organization.contact_email}</dd>
              </div>
              <div>
                <dt className="text-sm font-medium text-gray-500">Contact Phone</dt>
                <dd className="mt-1 text-sm text-gray-900">{employeeData.organization.contact_phone}</dd>
              </div>
            </dl>
          </div>
        </div>

        {/* Assignments Section - Table View */}
        <div className="p-6 border-t border-gray-200">
          <h2 className="text-lg font-semibold text-gray-900 flex items-center mb-4">
            <AcademicCapIcon className="h-5 w-5 mr-2 text-gray-700" />
            Current Assignments
          </h2>
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gray-50">
                <tr>
                  <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Title
                  </th>
                  <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Description
                  </th>
                  <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Status
                  </th>
                  <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    Start Date
                  </th>
                  <th scope="col" className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                    End Date
                  </th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {employeeData.assignments.map((assignment) => (
                  <tr key={assignment.id} className="hover:bg-gray-50">
                    <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                      {assignment.title}
                    </td>
                    <td className="px-6 py-4 text-sm text-gray-500">
                      {assignment.description}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <span className={`px-2 py-1 text-xs rounded-full ${getStatusColor(assignment.status)}`}>
                        {assignment.status.replace('_', ' ')}
                      </span>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {new Date(assignment.start_date).toLocaleDateString()}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {new Date(assignment.end_date).toLocaleDateString()}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}

export default EmployeeProfile;
