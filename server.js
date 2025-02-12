const mongoose = require('mongoose');
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3001;
const DB = "mongodb://localhost:27017/job_sorter";
const cors = require('cors')

console.log("🔌 MongoDB URI:", DB);
console.log("🚀 Starting server...");

app.use(cors());

// ✅ Middleware to parse JSON requests
app.use(express.json());

mongoose.connect(DB, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log("Connected"))
    .catch((err) => console.error("Connection Error:", err))

const jobSchema = new mongoose.Schema({ sender: String, subject: String, body: String, category: String});
const Jobs = mongoose.model('jobs', jobSchema, 'jobs');

app.get('/api/jobs', async (req, res) => {
    try {
        console.log("📨 API called: /api/jobs");
        const jobs = await Jobs.find();
        console.log("📋 Found jobs:", jobs);
        res.json(jobs);
    } catch (err) {
        console.error("❌ Error fetching jobs:", err);
        res.status(500).json({ error: err.message });
    }
});

app.listen(PORT, () => {
    console.log(`✅ Server is running on http://localhost:${PORT}`);
  });