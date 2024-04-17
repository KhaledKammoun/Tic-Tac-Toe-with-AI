'use client'
import { getServerSideProps } from "next/dist/build/templates/pages";
import { useState } from "react";

interface SquareProps {
    opponent: boolean ;
    onGame: boolean ;
} ;
type Props = Awaited<ReturnType<typeof getServerSideProps>>['props']

// export default function Square({opponent, onGame} : SquareProps) {

const Square: React.FC<Props> = ({opponent, onGame}) => {
  const [board, setBoard] = useState<string[]>(Array(9).fill('')) ;
  const [count, setCount] = useState(1) ;
  const [boardHistory, setBoardHistory] = useState<number[]>([]) ;
  const winner = calculateWinner(board);

  function calculateWinner(board : string[]) :string | null {
    const lines = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6]
    ];
    for (let i = 0; i < lines.length; i++) {
      const [a, b, c] = lines[i] ;
      if (board[a] && board[a] === board[b] && board[a] === board[c]){
        return board[a] ;
      }
    }
    return null;
  }
  
  const handleClick = (key : number) : void=> {
    if (!board[key] && !calculateWinner(board)) {
      
      const newBoard = [...board] ;
      newBoard[key] = (count % 2 != 0) ? 'X' : 'O' ;
      setBoard(newBoard) ;
      setCount(count + 1) ;

      setBoardHistory([...boardHistory, key]);
    }
  }
  const handleClickEvent = (key : number) : void => {
    setCount(key + 1) ;
    const newBH = boardHistory.slice(0, key);
    const newBoard = [...Array(9).fill('')];
    newBH.map((el, index) => {
      newBoard[el] = (index % 2 == 0) ? 'X' : 'O';
    });
    setBoard(newBoard);
    setBoardHistory(newBH) ;
  }
  const handleClean = () : void=> {
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
      </div>{
        winner && <div>The Winner Is {winner}</div>
        }
    </main>
  );
}

export default Square ;