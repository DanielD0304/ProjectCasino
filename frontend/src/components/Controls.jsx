import React from "react";

const Controls = ({ balance, onReset, onClear }) => {
  return (
    <div className="controls">
      <p>Balance: ${balance}</p>
      <button onClick={onReset}>Reset</button>
      <button onClick={onClear}>Clear Bets</button>
    </div>
  );
};
export default Controls;


