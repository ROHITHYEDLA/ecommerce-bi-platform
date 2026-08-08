import { Outlet } from "react-router-dom";

import Sidebar from "../components/layout/Sidebar";
import Navbar from "../components/layout/Navbar";

function MainLayout() {
  return (
    <div className="min-h-screen bg-slate-100">

      {/* Sidebar */}
      <Sidebar />

      {/* Main Area */}
      <div className="ml-64">

        {/* Navbar */}
        <Navbar />

        {/* Page Content */}
        <main className="pt-16">
          <div className="p-6">
            <Outlet />
          </div>
        </main>

      </div>

    </div>
  );
}

export default MainLayout;