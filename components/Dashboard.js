import React, {useState, useContext} from "react";
import { EmailContext } from "../App";

function Dashboard() {
    const { rejected } = useContext(EmailContext);
    const { offers} = useContext(EmailContext);
    const { assessments} = useContext(EmailContext);
    const { interview} = useContext(EmailContext);
    const { received} = useContext(EmailContext);
    const [selectedEmail, setSelectedEmail] = useState(null);
    
    if (selectedEmail === null){
        return (
            <div>
            <div className="container" id='Positive'>
            <div id='Offer'>
                <h4 style={{"text-align": "center"}}>Offers</h4>
                {offers.map((email, index) => (
                <div key={index} id='item' onClick={() => setSelectedEmail(email)}><p><strong>{email.sender}</strong>, <br></br>{email.subject}</p></div>
                ))}
            </div>
            <div id='Interview'>
                <h4 style={{"text-align": "center"}}>Interview</h4>
                {interview.map((email, index) => (
                <div key={index} id='item' onClick={() => setSelectedEmail(email)}><p><strong>{email.sender}</strong>, <br></br> {email.subject}</p></div>
                ))}
            </div>
            <div id='Assessment'>
                <h4 style={{"text-align": "center"}}>Technical Assessment/Next Steps</h4>
                {assessments.map((email, index) => (
                <div key={index} id='item' onClick={() => setSelectedEmail(email)}><p><strong>{email.sender}</strong>, <br></br> {email.subject}</p></div>
                ))}
            </div>
            <div id='Received'>
                <h4 style={{"text-align": "center"}}>Received Application</h4>
                {received.map((email, index) => (
                <div key={index} id='item' onClick={() => setSelectedEmail(email)}><p><strong>{email.sender}</strong>, <br></br>{email.subject}</p></div>
                ))}
            </div>
            </div>
            <div className="container" id='Rejected'>
            <div id='Rej'>
                <h4 style={{"text-align": "center"}}>Rejected</h4>
                {rejected.map((email, index) => (
                <div key={index} id='item' onClick={() => setSelectedEmail(email)}><p><strong>{email.sender}</strong>, <br></br>{email.subject}</p></div>
                ))}
            </div>
            </div>
            </div>
            );}
            
        return(
        <div className="modal" >
            <div className="modal-content">
                <span onClick={() => setSelectedEmail(null)} className="close">&times;</span>
                <h2>{selectedEmail.subject}</h2>
                <p><strong>From:</strong> {selectedEmail.sender}</p>
                <p><strong>Message:</strong></p>
                <div dangerouslySetInnerHTML={{__html:selectedEmail.body}}/>
            </div>
        </div>
        )
    };

    export default Dashboard;