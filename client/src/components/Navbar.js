import React from 'react';
import { Link, useLocation } from 'react-router-dom';

function Navbar() {
  const location = useLocation();

  const isActive = (path) => {
    return location.pathname === path;
  };

  return (
    <nav className="bg-black">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <span className="text-white font-bold text-xl">Think41</span>
            </div>
            <div className="hidden md:block">
              <div className="ml-10 flex items-baseline space-x-4">
                <Link
                  to="/"
                  className={`${
                    isActive('/') 
                      ? 'bg-gray-900 text-white'
                      : 'text-gray-300 hover:bg-gray-800 hover:text-white'
                  } px-3 py-2 rounded-md text-sm font-medium transition-colors duration-150`}
                >
                  Employees
                </Link>
                <Link
                  to="/assignments"
                  className={`${
                    isActive('/assignments')
                      ? 'bg-gray-900 text-white'
                      : 'text-gray-300 hover:bg-gray-800 hover:text-white'
                  } px-3 py-2 rounded-md text-sm font-medium transition-colors duration-150`}
                >
                  Assignments
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Mobile menu */}
      <div className="md:hidden">
        <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
          <Link
            to="/"
            className={`${
              isActive('/') 
                ? 'bg-gray-900 text-white'
                : 'text-gray-300 hover:bg-gray-800 hover:text-white'
            } block px-3 py-2 rounded-md text-base font-medium transition-colors duration-150`}
          >
            Employees
          </Link>
          <Link
            to="/assignments"
            className={`${
              isActive('/assignments')
                ? 'bg-gray-900 text-white'
                : 'text-gray-300 hover:bg-gray-800 hover:text-white'
            } block px-3 py-2 rounded-md text-base font-medium transition-colors duration-150`}
          >
            Assignments
          </Link>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
