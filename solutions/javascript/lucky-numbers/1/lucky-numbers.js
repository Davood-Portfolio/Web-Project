// @ts-check

export function twoSum(array1, array2) {
  const num1 = Number(array1.join(''));
  const num2 = Number(array2.join(''));
  return num1 + num2;
}

export function luckyNumber(value) {
  const str = String(value);
  return str === str.split('').reverse().join('');
}

export function errorMessage(input) {
  // اگر ورودی خالی باشد (به جز 0)
  if (!input && input !== 0) {
    return 'Required field';
  }

  const num = Number(input);

 
  if (isNaN(num) || num === 0) {
    return 'Must be a number besides 0';
  }

  return '';
}