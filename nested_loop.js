// Nested loop runtime

let indexSmallest;
let nums;
let temp;
let i;
let n;


for (let i = 0; i < n; ++i) {
    indexSmallest = i
    for (j = i + 1; j < n; ++j) {
        if (nums[i] < nums[indexSmallest]) {
            indexSmallest = j
        }
    }
    temp = nums[i]
    nums[i] = nums[indexSmallest]
    nums[indexSmallest] = temp
}