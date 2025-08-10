import React from 'react'
import './NavBar.css'
import logo from '../../assets/logo.png'
import search_icon from '../../assets/search_icon.svg'
import bell_icon from '../../assets/bell_icon.svg'
import profile_img from '../../assets/profile_img.png'
import caret_icon from '../../assets/caret_icon.svg'  


export default function NavBar() {
  return (
    <div className='navbar'>
      <div className="navbar-left">
        <img src={logo} alt="" />
        <ul>
          <li>Home</li>
          <li>TV Shows</li>
          <li>Movies</li>
          <li>New & Popular</li>
        </ul>
      </div>
      <div className="navbar-right">
        <img src={search_icon} className='icons' alt="" />
        <p>Children</p> 
        <img src={bell_icon} className='icons' alt="" />
        <div className="navbar-profile">
          <img src={profile_img} className='profile' alt="" />
          <img src={caret_icon} alt="" />
          <div className="dropdown">
            <p>sign out of netflix</p>
          </div>
        </div>
      </div>
    </div>
  )
}
 