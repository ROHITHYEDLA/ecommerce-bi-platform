import {
  BrowserRouter,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";

import Login from "../pages/auth/Login";

function Dashboard() {
  return (
    <div className="min-h-screen bg-slate-100 p-10">
      <h1 className="text-3xl font-bold text-slate-900">
        BI Dashboard
      </h1>

      <p className="mt-2 text-slate-600">
        Welcome to the E-Commerce BI Platform.
      </p>
    </div>
  );
}

function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>

        <Route
          path="/login"
          element={<Login />}
        />

        <Route
          path="/dashboard"
          element={<Dashboard />}
        />

        <Route
          path="*"
          element={
            <Navigate
              to="/login"
              replace
            />
          }
        />

      </Routes>
    </BrowserRouter>
  );
}

export default AppRoutes;