
import './App.css';

import React, { useState } from "react";
import RouletteWheel from "./components/RouletteWheel.jsx";
import BetTable from "./components/BetTable";
import Controls from "./components/Controls";
import "./styles.css";

const App = () => {
  const [balance, setBalance] = useState(1000);
  const [bets, setBets] = useState({});
  const [lastResult, setLastResult] = useState(null);

  const handleSpinComplete = (result) => {
    setLastResult(result);
    // Gewinnauswertung
    // ...
  };

  const placeBet = (number) => {
    if (balance >= 10) {
      setBets({ ...bets, [number]: (bets[number] || 0) + 10 });
      setBalance(balance - 10);
    }
  };

  const resetGame = () => {
    setBalance(1000);
    setBets({});
    setLastResult(null);
  };

  const clearBets = () => {
    setBets({});
  };

  return (
    <div className="app">
      <h1>Roulette</h1>
      <RouletteWheel onSpinComplete={handleSpinComplete} />
      <BetTable bets={bets} onPlaceBet={placeBet} />
      <Controls
        balance={balance}
        onReset={resetGame}
        onClear={clearBets}
      />
      {lastResult !== null && <p>Last Result: {lastResult}</p>}
    </div>
  );
};

export default App;

