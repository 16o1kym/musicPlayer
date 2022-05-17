import React from 'react';
import { Routes, Route } from 'react-router-dom';

const home = React.lazy (()=>import ('../views/home'));
const createRoomPage = React.lazy (()=>import ('../views/createRoomPage'));
const room = React.lazy(() => import('../views/room'));
const routes = [
    {
        path : '/',
        exact : true,
        page : home
    }, 
    {
        path : '/create',
        exact : true,
        page : createRoomPage
    },
    {
        path : '/room/:roomCode',
        exact : true,
        page : room,
    }
]


const router = () => {
    const element = (Component) => <Component />;
    return (
        <React.Suspense fallback={()=><h1>Loading...</h1>}>
        <Routes>
            {
                routes.map (route=>{
                    return (
                        <Route element={element (route.page)} path={route.path} exact={route.exact} key={route.path} ></Route>
                    )
                })
            }
        </Routes>
        </React.Suspense>
    )
}

export default router;
 
