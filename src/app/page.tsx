'use client'
import Link from "next/link";
import { useEffect, useState } from "react";
import Square from './Square/page'; // Assuming Game component is in a separate file

const Home = () => {


    const [selected, setSelected] = useState<string>('') ;
    // false : PC
    // true : Opponent :: friend
    const [opponent, setOpponent] = useState<boolean>(false) ;
    const [onGame, setOnGame] = useState<boolean>(false) ;

    const handleClickEvent = (key : string) : void => {
        setSelected(key) ;
    }
    const handleGameOpponent = (opponent : boolean) : void => {
        setOpponent(opponent) ;
        setOnGame(true) ;
    }
    useEffect(() => {
      console.log("Selected key: " + selected) ;

    }, [selected]) ;
    return (
        <main className="bg-black-400 text-gray-400 h-screen flex flex-col justify-center items-center">
            {(!onGame) ?
            <section className="h-[70vh] w-full sm:w-[60%] lg:w-[40%] flex flex-col items-center justify-center gap-10">
                <div>Logo</div>
                <div className="bg-black-300 w-[90%] rounded-lg p-5 text-center">
                    <h1 className="font-bold mb-5 text-lg">PICK PLAYER 1&apos;s MARK</h1>
                    <div className="bg-black-400 py-3 rounded-lg flex w-full mb-5">
                      <button onClick={() => handleClickEvent('X')} className="bg-gray-400 rounded-lg px-3 py-3 ml-3 w-1/2 mx-auto flex justify-center items-center"><svg width="32" height="32" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M31.5569 5.28973L26.7103 0.443061C26.1195 -0.147687 25.1617 -0.147687 24.571 0.443061L16 9.01404L7.42902 0.443061C6.83827 -0.147687 5.88048 -0.147687 5.28973 0.443061L0.443061 5.28973C-0.147687 5.88048 -0.147687 6.83827 0.443061 7.42902L9.01404 16L0.443061 24.571C-0.147687 25.1617 -0.147687 26.1195 0.443061 26.7103L5.28973 31.5569C5.88048 32.1477 6.83827 32.1477 7.42902 31.5569L16 22.986L24.571 31.5569C25.1617 32.1477 26.1195 32.1477 26.7103 31.5569L31.5569 26.7103C32.1477 26.1195 32.1477 25.1617 31.5569 24.571L22.986 16L31.5569 7.42902C32.1477 6.83827 32.1477 5.88048 31.5569 5.28973Z" stroke="#A8BFC9" stroke-width="2" fill="#1A2A33"></path></svg></button>
                      <button onClick={() => handleClickEvent('O')} className="false w-1/2 mx-auto flex justify-center items-center"><svg width="32" height="32" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M32 16C32 7.16344 24.8366 0 16 0C7.16344 0 0 7.16344 0 16C0 24.8366 7.16344 32 16 32C24.8366 32 32 24.8366 32 16ZM9.48145 16C9.48145 12.3999 12.3999 9.48147 16 9.48147C19.6 9.48147 22.5185 12.3999 22.5185 16C22.5185 19.6001 19.6 22.5185 16 22.5185C12.3999 22.5185 9.48145 19.6001 9.48145 16Z" stroke-width="2" stroke="#1A2A33" fill="#A8BFC9"></path></svg></button>

                    </div>
                    <h3 className="text-gray-500">REMEMBER : {selected} GOES FIRST</h3>                
                </div>
                <article className="flex flex-col gap-3 w-[90%]">
                  <div className="w-full bg-yellow-500 rounded-2xl pb-2">
                    <button onClick={() => handleGameOpponent(false)} className="uppercase text-black-400  py-3 px-3 cursor-default bg-yellow-400 rounded-2xl w-full">
                      new game (vs cpu)
                    </button>
                  </div>
                  <div onClick={() => handleGameOpponent(true)} className="w-full bg-blue-500 rounded-2xl pb-2">
                    <button className="uppercase text-black-400  py-3 px-3 cursor-default bg-blue-400 rounded-2xl w-full">
                      new Game (vs player)
                    </button>
                  </div>
                  <div onClick={() => handleGameOpponent(true)} className="w-full bg-blue-500 rounded-2xl pb-2">
                    <button className="uppercase text-black-400  py-3 px-3 cursor-default bg-blue-400 rounded-2xl w-full">
                      new Game (online)
                    </button>
                  </div>
                </article>

            </section>
            : <Square opponent={opponent} onGame={onGame}/>
            }
        </main>
    )
}

export default Home;