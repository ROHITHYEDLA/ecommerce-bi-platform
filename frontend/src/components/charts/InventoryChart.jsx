import {
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
} from "recharts";

const inventoryData = [
  {
    name: "In Stock",
    value: 720,
  },
  {
    name: "Low Stock",
    value: 180,
  },
  {
    name: "Out of Stock",
    value: 65,
  },
];

const COLORS = [
  "#10b981",
  "#f59e0b",
  "#ef4444",
];

function InventoryChart() {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">

      <div className="mb-4">
        <h2 className="text-lg font-bold text-slate-900">
          Inventory Health
        </h2>

        <p className="mt-1 text-sm text-slate-500">
          Current inventory distribution
        </p>
      </div>

      <div className="h-80 w-full">
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>

            <Pie
              data={inventoryData}
              cx="50%"
              cy="45%"
              innerRadius={65}
              outerRadius={105}
              paddingAngle={4}
              dataKey="value"
            >
              {inventoryData.map((entry, index) => (
                <Cell
                  key={`cell-${index}`}
                  fill={COLORS[index]}
                />
              ))}
            </Pie>

            <Tooltip />

            <Legend
              verticalAlign="bottom"
              height={36}
            />

          </PieChart>
        </ResponsiveContainer>
      </div>

    </div>
  );
}

export default InventoryChart;