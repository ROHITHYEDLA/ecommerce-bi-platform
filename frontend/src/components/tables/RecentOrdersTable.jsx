const orders = [
  {
    id: "#ORD-1024",
    customer: "Rahul Sharma",
    amount: "₹85,000",
    status: "Completed",
  },
  {
    id: "#ORD-1023",
    customer: "Ananya Reddy",
    amount: "₹42,500",
    status: "Processing",
  },
  {
    id: "#ORD-1022",
    customer: "Vikram Kumar",
    amount: "₹18,900",
    status: "Completed",
  },
  {
    id: "#ORD-1021",
    customer: "Priya Singh",
    amount: "₹64,200",
    status: "Pending",
  },
  {
    id: "#ORD-1020",
    customer: "Arjun Rao",
    amount: "₹31,500",
    status: "Completed",
  },
];

function RecentOrdersTable() {
  const statusStyles = {
    Completed:
      "bg-emerald-50 text-emerald-700",

    Processing:
      "bg-blue-50 text-blue-700",

    Pending:
      "bg-amber-50 text-amber-700",
  };

  return (
    <div className="rounded-2xl border border-slate-200 bg-white shadow-sm">

      <div className="flex items-center justify-between border-b border-slate-200 p-6">

        <div>
          <h2 className="text-lg font-bold text-slate-900">
            Recent Orders
          </h2>

          <p className="mt-1 text-sm text-slate-500">
            Latest customer orders
          </p>
        </div>

        <button className="text-sm font-semibold text-blue-600 hover:text-blue-700">
          View All
        </button>

      </div>

      <div className="overflow-x-auto">

        <table className="w-full text-left">

          <thead className="bg-slate-50 text-xs uppercase text-slate-500">
            <tr>
              <th className="px-6 py-4">
                Order
              </th>

              <th className="px-6 py-4">
                Customer
              </th>

              <th className="px-6 py-4">
                Amount
              </th>

              <th className="px-6 py-4">
                Status
              </th>
            </tr>
          </thead>

          <tbody className="divide-y divide-slate-100">

            {orders.map((order) => (
              <tr
                key={order.id}
                className="hover:bg-slate-50"
              >
                <td className="px-6 py-4 text-sm font-semibold text-slate-900">
                  {order.id}
                </td>

                <td className="px-6 py-4 text-sm text-slate-600">
                  {order.customer}
                </td>

                <td className="px-6 py-4 text-sm font-semibold text-slate-900">
                  {order.amount}
                </td>

                <td className="px-6 py-4">
                  <span
                    className={`rounded-full px-3 py-1 text-xs font-semibold ${
                      statusStyles[order.status]
                    }`}
                  >
                    {order.status}
                  </span>
                </td>
              </tr>
            ))}

          </tbody>

        </table>

      </div>
    </div>
  );
}

export default RecentOrdersTable;