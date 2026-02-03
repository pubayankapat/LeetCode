/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isTrionic = function(nums) {
     const n = nums.length;
  if (n < 4) return false; // minimum length needed

  let i = 1;

  // 1️⃣ strictly increasing
  while (i < n && nums[i] > nums[i - 1]) {
    i++;
  }
  // must have at least one increase AND not end here
  if (i === 1 || i === n) return false;

  // 2️⃣ strictly decreasing
  const decStart = i;
  while (i < n && nums[i] < nums[i - 1]) {
    i++;
  }
  // must have at least one decrease AND not end here
  if (i === decStart || i === n) return false;

  // 3️⃣ strictly increasing again
  while (i < n && nums[i] > nums[i - 1]) {
    i++;
  }

  // must reach the end
  return i === n;
};