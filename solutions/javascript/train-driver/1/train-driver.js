// @ts-check

export function getListOfWagons(...ids) {
  return ids;
}

export function fixListOfWagons(ids) {
  const wagonList = Array.from(ids);
  return [...wagonList.slice(2), ...wagonList.slice(0, 2)];
}

export function correctListOfWagons(ids, missingWagons) {
  const wagonList = Array.from(ids);
  const missingList = Array.from(missingWagons);
  return [wagonList[0], ...missingList, ...wagonList.slice(1)];
}

export function extendRouteInformation(information, additional) {
  return { ...information, ...additional };
}

export function separateTimeOfArrival(information) {
  const { timeOfArrival, ...rest } = information;
  return [timeOfArrival, rest];
}