// @ts-check

export function cardTypeCheck(stack, card) {
  let count = 0;
  stack.forEach((currentCard) => {
    if (currentCard === card) {
      count++;
    }
  });
  return count;
}

export function determineOddEvenCards(stack, type) {
  let count = 0;

  for (const currentCard of stack) {
    if (type && currentCard % 2 === 0) {
      count++;
    }
    if (!type && currentCard % 2 !== 0) {
      count++;
    }
  }

  return count;
}