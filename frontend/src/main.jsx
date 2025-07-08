import { createRoot } from 'react-dom/client';
import { StrictMode } from 'react';
import './index.css';

/* PAGES */
import Home from './pages/Home/Home.jsx';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Home />
  </StrictMode>,
)
