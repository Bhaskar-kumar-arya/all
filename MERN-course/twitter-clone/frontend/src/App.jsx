import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import SignUpPage from "./pages/auth/signup/SignUpPage.jsx";
import HomePage from "./pages/home/HomePage.jsx";
import LoginPage from "./pages/auth/login/LoginPage.jsx";
import { Routes, Route, Navigate } from "react-router-dom";
import Sidebar from './components/common/Sidebar.jsx'
import NotificationPage from "./pages/notification/NotificationPage.jsx";
import RightPanel from './components/common/RightPanel.jsx'
import ProfilePage from "./pages/profile/ProfilePage.jsx";
import { Toaster } from "react-hot-toast";
import { useQuery } from "@tanstack/react-query";
import LoadingSpinner from "./components/common/LoadingSpinner.jsx";

function App() {

  const {data:authUser,isLoading} = useQuery({
    queryKey : ['authUser'],
    queryFn : async () => {
      try {
        const res = await fetch("/api/auth/me")
        const data = await res.json()
        console.log("fetched data of me : ",data)
        if (data.error) {
          return null
        }
        if (!res.ok) {
          throw new Error(data.message || "Failed to fetch auth user")
        }
        console.log("fetched data of me : ",data)
        return data
      } catch (error) {
        console.log("error in fetching auth user : ",error)
        throw error
      }
    }
  })

  if (isLoading) {
    return (
      <div className="h-screen flex justify-center items-center">
        <LoadingSpinner size="lg"/>
      </div>
    )
  }

  return (
    <div className='flex max-w-6xl mx-auto'>
        {authUser && <Sidebar/>}
        <Routes>
          <Route path='/' element={authUser ? <HomePage /> : <Navigate to={"/login"}/>} />
          <Route path='/signup' element={!authUser ? <SignUpPage /> : <Navigate to={"/"}/>} />
          <Route path='/login' element={!authUser ? <LoginPage /> : <Navigate to={"/"}/>} />
          <Route path="/notifications" element={authUser ? <NotificationPage/> : <Navigate to={"/logib"}/>}/>
          <Route path="/profile/:username" element={authUser ? <ProfilePage/> : <Navigate to={"/login"}/>}/>
        </Routes>
        {authUser && <RightPanel/>}
        <Toaster/>
  </div>

  );
}

export default App;
