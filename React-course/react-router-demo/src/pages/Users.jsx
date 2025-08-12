import React from 'react'
import { Link } from "react-router-dom";


export default function Users() {

    const users = [
    { id: 1, name: "Alice" },
    { id: 2, name: "Bob" },
    { id: 3, name: "Charlie" }
  ];

  return (
    <div>
        <h1>Users List</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>
            <Link to = {`/users/${user.id}`}>{user.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  )
}
