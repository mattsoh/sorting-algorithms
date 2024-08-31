import logo from './logo.svg';
import './App.css';

export function selectSort(lst) {
  
}

function App() {
  return (
    <div id="select">
    <select id="select" value={selectedSort} onChange="{(e) => selectSort(e.target.value)}" multiple>
    <option value="bubbleSort">Bubble Sort</option>
    <option value="mergeSort">Merge Sort</option>
    </select>
    </div>
  );
}

export default App;
