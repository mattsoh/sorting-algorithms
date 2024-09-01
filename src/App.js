import React from 'react';
import axios from 'axios';
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      response: "Nothing yet!"
    };
    this.handleSort = this.handleSort.bind(this);
  }

  handleSort() {
    const checkboxes = document.getElementsByClassName('sortBox');
    let responses = [];
    for (const checkbox of checkboxes) {
      if (checkbox.checked) {
        // window.alert(encodeURIComponent(document.getElementById('inputList').value));
        // window.alert(`http://localhost:8080/query?type=${checkbox.id}&list=${encodeURIComponent(document.getElementById('inputList').value)}`)
        axios.get(`http://localhost:8080/query?type=${checkbox.id}&list=${encodeURIComponent(document.getElementById('inputList').value)}`)
          .then(res => {
            const data = res.data;
            console.log(data);
            responses.push(`${checkbox.value}: ${data[0]}`);
            console.log(responses)
            // this.setState({ response: [checkbox.value, data[0]] });
          })
          .catch(error => {
            console.error('There was an error making request for '+ checkbox.value + ":", error);
            window.alert('There was an error making the request for ' + checkbox.value + '. Please try again later.');
            return;
          });
      }
    }
    console.log(responses);
    this.res = responses;
    this.setState({response: responses} );
    console.log(this.state, "set")
    Promise.all(this.res).then(responses => {
      const validResponses = responses.filter(response => response.value !== 'Error').map(response => response.value);
      const mean = validResponses.reduce((a, b) => a + b, 0) / validResponses.length;
      const stdDev = Math.sqrt(validResponses.map(x => Math.pow(x - mean, 2)).reduce((a, b) => a + b) / validResponses.length);
      const zScores = responses.map(response => {
        if (response.value === 'Error') {
          return { ...response, zScore: null };
        }
        const zScore = (response.value - mean) / stdDev;
        return { ...response, zScore };
      });
      this.setState({ response: zScores });
    });
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
      window.alert("You can only select up to 3 algorithms.");
      event.target.checked = false;
    }
  }

  render() {
    return (
      <div>
        <div className="checkbox-container">
          <input type="checkbox" id="bubble" className="sortBox" value="Bubble Sort" onChange={this.handleCheckboxChange} selected/>
          <label htmlFor="bubble">Bubble Sort</label>
        </div>
        <div>
          <input type="checkbox" id="insertion" className="sortBox" value="Insertion Sort" onChange={this.handleCheckboxChange} selected/>
          <label htmlFor="insertion">Insertion Sort</label>
        </div>
        <div>
          <input type="checkbox" id="merge" className="sortBox" value="Merge Sort" onChange={this.handleCheckboxChange} selected  />
          <label htmlFor="merge">Merge Sort</label>
        </div>
        <div>
          <input type="checkbox" id="selection" className="sortBox" value="Selection Sort" onChange={this.handleCheckboxChange}/>
          <label htmlFor="selection">Selection Sort</label>
        </div>
        <div>
          <input type="checkbox" id="radix" className="sortBox" value="Radix Sort" onChange={this.handleCheckboxChange}/>
          <label htmlFor="radix">Radix Sort</label>
        </div>
        <div>
          <input type="checkbox" id="quick" className="sortBox" value="Quick Sort" onChange={this.handleCheckboxChange}/>
          <label htmlFor="quick">Quick Sort</label>
        </div>
        <div>
          <input type="checkbox" id="tree" className="sortBox" value="Tree Sort" onChange={this.handleCheckboxChange}/>
          <label htmlFor="tree">Tree Sort</label>
        </div>
        <div>
          <input type="checkbox" id="bogo" className="sortBox" value="Bogo Sort" onChange={this.handleCheckboxChange}/>
          <label htmlFor="bogo">Bogo Sort</label>
        </div>
        <div>
          <input type="checkbox" id="slow" className="sortBox" value="Slow Sort" onChange={this.handleCheckboxChange}/>
          <label htmlFor="slow">Slow Sort</label>
        </div>
        <br />
        <label htmlFor="input-list">Enter List:</label>
        <input type="text" id="inputList" placeholder="e.g., [1, 5, 3]"/>
        <br />
        <button onClick={this.handleSort}>See Comparisons!</button>
        <br />
        <h2>Results:</h2>
        <div id="responses">
          {this.state.response ? (
            <pre>{JSON.stringify(this.state.response, null, 2)}</pre>
          ) : (
            <p>No results yet.</p>
          )}
        </div>
      </div>
    );
  }
}

export default App;