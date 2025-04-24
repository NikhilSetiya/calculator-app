from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

class CalculatorInput(BaseModel):
    num1: float
    num2: float
    operation: str

class CalculatorResponse(BaseModel):
    result: float
    operation: str

@app.post("/calculate", response_model=CalculatorResponse)
async def calculate(input_data: CalculatorInput):
    result = 0.0
    
    if input_data.operation == "add":
        result = input_data.num1 + input_data.num2
    elif input_data.operation == "subtract":
        result = input_data.num1 - input_data.num2
    elif input_data.operation == "multiply":
        result = input_data.num1 * input_data.num2
    elif input_data.operation == "divide":
        if input_data.num2 == 0:
            raise ValueError("Cannot divide by zero")
        result = input_data.num1 / input_data.num2
    else:
        raise ValueError("Invalid operation")
    
    return CalculatorResponse(result=result, operation=input_data.operation)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 