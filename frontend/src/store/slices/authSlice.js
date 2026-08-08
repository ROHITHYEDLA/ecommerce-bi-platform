import { createSlice } from "@reduxjs/toolkit";

const accessToken = localStorage.getItem("accessToken");
const refreshToken = localStorage.getItem("refreshToken");
const storedUser = localStorage.getItem("user");

const initialState = {
  user: storedUser ? JSON.parse(storedUser) : null,
  accessToken: accessToken,
  refreshToken: refreshToken,
  isAuthenticated: !!accessToken,
};

const authSlice = createSlice({
  name: "auth",

  initialState,

  reducers: {
    loginSuccess: (state, action) => {
      const {
        user,
        access,
        refresh,
      } = action.payload;

      state.user = user;
      state.accessToken = access;
      state.refreshToken = refresh;
      state.isAuthenticated = true;

      localStorage.setItem("accessToken", access);
      localStorage.setItem("refreshToken", refresh);
      localStorage.setItem(
        "user",
        JSON.stringify(user)
      );
    },

    logout: (state) => {
      state.user = null;
      state.accessToken = null;
      state.refreshToken = null;
      state.isAuthenticated = false;

      localStorage.removeItem("accessToken");
      localStorage.removeItem("refreshToken");
      localStorage.removeItem("user");
    },

    setUser: (state, action) => {
      state.user = action.payload;

      localStorage.setItem(
        "user",
        JSON.stringify(action.payload)
      );
    },
  },
});

export const {
  loginSuccess,
  logout,
  setUser,
} = authSlice.actions;

export default authSlice.reducer;