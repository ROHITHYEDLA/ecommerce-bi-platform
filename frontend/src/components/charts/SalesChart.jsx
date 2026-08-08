import {
  ResponsiveContainer,
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
} from "recharts";

const salesData = [
  { month: "Jan", sales: 82000 },
  { month: "Feb", sales: 96000 },
  { month: "Mar", sales: 88000 },
  { month: "Apr", sales: 115000 },
  { month: "May", sales: 128000 },
  { month: "Jun", sales: 142000 },
  { month: "Jul", sales: 156000 },
];

function SalesChart() {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">

      <div className="mb-6">
        <h2 className="text-lg font-bold text-slate-900">
          Sales Overview
        </h2>

        <p className="mt-1 text-sm text-slate-500">
          Monthly revenue performance
        </p>
      </div>

      <div className="h-80 w-full">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={salesData}>

            <defs>
              <linearGradient
                id="salesGradient"
                x1="0"
                y1="0"
                x2="0"
                y2="1"
              >
                <stop
                  offset="0%"
                  stopColor="#2563eb"
                  stopOpacity={0.3}
                />

                <stop
                  offset="100%"
                  stopColor="#2563eb"
                  stopOpacity={0}
                />
              </linearGradient>
            </defs>

            <CartesianGrid
              strokeDasharray="3 3"
              stroke="#e2e8f0"
            />

            <XAxis
              dataKey="month"
              stroke="#64748b"
              fontSize={12}
            />

            <YAxis
              stroke="#64748b"
              fontSize={12}
              tickFormatter={(value) =>
                `₹${value / 1000}k`
              }
            />

            <Tooltip
              formatter={(value) =>
                `₹${value.toLocaleString("en-IN")}`
              }
              contentStyle={{
                borderRadius: "12px",
                border: "1px solid #e2e8f0",
              }}
            />

            <Area
              type="monotone"
              dataKey="sales"
              stroke="#2563eb"
              strokeWidth={3}
              fill="url(#salesGradient)"
            />

          </AreaChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export default SalesChart;