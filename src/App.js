import React from 'react';
import axios from 'axios';
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      response: "Nothing yet!"
      
    };
  }

  handleSort() {
    const checkboxes = document.getElementsByClassName('sortBox');
    for (const checkbox of checkboxes) {
      if (checkbox.checked) {
        axios.get(`http://localhost:8080/query?type=${checkbox.id}&list=${document.getElementById('inputList').value}`)
        .then(res => {
            const data = res.data;
            this.setState({ response: data });
        });
      }
    }
  }

  handleCheckboxChange(event) {
    const checkboxes = document.getElementsByClassName('sortBox');
    let checkedCount = 0;
    for (const checkbox of checkboxes) {
      if (checkbox.checked) {
        checkedCount++;
      }
    }
    if (checkedCount > 3) {
      window.alert("You can only select up to 3 checkboxes.");
      // Uncheck the last checkbox that was checked
      event.target.checked = false;
    }
  }

  render() {
    return (
      <div>
        <div>
          <input type="checkbox" id="selectionSort" className="sortBox" value="selectionSort" onChange={this.handleCheckboxChange}/>
          <label htmlFor="selectionSort">Selection Sort</label>
        </div>
        <div>
          <input type="checkbox" id="bubbleSort" className="sortBox" value="bubbleSort" onChange={this.handleCheckboxChange}/>
          <label htmlFor="bubbleSort">Bubble Sort</label>
        </div>
        <div> 
          <input type="checkbox" id="mergeSort" className="sortBox" value="mergeSort" onChange={this.handleCheckboxChange}/>
          <label htmlFor="mergeSort">Merge Sort</label>
        </div>
        <div>
          <input type="checkbox" id="quickSort" className="sortBox" value="quickSort" onChange={this.handleCheckboxChange}/>
          <label htmlFor="quickSort">Quick Sort</label>
        </div>
        <br />
        <label htmlFor="input-list">Enter List:</label>
        <input type="text" id="inputList" placeholder="e.g., [1, 5, 3]"/>
        <br />
        <button onClick={this.handleSort}>See Comparisons!</button>
        <br />
        <h2>Results:</h2>
        {this.state.response ? (
          <pre>{JSON.stringify(this.state.response, null, 2)}</pre>
        ) : (
          <p>No results yet.</p>
        )}
      </div>
    );
  }
}

export default App;