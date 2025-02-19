import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

console.log('Using API URL:', API_BASE_URL);

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add response interceptor for debugging
api.interceptors.response.use(
  (response) => {
    console.log(`API Response [${response.config.method}] ${response.config.url}:`, response.data);
    return response;
  },
  (error) => {
    console.error('API Error:', {
      url: error.config?.url,
      method: error.config?.method,
      status: error.response?.status,
      data: error.response?.data,
    });
    return Promise.reject(error);
  }
);

const extractData = (response) => {
  // Handle responses that have a nested data structure
  if (response.data?.status === 'success' && response.data?.data) {
    return response.data.data;
  }
  // Handle responses that return data directly
  if (Array.isArray(response.data)) {
    return response.data;
  }
  // Handle single object responses
  if (response.data && typeof response.data === 'object') {
    return response.data;
  }
  return null;
};

export const getEmployees = async () => {
  try {
    const response = await api.get('/api/employees/');
    const data = extractData(response);
    return Array.isArray(data) ? data : [];
  } catch (error) {
    console.error('Error fetching employees:', error);
    throw error;
  }
};

export const getEmployee = async (id) => {
  try {
    const response = await api.get(`/api/employees/${id}/`);
    return extractData(response);
  } catch (error) {
    console.error('Error fetching employee:', error);
    throw error;
  }
};

export const getAssignments = async () => {
  try {
    const response = await api.get('/api/assignments/');
    const data = extractData(response);
    return Array.isArray(data) ? data : [];
  } catch (error) {
    console.error('Error fetching assignments:', error);
    throw error;
  }
};

export const getAssignment = async (id) => {
  try {
    const response = await api.get(`/api/assignments/${id}/`);
    return extractData(response);
  } catch (error) {
    console.error('Error fetching assignment:', error);
    throw error;
  }
};
