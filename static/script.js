// chessboard.js

export function generateChessboard(containerSelector) {
  const container = document.querySelector(containerSelector);
  if (!container) return;

  for (let row = 0; row < 8; row++) {
    for (let col = 0; col < 8; col++) {
      const square = document.createElement('div');
      square.classList.add('square');
      if ((row + col) % 2 === 0) {
        square.classList.add('white');
      } else {
        square.classList.add('black');
      }
      container.appendChild(square);
    }
  }
}

