import './App.css';
import React, {useState, useEffect, createContext} from "react";
import { Routes, Route, BrowserRouter } from "react-router-dom";
import Offer from './components/Offer.js';
import Assessment from './components/Assessment.js';
import Dashboard from './components/Dashboard.js';
import Interview from './components/Interview.js';
import Received from './components/Received.js';
import Rejected from './components/Rejected.js';

export const EmailContext = createContext();

function App() {
  const [emails, setEmails] = useState([]);
  const [categorizedEmails, setCategorizedEmails] = useState({
    offers: [],
    rejected: [],
    assessments: [],
    interview: [],
    received: [],
  });

  useEffect(() => {
      fetch('http://localhost:3001/api/jobs/')
      .then(response => response.json())
      .then(data => setEmails(data));
  }, []);

  useEffect(() => {
    setCategorizedEmails({
      offers: emails.filter((email) => email.category === "Offer"),
      rejected: emails.filter((email) => email.category === "Negative"),
      assessments: emails.filter((email) => email.category === "Technical Assessment" || email.category === "Next Steps"),
      interview: emails.filter((email) => email.category === "Interview"),
      received: emails.filter((email) => email.category === "Received Application"),
    });
  }, [emails]);

  return(
    <EmailContext.Provider value={categorizedEmails}>
      <div className="App">
        <h1>Job Applications Dashboard</h1>
        <nav><a href="/">Dashboard</a> | <a href="/Offers">Offers</a> | <a href="/Interview">Interview</a> | <a href="/Assessment">Assessment/Next Steps</a> | <a href="/Received">Received</a> | <a href="/Rejected">Rejected</a></nav>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Dashboard/>}/>
            <Route path="/Offers" element={<Offer/>}/>
            <Route path="/Interview" element={<Interview/>}/>
            <Route path="/Assessment" element={<Assessment/>}/>
            <Route path="/Received" element={<Received/>}/>
            <Route path="/Rejected" element={<Rejected/>}/>
          </Routes>
        </BrowserRouter>
      </div>
    </EmailContext.Provider>
  );
}

export default App;
