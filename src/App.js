import './App.css';
import React from 'react';
import axios from 'axios';

export function handleSort() {
  const checkboxes = document.getElementsByClassName(`sortBox`);
  for (const checkbox of checkboxes) {
    if (checkbox.checked) {
      axios.get(`http://localhost:8080/query?type=${checkbox.id}&list=${document.getElementById(`inputList`)}`)
      .then(res => {
          const data = res.data;
          this.setState({ response: data });
      });
    }
  }
  
}

function App() {
  return (
    <div>
    <h1>Sorting Comparison</h1>
      <label>Select Sorting Algorithms:</label>
      <div>
        <input type="checkbox" id="bubbleSort" class="sortBox" value="bubbleSort"/>
        <label htmlFor="bubbleSort">Bubble Sort</label>
      </div>
      <div>
        <input type="checkbox" id="mergeSort" class="sortBox" value="mergeSort"/>
        <label htmlFor="mergeSort">Merge Sort</label>
      </div>
      <div>
        <input type="checkbox" id="selectionSort" class="sortBox" value="selectionSort"/>
        <label htmlFor="selectionSort">Selection Sort</label>
      </div>
      <br />
      <label htmlFor="input-list">Enter List:</label>
      <input type="text" id="inputList" placeholder="Enter list (e.g., [1, 5, 3])"/>
      <br />
      <button onClick={handleSort}>See Comparisons!</button>
      <br />
      <h2>Results:</h2>
      {/* {result ? (
        <pre>{JSON.stringify(result, null, 2)}</pre>
      ) : (
        <p>No results yet.</p>
      )} */}
    </div>
  );
}

export default App;
