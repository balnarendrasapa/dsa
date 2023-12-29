/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    stack = []
    flag = false
    for(let i of s){
        if(i === '[' || i === '(' || i === '{'){
            stack.push(i)
            flag = true
        }
        else{
            if((stack[stack.length - 1] === '(' && i === ')') || (stack[stack.length - 1] === '[' && i === ']') || (stack[stack.length - 1] === '{' && i === '}')){
                let k = stack.pop()
            }
            else{
                return false
            }
        }
    }
    if(flag === true && stack.length === 0){
        return true
    }
    else{
        return false
    }
};
