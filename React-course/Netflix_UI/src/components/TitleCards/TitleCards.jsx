import React, { useEffect, useRef } from 'react'
import './TitleCards.css'


export default function TitleCards({cards_data,title,category}) {

  const cardsRef = useRef()
  
  const handleWheel = (e)=>{ 
    e.preventDefault()
    cardsRef.current.scrollLeft += e.deltaY;
  }
  
  useEffect(()=> {
    cardsRef.current.addEventListener('wheel',handleWheel,{passive:false})
  },[])
  return (
    <div className='title-cards'>
      <h2>{title?title:"Popular on Netflix"}</h2>
      <div className="card-list" ref={cardsRef}>
        {cards_data.map((card,index)=> {
          return <div className="card" key={index}>
            <img src={card.image} alt="" />
            <p>
              {card.name}
            </p>
          </div>
        })}
      </div>
    </div>
  )
}
