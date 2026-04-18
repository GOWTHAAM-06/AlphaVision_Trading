import React, { useState, useEffect } from 'react';
import { TrendingUp, TrendingDown, Activity, ShieldCheck } from 'lucide-react';

function App() {
  const [signal, setSignal] = useState(null);

  useEffect(() => {
    // Fetching data from your Django Brain
    fetch('http://127.0.0.1:8000/api/signal/')
      .then(res => res.json())
      .then(data => setSignal(data))
      .catch(err => console.error("Pitch Error:", err));
  }, []);

  return (
    <div className="min-h-screen p-8">
      {/* Header */}
      <div className="flex justify-between items-center mb-12 border-b border-zinc-800 pb-6">
        <h1 className="text-2xl font-bold tracking-tighter flex items-center gap-2">
          <Activity className="text-trading-green" /> ALPHAVISION <span className="text-zinc-500 font-light">TRADING</span>
        </h1>
        <div className="flex items-center gap-4 text-xs font-mono text-zinc-400">
          <div className="flex items-center gap-1"><ShieldCheck size={14}/> CORE ONLINE</div>
          <div className="bg-zinc-800 px-3 py-1 rounded">V1.0.0</div>
        </div>
      </div>

      {/* Main Signal Card */}
      <div className="max-w-md mx-auto bg-[#121212] border border-zinc-800 p-8 rounded-2xl shadow-2xl">
        <p className="text-zinc-500 text-sm mb-2 font-mono uppercase tracking-widest">{signal?.symbol || 'Analyzing...'}</p>
        
        <div className="flex items-end gap-4 mb-6">
          <h2 className="text-5xl font-bold tracking-tight">₹{signal?.current_price?.toLocaleString()}</h2>
          <span className={`text-sm mb-2 font-bold ${signal?.signal === 'BULLISH' ? 'text-green-500' : 'text-red-500'}`}>
            {signal?.signal === 'BULLISH' ? <TrendingUp className="inline" /> : <TrendingDown className="inline" />}
          </span>
        </div>

        <div className={`inline-block px-4 py-1 rounded-full text-xs font-bold mb-6`} 
             style={{ backgroundColor: `${signal?.ui_color}20`, color: signal?.ui_color, border: `1px solid ${signal?.ui_color}50` }}>
          {signal?.signal}
        </div>

        <div className="bg-zinc-900/50 p-4 rounded-xl border border-zinc-800/50">
          <p className="text-zinc-400 text-sm italic">"{signal?.advice}"</p>
        </div>
      </div>
    </div>
  );
}

export default App;