import {useContext} from "react";
import { EmailContext } from "../App";

function Interview(){
    const {interview} = useContext(EmailContext);
    
    if (interview.length > 0){
        return (
            <div>
                {interview.map((email) => (
                    <div id='l'><p><strong>{email.sender}</strong></p><p>{email.subject}</p>
                    <div dangerouslySetInnerHTML={{__html:email.body}}></div></div>
                ))}
            </div>
        )
    }

    return (
        <h2>Nothing to see here!</h2>
    )
};

export default Interview;