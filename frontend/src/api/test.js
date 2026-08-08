import api from "./axios";

export const getCustomers = async () => {
  const response = await api.get("customers/");
  return response.data;
};