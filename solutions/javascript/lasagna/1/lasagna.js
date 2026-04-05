// @ts-check

/**
 * The number of minutes it takes to prepare a single layer.
 */
export const PREPARATION_MINUTES_PER_LAYER = 2;

/**
 * The expected oven time in minutes.
 */
export const EXPECTED_MINUTES_IN_OVEN = 40;

/**
 * Calculates remaining oven time.
 */
export function remainingMinutesInOven(actualMinutesInOven) {
  return EXPECTED_MINUTES_IN_OVEN - actualMinutesInOven;
}

/**
 * Calculates preparation time.
 */
export function preparationTimeInMinutes(numberOfLayers) {
  return numberOfLayers * PREPARATION_MINUTES_PER_LAYER;
}

/**
 * Calculates total time.
 */
export function totalTimeInMinutes(numberOfLayers, actualMinutesInOven) {
  return (
    preparationTimeInMinutes(numberOfLayers) +
    actualMinutesInOven
  );
}