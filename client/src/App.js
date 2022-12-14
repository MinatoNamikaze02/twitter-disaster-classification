import "./App.css";
import { useState } from "react";

function App() {
  const [tweet, setTweet] = useState("");
  const [count, setCount] = useState(10);
  const [success, setSuccess] = useState(false);
  const [data, setData] = useState([]);
  const handleSubmit = (event) => {
    event.preventDefault();
    console.log("Tweet: ", tweet);
    {
      /* fetch tweets */
    }
    fetch(`http://localhost:80/tweets?tags=${tweet}&count=${count}`, {
      method: "POST",
      headers: {
        Authorization: "Bearer " + "arjun",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        setData(data);
        console.log(data[0]);
        setSuccess(true);
      })
      .catch((error) => {
        console.error("Error:", error);
        setSuccess(false);
      });
  };

  const handleReset = () => {
    setTweet("");
    setCount(10);
    setSuccess(false);
    setData([]);
  }

  return (
    <div className="App">
      <header className="App-header">
        # navbar
        <nav className="navbar">
          <h3>Twitter Disaster Classification Client</h3>
        </nav>
      </header>
      {!success && (
        <form className="form-outer">
          <div className="form-group">
            <label htmlFor="tweet">Tweet</label>
            <input
              type="text"
              className="form-control"
              id="tweet"
              placeholder="Enter tweet"
              value={tweet}
              onChange={(event) => setTweet(event.target.value)}
            />
            <br/>
            <label htmlFor="tweet">Count</label>
            <input
              type="number"
              className="form-control"
              id="count"
              placeholder="Enter count"
              value={count}
              onChange={(event) => setCount(event.target.value)}
            />
          </div>
          <button
            type="submit"
            className="btn btn-primary"
            onClick={handleSubmit}
          >
            Submit
          </button>
        </form>
      )}
      <article>
        {success &&  (
        <div className="title-reset">
           <p className="title-results"><b>SEARCH TAG: </b>{tweet}</p>
           <button className="btn btn-primary" onClick={handleReset}>RESET</button>
        </div>
        )}
        {data &&
          data.map((tweet) => {
            return (
              <div className="tweet">
                  <h1>Tweet Information</h1>
                  <p>
                    <b>TEXT</b>: {tweet.text}
                  </p>
                  <p>
                    <b>ID</b>: {tweet.id}
                  </p>
                  <p>
                    <b>CREATED AT</b>: {tweet.created_at.substr(0, 10)}
                  </p>
                  <br />
                  <p><b>Predictions: </b></p>
                  {tweet.predictions.map((prediction) => {
                    return (
                      <div className="prediction">
                        <div className="tag">
                          #{prediction.label}
                          <br/>
                        </div>
                      </div>
                    );
                  })}
              </div>
            );
          })}
      </article>
    </div>
  );
}

export default App;
