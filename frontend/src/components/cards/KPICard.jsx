import {
  FiTrendingUp,
  FiTrendingDown,
} from "react-icons/fi";

function KPICard({
  title,
  value,
  change,
  icon,
  positive = true,
}) {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm transition hover:-translate-y-1 hover:shadow-md">

      <div className="flex items-start justify-between">

        {/* Title + Icon */}

        <div>
          <p className="text-sm font-medium text-slate-500">
            {title}
          </p>

          <h2 className="mt-2 text-2xl font-bold text-slate-900">
            {value}
          </h2>
        </div>

        {/* Icon */}

        <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-blue-50 text-blue-600">
          {icon}
        </div>

      </div>

      {/* Change */}

      {change && (
        <div className="mt-4 flex items-center gap-2">

          <div
            className={`flex items-center gap-1 text-sm font-semibold ${
              positive
                ? "text-emerald-600"
                : "text-red-600"
            }`}
          >
            {positive ? (
              <FiTrendingUp size={15} />
            ) : (
              <FiTrendingDown size={15} />
            )}

            {change}
          </div>

          <span className="text-xs text-slate-400">
            vs last month
          </span>

        </div>
      )}

    </div>
  );
}

export default KPICard;