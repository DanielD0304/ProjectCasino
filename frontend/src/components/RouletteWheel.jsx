import React, { useState } from "react";

const RouletteWheel = ({ onSpinComplete }) => {
  const [spinning, setSpinning] = useState(false);

  const spinWheel = () => {
    setSpinning(true);
    const result = Math.floor(Math.random() * 37); // 0-36
    setTimeout(() => {
      setSpinning(false);
      onSpinComplete(result);
    }, 3000); // Simuliert 3 Sekunden Spin
  };

  return (
    <div className="roulette-wheel">
      <div className={`wheel ${spinning ? "spinning" : ""}`}>
        {/* Das Rad wird hier grafisch dargestellt */}
      </div>
      <button onClick={spinWheel} disabled={spinning}>
        Spin
      </button>
    </div>
  );
};

export default RouletteWheel;
