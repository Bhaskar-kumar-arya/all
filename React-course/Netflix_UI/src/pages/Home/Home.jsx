import React from 'react'
import './Home.css'
import NavBar from '../../components/NavBar/NavBar'
import heroImage from '../../assets/hero_banner.jpg'
import hero_title from '../../assets/hero_title.png'
import play_icon from '../../assets/play_icon.png'
import info_icon from '../../assets/info_icon.png'
import TitleCards from '../../components/TitleCards/TitleCards'
import cards_data from '../../assets/cards/Cards_data'

export default function Home() {
  return (
    <div className='home'>
        <NavBar/>
        <div className="hero">
          <img src={heroImage} className='banner-img' alt="" />
          <div className="hero-caption">
            <img src={hero_title} className='caption-img' alt="" /> 
            <p>Discovering his ties to a secret ancient order, a young man is thrust into a battle against dark forces that threaten the world.</p>
            <div className="hero-btns">
              <button className='btn'><img src={play_icon} alt="" /> <span>Play</span></button>
              <button className='btn dark-btn'><img src={info_icon} alt="" /> <span>Info</span></button>
            </div>
            <TitleCards cards_data={cards_data}/>
          </div>
        </div>
        <div className="more-cards">
          <TitleCards cards_data={cards_data}/>
          <TitleCards cards_data={cards_data}/>
          <TitleCards cards_data={cards_data}/>
        </div>
    </div>
  )
}
