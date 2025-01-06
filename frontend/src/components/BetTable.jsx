import React from 'react';
import './betTable.css';

const BetTable = () => {
  const getColor = (number) => {
    return number % 2 === 0 ? 'black' : 'red';
  };

  const numbers = Array.from({ length: 36 }, (_, index) => index + 1);

  return (
    <div className="table-container">
      <table className="table">
        <tbody>
          {Array.from({ length: 3 }).map((_, rowIndex) => (
            <tr key={rowIndex}>
              {Array.from({ length: 12 }).map((_, colIndex) => {
                const number = numbers[colIndex * 3 + rowIndex];
                return (
                  <td key={colIndex} className={getColor(number)}>
                    {number}
                  </td>
                );
              })}
            </tr>
          ))}
        </tbody>
      </table>
      <table className="table">
        <tbody>
          <tr>
            <td>1st 12</td>
            <td>2nd 12</td>
            <td>3rd 12</td>
          </tr>
        </tbody>
      </table>
      <table className="table">
        <tbody>
          <tr>
            <td className="transparent">1 - 18</td>
            <td className="transparent">EVEN</td>
            <td className="karoRed">♦</td>
            <td className="karoBlack">♦</td>
            <td className="transparent">ODD</td>
            <td className="transparent">19 - 36</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default BetTable;