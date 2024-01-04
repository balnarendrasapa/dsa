impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack: Vec<i32> = Vec::new();

        for (index, value) in tokens.iter().enumerate(){
            if(value == "+" || value == "-" || value == "*" || value == "/"){
                let operandA = stack.pop().unwrap();
                let operandB = stack.pop().unwrap();
                if(value == "+"){
                    stack.push(operandB + operandA);
                }
                else if(value == "-"){
                    stack.push(operandB - operandA);
                }
                else if(value == "*"){
                    stack.push(operandB * operandA);
                }
                else if(value == "/"){
                    stack.push(operandB / operandA);
                }
            }
            else{
                stack.push(value.parse::<i32>().unwrap());
            }
        }
        return stack.pop().unwrap();
    }
}
