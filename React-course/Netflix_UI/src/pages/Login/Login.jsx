import React, { useState } from 'react'
import './Login.css'

export default function Login() {

  const [signState,setSignState] = useState("Sign In")

  return (
    <div className='login'>
      <form>
        {signState === "Sign Up" ? <input type="text" placeholder='Your Name' /> : null}
        <input type="email" placeholder='Your Email' />
        <input type="password" placeholder='Your pass' /> 
        <button>SignIn</button>
        <div className="form-help">
          <div className="remember">
            <input type="checkbox" />
            <label htmlFor="">Remember Me</label>
          </div>
        </div>
      </form>
      <div className="form-switch">
        {signState === "Sign Up" ? 
        <p>Already have an account? <span onClick={()=>{setSignState("Sign In")}}>Sign In Now</span></p> 
        : <p>New To Netflix? <span onClick={()=>{setSignState("Sign Up")}}>Sign Up Now</span></p> }
      </div>
    </div>
  )
}
