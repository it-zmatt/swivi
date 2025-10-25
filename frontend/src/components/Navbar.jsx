import React from "react";
import logo from "../assets/swim.png";


export default function Navbar() {
  return (
    <nav className="w-full flex items-center justify-between px-12 pt-2 pb-0 bg-[#264653] shadow-sm">
      {/* Left - Logo */}
      <div className="text-2xl font-bold text-blue-700 cursor-pointer">
        <img src={logo} alt="Company logo" className="h-22 w-auto" />        
      </div>

      {/* Right - Sign Up */}
      <button className="px-6 py-2 bg-[#F9F9F9] text-[#264653] border-[#264653] rounded-full hover:bg-[#F9F9F9]/80 hover:cursor-pointer transition-all">
        Rendez Vous
      </button>
    </nav>
  );
}

