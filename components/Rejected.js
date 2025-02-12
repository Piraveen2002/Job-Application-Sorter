import {useContext} from "react";
import { EmailContext } from "../App";

function Rejected(){
    const {rejected} = useContext(EmailContext);

    if (rejected.length > 0){
        return (
            <div>
                {rejected.map((email) => (
                    <div id='l'><p><strong>{email.sender}</strong></p><p>{email.subject}</p>
                    <div dangerouslySetInnerHTML={{__html:email.body}}></div></div>
                ))}
            </div>
        )
    }

    return (
        <h2>Nothing to see here!</h2>
    )
}

export default Rejected