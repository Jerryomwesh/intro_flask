import {BrowserRouter, Routes, Route} from "react-router-dom";
import Login from "./Screens/Login";
import studentDashBoard from "./Screens/Dashboard";
import AddStudent from "./Screens/Dashboard/Add";
import studentAnayltics from "./Screens/Dashboard/Analytics";  
import ListStudent from "./Screens/Dashboard/StudentList";


function App() {
    return (
        <BrowserRouter>

        <Routes>

        <Route path="" element={<Login/>}/>
        {/*Nested Route*/}
        <Route path="/student" element={<studentDashBoard/>}/> 
        <Route path="" element={<studentAnayltics/>}/>
        <Route path="add" element={<AddStudent/>}/>
        <Route path="List" element={<ListStudent/>}/>  
        </Routes>     
        
       </BrowserRouter>)
}


export default App;