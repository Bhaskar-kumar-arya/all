import { Link, Outlet } from "react-router-dom";

export default function UsersLayout() {
  const users = [
    { id: 1, name: "Alice" },
    { id: 2, name: "Bob" },
    { id: 3, name: "Charlie" }
  ];

  return (
    <div style={{ display: "flex", gap: "20px" }}>
      {/* Sidebar list */}
      <aside style={{ minWidth: "150px" }}>
        <h3>Users</h3>
        <ul>
          {users.map(user => (
            <li key={user.id}>
              <Link to={`${user.id}`}>{user.name}</Link>
            </li>
          ))}
        </ul>
      </aside>

      {/* Nested route content */}
      <main style={{ flex: 1 }}>
        <Outlet />
      </main>
    </div>
  );
}
