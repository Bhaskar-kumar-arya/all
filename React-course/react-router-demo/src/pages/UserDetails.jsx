import { useParams } from "react-router-dom";

export default function UserDetails() {
  const { id } = useParams();
  return <h2>Details for User ID: {id}</h2>;
}
