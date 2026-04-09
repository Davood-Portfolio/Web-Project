// @ts-check

export function timeToMixJuice(name) {
  switch (name) {
    case 'Pure Strawberry Joy':
      return 0.5;
    case 'Energizer':
    case 'Green Garden':
      return 1.5;
    case 'Tropical Island':
      return 3;
    case 'All or Nothing':
      return 5;
    default:
      return 2.5;
  }
}

export function limesToCut(wedgesNeeded, limes) {
  let wedges = 0;
  let count = 0;

  for (let i = 0; i < limes.length && wedges < wedgesNeeded; i++) {
    count++;

    switch (limes[i]) {
      case 'small':
        wedges += 6;
        break;
      case 'medium':
        wedges += 8;
        break;
      case 'large':
        wedges += 10;
        break;
    }
  }

  return count;
}

export function remainingOrders(timeLeft, orders) {
  let i = 0;

  while (i < orders.length && timeLeft > 0) {
    timeLeft -= timeToMixJuice(orders[i]);
    i++;
  }

  return orders.slice(i);
}