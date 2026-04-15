// @ts-check

export function getFirstCard([firstCard]) {
  return firstCard;
}

export function getSecondCard([, secondCard]) {
  return secondCard;
}

export function swapTwoCards([firstCard, secondCard]) {
  return [secondCard, firstCard];
}

export function shiftThreeCardsAround([firstCard, secondCard, thirdCard]) {
  return [secondCard, thirdCard, firstCard];
}

export function pickNamedPile({ chosen }) {
  return chosen;
}

export function swapNamedPile({ chosen, disregarded }) {
  return { chosen: disregarded, disregarded: chosen };
}