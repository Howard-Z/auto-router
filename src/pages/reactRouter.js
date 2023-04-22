import {createBrowserRouter} from "react-router-dom";
import Welcome from "./welcome";
//page navigation tree
const router = createBrowserRouter([
    {
        path: "/",
        element: <Welcome />,
    }
]);

export {router}