const stampDutyBands = [
  { threshold: 125000, rate: 0 },
  { threshold: 125000, rate: 0.02 },
  { threshold: 675000, rate: 0.05 },
  { threshold: 575000, rate: 0.1 },
  { threshold: Infinity, rate: 0.12 },
];

const calculateStampDuty = (price: number): number => {
  const totalStampDuty = stampDutyBands.reduce(
    (stampDuty, { threshold, rate }) => {
      const value = Math.min(price, threshold);
      const tax = value * rate;

      price -= value;
      console.log(`Tax for band with threshold ${threshold} is ${tax}`);
      return stampDuty + tax;
    },
    0,
  );

  return totalStampDuty;
};

console.log(calculateStampDuty(2_000_000));
