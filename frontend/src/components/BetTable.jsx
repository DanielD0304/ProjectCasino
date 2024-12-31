import React from "react";
import "./betTable.css";

const BetTable = ({ onPlaceBet }) => {
  const placeBet = (betType) => {
    onPlaceBet(betType);
  };

  const renderNumberCell = (number, color) => (
    <button
      key={number}
      onClick={() => placeBet(number)}
      className={`bet-cell ${color}`}
    >
      {number}
    </button>
  );

  return (
    <div className="roulette-table">
      {/* Number grid */}
      <div className="number-grid">
        <div className="zero-cell">{renderNumberCell(0, "green")}</div>
        <div className="number-rows">
          {[
            [1, "red"], [2, "black"], [3, "red"], [4, "black"], [5, "red"], [6, "black"],
            [7, "red"], [8, "black"], [9, "red"], [10, "black"], [11, "black"], [12, "red"],
            [13, "black"], [14, "red"], [15, "black"], [16, "red"], [17, "black"], [18, "red"],
            [19, "red"], [20, "black"], [21, "red"], [22, "black"], [23, "red"], [24, "black"],
            [25, "red"], [26, "black"], [27, "red"], [28, "black"], [29, "black"], [30, "red"],
            [31, "black"], [32, "red"], [33, "black"], [34, "red"], [35, "black"], [36, "red"]
          ].map(([number, color]) => renderNumberCell(number, color))}
        </div>
      </div>

      {/* Betting options */}
      <div className="bet-options">
        <button onClick={() => placeBet("1st12")} className="bet-cell">1st 12</button>
        <button onClick={() => placeBet("2nd12")} className="bet-cell">2nd 12</button>
        <button onClick={() => placeBet("3rd12")} className="bet-cell">3rd 12</button>
        <button onClick={() => placeBet("1to18")} className="bet-cell">1 to 18</button>
        <button onClick={() => placeBet("19to36")} className="bet-cell">19 to 36</button>
        <button onClick={() => placeBet("even")} className="bet-cell">Even</button>
        <button onClick={() => placeBet("odd")} className="bet-cell">Odd</button>
        <button onClick={() => placeBet("red")} className="bet-cell red">Red</button>
        <button onClick={() => placeBet("black")} className="bet-cell black">Black</button>
      </div>
    </div>
  );
};

export default BetTable;
