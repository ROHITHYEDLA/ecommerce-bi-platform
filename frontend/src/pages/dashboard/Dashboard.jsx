import {
  FiDollarSign,
  FiShoppingCart,
  FiUsers,
  FiPackage,
} from "react-icons/fi";

import KPICard from "../../components/cards/KPICard";
import InventoryCard from "../../components/cards/InventoryCard";
import ProcurementCard from "../../components/cards/ProcurementCard";

import SalesChart from "../../components/charts/SalesChart";
import InventoryChart from "../../components/charts/InventoryChart";

import RecentOrdersTable from "../../components/tables/RecentOrdersTable";

function Dashboard() {
  return (
    <div className="space-y-6">

      {/* Header */}

      <div>
        <h1 className="text-2xl font-bold text-slate-900">
          Dashboard
        </h1>

        <p className="mt-1 text-sm text-slate-500">
          Overview of your business performance
        </p>
      </div>

      {/* KPI Cards */}

      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 xl:grid-cols-4">

        <KPICard
          title="Total Sales"
          value="₹12.4 L"
          change="+12.5%"
          icon={<FiDollarSign size={22} />}
        />

        <KPICard
          title="Total Orders"
          value="1,284"
          change="+8.2%"
          icon={<FiShoppingCart size={22} />}
        />

        <KPICard
          title="Customers"
          value="3,842"
          change="+15.4%"
          icon={<FiUsers size={22} />}
        />

        <KPICard
          title="Inventory Value"
          value="₹28.6 L"
          change="-3.2%"
          positive={false}
          icon={<FiPackage size={22} />}
        />

      </div>

      {/* Charts */}

      <div className="grid grid-cols-1 gap-6 xl:grid-cols-3">

        <div className="xl:col-span-2">
          <SalesChart />
        </div>

        <InventoryChart />

      </div>

      {/* Inventory + Procurement */}

      <div className="grid grid-cols-1 gap-6 lg:grid-cols-2">

        <InventoryCard />

        <ProcurementCard />

      </div>

      {/* Recent Orders */}

      <RecentOrdersTable />

    </div>
  );
}

export default Dashboard;