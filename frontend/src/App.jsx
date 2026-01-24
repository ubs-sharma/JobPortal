import "./App.css";
import { ApplyJobPage } from "./ApplyJobPage";
import { JobListingPage } from "./JobListingPage";
import { LoginPage } from "./LoginPage";
import { RegisterPage } from "./RegisterPage";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<LoginPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/jobs" element={<JobListingPage />} />
          <Route path="/apply/:jobId" element={<ApplyJobPage />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
