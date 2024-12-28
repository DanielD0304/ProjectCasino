import React from "react";

const BetTable = ({ bets, onPlaceBet }) => {
  const placeBet = (number) => {
    onPlaceBet(number);
  };

  return (
    <div className="bet-table">
      {Array.from({ length: 37 }, (_, i) => (
        <button key={i} onClick={() => placeBet(i)} className="bet-cell">
          {i}
        </button>
      ))}
      {/* Zusätzliche Felder für Rot/Schwarz, Gerade/Ungerade */}
    </div>
  );
};

export default BetTable;
