import {
  FiCheckCircle,
  FiAlertTriangle,
  FiXCircle,
} from "react-icons/fi";

function InventoryCard() {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">

      <h2 className="text-lg font-bold text-slate-900">
        Inventory Status
      </h2>

      <p className="mt-1 text-sm text-slate-500">
        Current stock availability
      </p>

      <div className="mt-6 space-y-4">

        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <FiCheckCircle
              className="text-emerald-500"
              size={20}
            />

            <span className="text-sm text-slate-600">
              In Stock
            </span>
          </div>

          <span className="font-semibold text-slate-900">
            720
          </span>
        </div>

        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <FiAlertTriangle
              className="text-amber-500"
              size={20}
            />

            <span className="text-sm text-slate-600">
              Low Stock
            </span>
          </div>

          <span className="font-semibold text-slate-900">
            180
          </span>
        </div>

        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <FiXCircle
              className="text-red-500"
              size={20}
            />

            <span className="text-sm text-slate-600">
              Out of Stock
            </span>
          </div>

          <span className="font-semibold text-slate-900">
            65
          </span>
        </div>

      </div>
    </div>
  );
}

export default InventoryCard;