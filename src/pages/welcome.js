import React, {useEffect, useState} from "react"
import "./Welcome.css";

function Welcome()
{
    return (
        <div className="wrapper">
            <div>
                <h1>Welcome</h1>
            </div>
            <div>
                <p>This is the home page</p>
            </div>
            <div>
                <b style={{fontSize: "2em"}}>This is a button</b>
                <div style={{flexGrow: "1"}}/>
                <Button onClick={() => {/*do something*/}}>
                    <Close/>
                </Button>
            </div>
        </div>
    )
}

export default Welcome