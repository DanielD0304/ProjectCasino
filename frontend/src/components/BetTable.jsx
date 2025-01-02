import React from 'react';
import './betTable.css'; // Create a CSS file for styling

const BetTable = () => {
  // Define the numbers and their colors
  const rouletteNumbers = [
    { number: 0, color: 'green' },
    ...Array.from({ length: 36 }, (_, i) => ({
      number: i + 1,
      color: (i + 1 <= 10 || (i + 1 > 18 && i + 1 <= 28)) ? (i % 2 === 0 ? 'black' : 'red') : (i % 2 === 0 ? 'red' : 'black')
    }))
  ];

  return (
    <div className="roulette-table">
      <div className="number-grid">
        {rouletteNumbers.map(({ number, color }) => (
          <div 
            key={number} 
            className="number-cell" 
            style={{ backgroundColor: color }}
          >
            {number}
          </div>
        ))}
      </div>
      <div className="bet-fields">
        <div className="bet-field" data-bet="even">Even</div>
        <div className="bet-field" data-bet="odd">Odd</div>
        <div className="bet-field" data-bet="red">Red</div>
        <div className="bet-field" data-bet="black">Black</div>
        <div className="bet-field" data-bet="1to18">1 to 18</div>
        <div className="bet-field" data-bet="19to36">19 to 36</div>
        <div className="bet-field" data-bet="1st12">1st 12</div>
        <div className="bet-field" data-bet="2nd12">2nd 12</div>
        <div className="bet-field" data-bet="3rd12">3rd 12</div>
      </div>
    </div>
  );
};

export default BetTable;
