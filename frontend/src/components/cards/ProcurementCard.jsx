import {
  FiClock,
  FiTruck,
  FiCheckCircle,
} from "react-icons/fi";

function ProcurementCard() {
  return (
    <div className="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">

      <div className="mb-5">
        <h2 className="text-lg font-bold text-slate-900">
          Procurement
        </h2>

        <p className="mt-1 text-sm text-slate-500">
          Purchase order status
        </p>
      </div>

      <div className="space-y-4">

        <div className="flex items-center justify-between rounded-xl bg-amber-50 p-4">
          <div className="flex items-center gap-3">
            <FiClock
              className="text-amber-600"
              size={20}
            />

            <span className="text-sm font-medium text-slate-700">
              Pending
            </span>
          </div>

          <span className="font-bold text-amber-700">
            12
          </span>
        </div>

        <div className="flex items-center justify-between rounded-xl bg-blue-50 p-4">
          <div className="flex items-center gap-3">
            <FiTruck
              className="text-blue-600"
              size={20}
            />

            <span className="text-sm font-medium text-slate-700">
              Expected
            </span>
          </div>

          <span className="font-bold text-blue-700">
            8
          </span>
        </div>

        <div className="flex items-center justify-between rounded-xl bg-emerald-50 p-4">
          <div className="flex items-center gap-3">
            <FiCheckCircle
              className="text-emerald-600"
              size={20}
            />

            <span className="text-sm font-medium text-slate-700">
              Received
            </span>
          </div>

          <span className="font-bold text-emerald-700">
            34
          </span>
        </div>

      </div>
    </div>
  );
}

export default ProcurementCard;