
import './App.css';
import ImageEditComponent from './components/ImageEditComponent';
import ImproveComponent from "./components/ImproveComponent";
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <header className="App-header">
          <BrowserRouter>
              <Routes>
                  <Route path="/" element={<ImageEditComponent />} />
                  <Route path="/improve" element={<ImproveComponent />} />

              </Routes>
          </BrowserRouter>




      </header>
    </div>
  );
}

export default App;
