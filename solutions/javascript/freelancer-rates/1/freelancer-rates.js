export function dayRate(ratePerHour) {
  return ratePerHour * 8;
}

export function daysInBudget(budget, ratePerHour) {
  const dailyRate = dayRate(ratePerHour);
  return Math.floor(budget / dailyRate);
}

export function priceWithMonthlyDiscount(ratePerHour, numDays, discount) {
  const dailyRate = dayRate(ratePerHour);

  const fullMonths = Math.floor(numDays / 22);
  const remainingDays = numDays % 22;

  const discountedMonthCost =
    fullMonths * 22 * dailyRate * (1 - discount);

  const remainingCost = remainingDays * dailyRate;

  const total = discountedMonthCost + remainingCost;

  return Math.ceil(total);
}