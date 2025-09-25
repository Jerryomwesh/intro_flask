import { Outlet } from "react-router-dom";

function MainDash() {
    return (
        <div>
            <h1> Dashboard Main Screen </h1>
            <Outlet />
        </div>
    )
}

export default MainDash;
