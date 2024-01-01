/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    let n = heights.length;
    if(n === 0){
        return 0;
    }
    let max_val = Number.MIN_SAFE_INTEGER
    let left = new Array(n).fill(0)
    let right = new Array(n).fill(0)

    left[0] = -1
    right[n-1] = n

    for(let i = 1; i < n; i++){
        let prev = i - 1
        while(prev >= 0 && heights[prev] >= heights[i]){
            prev = left[prev]
        }
        left[i] = prev
    }
    
    for(let i = n - 2; i >= 0 ; i--){
        let next = i + 1
        while(next < n && heights[next] >= heights[i]){
            next = right[next]
        }
        right[i] = next
    }

    for(i in heights){
        area = (right[i] - left[i] - 1) * heights[i]
        if(max_val < area){
            max_val = area
        }
    }
    return max_val
};
