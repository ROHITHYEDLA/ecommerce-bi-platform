import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import {
  FiBell,
  FiSearch,
  FiLogOut,
  FiUser,
} from "react-icons/fi";

import { logout } from "../../store/slices/authSlice";

function Navbar() {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const user = useSelector((state) => state.auth.user);

  const handleLogout = () => {
    dispatch(logout());
    navigate("/login");
  };

  return (
    <header className="fixed left-64 right-0 top-0 z-30 h-16 border-b border-slate-200 bg-white">
      <div className="flex h-full items-center justify-between px-6">

        {/* Search */}

        <div className="relative w-96">
          <FiSearch
            className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"
            size={18}
          />

          <input
            type="text"
            placeholder="Search..."
            className="w-full rounded-lg border border-slate-200 bg-slate-50 py-2 pl-10 pr-4 text-sm outline-none focus:border-blue-500"
          />
        </div>

        {/* Right side */}

        <div className="flex items-center gap-5">

          {/* Notifications */}

          <button
            className="relative rounded-lg p-2 text-slate-500 hover:bg-slate-100"
            title="Notifications"
          >
            <FiBell size={20} />

            <span className="absolute right-1 top-1 h-2 w-2 rounded-full bg-red-500" />
          </button>

          {/* User */}

          <div className="flex items-center gap-3 border-l border-slate-200 pl-5">

            <div className="flex h-9 w-9 items-center justify-center rounded-full bg-blue-600 text-white">
              <FiUser size={18} />
            </div>

            <div className="hidden text-right md:block">
              <p className="text-sm font-semibold text-slate-800">
                {user?.username || "User"}
              </p>

              <p className="text-xs text-slate-500">
                {user?.role || "User"}
              </p>
            </div>

            <button
              onClick={handleLogout}
              className="rounded-lg p-2 text-slate-500 hover:bg-red-50 hover:text-red-600"
              title="Logout"
            >
              <FiLogOut size={19} />
            </button>

          </div>

        </div>

      </div>
    </header>
  );
}

export default Navbar;