import { useState } from "react";
export default function Square() {
  const [board, setBoard] = useState([...Array(9).fill('')]) ;
  const [count, setCount] = useState(1) ;
  const [boardHistory, setBoardHistory] = useState([]) ;
  const handleClick = (key) => {
    if (!board[key]) {
      
      const newBoard = [...board] ;
      newBoard[key] = (count % 2 != 0) ? 'X' : 'O' ;
      setBoard(newBoard) ;
      setCount(count + 1) ;

      setBoardHistory([...boardHistory, key]);
    }
  }
  const handleClickEvent = (key) => {
    setCount(key + 1) ;
    const newBH = boardHistory.slice(0, key);
    const newBoard = [...Array(9).fill('')];
    newBH.map((el, index) => {
      newBoard[el] = (index % 2 == 0) ? 'X' : 'O';
    });
    setBoard(newBoard) ;
    setBoardHistory(newBH) ;
  }
  const handleClean = () => {
    setBoard([...Array(9).fill('')]) ;
    setBoardHistory([]) ;
    setCount(1) ;
  }
  return (
    <main style={{display:'flex', flexDirection:'row'}}>
      <div>Next Player :: {(count % 2 != 0) ? 'X' : 'O'}</div>
      <div><button onClick={() => handleClean()}>CLean Board</button></div>
      <div style={{display:'flex', flexDirection:'column'}}>
      {
        [...Array(3)].map((_, i) => (
          <div key="i" className="boardRow">{
          [...Array(3)].map((_, j) => (
            <button key={j + i * 3} className="square" onClick={() => handleClick(j + i * 3)}>{board[j + i * 3]}</button>
          ))}
          </div>
        ))
      }
      </div>
      <div style={{display:'flex', flexDirection:'column'}}>
          {
            
            [...Array(count)].map((_, i) => (<button key={i} onClick={() => handleClickEvent(i)}>{(!i) ? "Go To The Game" : `Go To Move #${i}`}</button>))
          }
      </div>
    </main>
  );
}
