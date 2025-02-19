// Mock data for development and testing
export const organizations = [
  {
    id: 1,
    name: "Tech Solutions Inc",
    description: "Leading tech company",
    address: "123 Tech Street, Silicon Valley",
    contactEmail: "contact@techsolutions.com",
    contactPhone: "+1-555-0123"
  },
  {
    id: 2,
    name: "Digital Innovations",
    description: "Digital transformation company",
    address: "456 Innovation Ave, New York",
    contactEmail: "info@digitalinnovations.com",
    contactPhone: "+1-555-0456"
  }
];

export const users = [
  {
    id: 1,
    username: "john.doe",
    firstName: "John",
    lastName: "Doe",
    email: "john.doe@example.com",
    isActive: true,
    isStaff: false,
    dateJoined: "2025-02-18T11:33:20+05:30"
  },
  {
    id: 2,
    username: "jane.smith",
    firstName: "Jane",
    lastName: "Smith",
    email: "jane.smith@example.com",
    isActive: true,
    isStaff: false,
    dateJoined: "2025-02-18T11:33:20+05:30"
  }
];

export const employees = [
  {
    id: 1,
    userId: 1,
    organizationId: 1,
    employeeType: "FULL_TIME",
    designation: "Senior Developer",
    dateJoined: "2025-01-01"
  },
  {
    id: 2,
    userId: 2,
    organizationId: 2,
    employeeType: "PART_TIME",
    designation: "Project Manager",
    dateJoined: "2025-01-15"
  }
];

export const assignments = [
  {
    id: 1,
    title: "Web Application Development",
    description: "Develop a new web application using Django",
    startDate: "2025-02-01",
    endDate: "2025-04-01",
    status: "IN_PROGRESS"
  },
  {
    id: 2,
    title: "Mobile App Design",
    description: "Design UI/UX for mobile application",
    startDate: "2025-02-15",
    endDate: "2025-03-15",
    status: "NOT_STARTED"
  }
];

export const assignmentAllocations = [
  {
    id: 1,
    employeeId: 1,
    assignmentId: 1,
    startDate: "2025-02-01",
    endDate: "2025-04-01",
    status: "ACTIVE"
  },
  {
    id: 2,
    employeeId: 2,
    assignmentId: 2,
    startDate: "2025-02-15",
    endDate: "2025-03-15",
    status: "PENDING"
  }
];
