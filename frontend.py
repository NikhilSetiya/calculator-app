import gradio as gr
import requests

def calculate(num1: float, num2: float, operation: str) -> str:
    try:
        response = requests.post(
            "http://localhost:8000/calculate",
            json={
                "num1": num1,
                "num2": num2,
                "operation": operation
            }
        )
        response.raise_for_status()
        result = response.json()
        return f"Result: {result['result']}"
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Create the Gradio interface
with gr.Blocks(title="Calculator") as demo:
    gr.Markdown("# Calculator")
    with gr.Row():
        num1 = gr.Number(label="First Number")
        num2 = gr.Number(label="Second Number")
    
    with gr.Row():
        operation = gr.Radio(
            choices=["add", "subtract", "multiply", "divide"],
            label="Operation",
            value="add"
        )
    
    with gr.Row():
        calculate_btn = gr.Button("Calculate")
        result = gr.Textbox(label="Result")
    
    calculate_btn.click(
        fn=calculate,
        inputs=[num1, num2, operation],
        outputs=result
    )

if __name__ == "__main__":
    demo.launch() 