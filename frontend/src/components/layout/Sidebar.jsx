import { NavLink } from "react-router-dom";
import {
  FiGrid,
  FiPackage,
  FiUsers,
  FiShoppingCart,
  FiBox,
  FiTruck,
  FiCreditCard,
  FiBarChart2,
  FiFileText,
  FiSettings,
  FiChevronDown,
} from "react-icons/fi";
import { useState } from "react";

function Sidebar() {
  const [masterOpen, setMasterOpen] = useState(true);
  const [operationsOpen, setOperationsOpen] = useState(true);

  const linkClass = ({ isActive }) =>
    `flex items-center gap-3 rounded-lg px-4 py-3 text-sm font-medium transition ${
      isActive
        ? "bg-blue-600 text-white"
        : "text-slate-300 hover:bg-slate-800 hover:text-white"
    }`;

  return (
    <aside className="fixed left-0 top-0 z-40 flex h-screen w-64 flex-col bg-slate-950 text-white">

      {/* Logo */}

      <div className="flex h-16 items-center border-b border-slate-800 px-6">
        <div>
          <h1 className="text-xl font-bold">
            E-Commerce BI
          </h1>

          <p className="text-xs text-slate-400">
            Intelligence Platform
          </p>
        </div>
      </div>

      {/* Navigation */}

      <nav className="flex-1 overflow-y-auto p-4">

        {/* Dashboard */}

        <NavLink
          to="/dashboard"
          className={linkClass}
        >
          <FiGrid size={18} />
          Dashboard
        </NavLink>

        {/* Master Data */}

        <button
          onClick={() => setMasterOpen(!masterOpen)}
          className="mt-4 flex w-full items-center justify-between rounded-lg px-4 py-3 text-sm font-medium text-slate-300 hover:bg-slate-800 hover:text-white"
        >
          <span className="flex items-center gap-3">
            <FiPackage size={18} />
            Master Data
          </span>

          <FiChevronDown
            className={`transition ${
              masterOpen ? "rotate-180" : ""
            }`}
          />
        </button>

        {masterOpen && (
          <div className="ml-4 mt-1 space-y-1 border-l border-slate-700 pl-3">

            <NavLink
              to="/products"
              className={linkClass}
            >
              Products
            </NavLink>

            <NavLink
              to="/suppliers"
              className={linkClass}
            >
              Suppliers
            </NavLink>

            <NavLink
              to="/customers"
              className={linkClass}
            >
              Customers
            </NavLink>

            <NavLink
              to="/categories"
              className={linkClass}
            >
              Categories
            </NavLink>

          </div>
        )}

        {/* Operations */}

        <button
          onClick={() =>
            setOperationsOpen(!operationsOpen)
          }
          className="mt-4 flex w-full items-center justify-between rounded-lg px-4 py-3 text-sm font-medium text-slate-300 hover:bg-slate-800 hover:text-white"
        >
          <span className="flex items-center gap-3">
            <FiShoppingCart size={18} />
            Operations
          </span>

          <FiChevronDown
            className={`transition ${
              operationsOpen ? "rotate-180" : ""
            }`}
          />
        </button>

        {operationsOpen && (
          <div className="ml-4 mt-1 space-y-1 border-l border-slate-700 pl-3">

            <NavLink
              to="/inventory"
              className={linkClass}
            >
              <FiBox size={16} />
              Inventory
            </NavLink>

            <NavLink
              to="/procurement"
              className={linkClass}
            >
              <FiTruck size={16} />
              Procurement
            </NavLink>

            <NavLink
              to="/orders"
              className={linkClass}
            >
              Orders
            </NavLink>

            <NavLink
              to="/payments"
              className={linkClass}
            >
              <FiCreditCard size={16} />
              Payments
            </NavLink>

          </div>
        )}

        {/* Analytics */}

        <NavLink
          to="/analytics"
          className={linkClass}
        >
          <FiBarChart2 size={18} />
          Analytics
        </NavLink>

        {/* Reports */}

        <NavLink
          to="/reports"
          className={linkClass}
        >
          <FiFileText size={18} />
          Reports
        </NavLink>

        {/* Settings */}

        <NavLink
          to="/settings"
          className={linkClass}
        >
          <FiSettings size={18} />
          Settings
        </NavLink>

      </nav>

    </aside>
  );
}

export default Sidebar;