import {useContext} from "react";
import { EmailContext } from "../App";

function Assessment(){
    const {assessments} = useContext(EmailContext)
    if (assessments.length > 0){
        return (
            <div>
                {assessments.map((email) => (
                    <div id='l'><p><strong>{email.sender}</strong></p><p>{email.subject}</p>
                    <div dangerouslySetInnerHTML={{__html:email.body}}></div><br/></div>
                ))}
            </div>
        )
    }

    return (
        <h2>Nothing to see here!</h2>
    )
};

export default Assessment;