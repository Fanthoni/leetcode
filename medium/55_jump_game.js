/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    const arrLength = nums.length;

    console.log(nums);

    // if len == 1
    // return true
    if (arrLength === 1) return true;

    let currIndex = 0 ;
    while (currIndex < arrLength - 1) {
        // console.log(nums[currIndex], arrLength - currIndex);
        if (nums[currIndex] >= arrLength - currIndex - 1) {
            return canJump(nums.splice(0, currIndex + 1))
        } else {
            currIndex += 1;
        }
    }
    return false

    
    // while current index is not -1
    // if any of the elements > len - index then call canJump to that index
    // for every element before the last element starting from the back
        // check if that number is bigger than the len - index
        // if so , recurse call up to that number
        // if not keep going back

    // [2, 3, 1, 1]
    //  [2, 3, 1]
    // [2, 3]
    // [2]

    // else false

    // [3, 2, 3, 0, 4]
    // [3, 2, 3]
    // []
};

console.log(canJump([2,3,1,0,4])); // true
// canJump([3, 2, 1, 0, 4]); // false