/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    result = []
    function parenthesisBacktrack(left, right, n, res){
        if(left === n && right === n){
            result.push(res)
            return
        }
        if(left < n){
            parenthesisBacktrack(left + 1, right, n, res + "(")
        }
        if(right < left){
            parenthesisBacktrack(left, right + 1, n, res + ")")
        }
    }
    parenthesisBacktrack(0, 0, n, "")
    return result
};
