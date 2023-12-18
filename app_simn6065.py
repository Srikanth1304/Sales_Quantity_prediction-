import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, Response
import io
import base64

app = Flask(__name__)

def read_excel_data(file_path):
    # Assuming the data is in the first sheet of the Excel file
    df = pd.read_excel(file_path)

    # Convert 'month' column to int64 dtype
    df['month'] = pd.to_numeric(df['month'])

    return df

def generate_line_plot(data):
    # Convert 'Year' column to strings to match the 'month' column data type
    data['Year'] = data['Year'].astype(str)

    # Create a 'Date' column by combining 'month' and 'Year'
    data['Date'] = pd.to_datetime(data['month'] + '-' + data['Year'])

    x = data['Date']  # Use the 'Date' column as the X-axis data
    y = data['QUANTITY']  # Use the 'QUANTITY' column as the Y-axis data

    plt.figure(figsize=(12, 6))  # Adjust the figure size if needed
    plt.plot(x, y, marker='o', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('QUANTITY')
    plt.title('Line Plot of QUANTITY over Time')
    plt.xticks(rotation=45)  # Rotate X-axis labels for better readability

    # Show the values when the cursor is over the line
    for i in range(len(data)):
        x_val, y_val = x[i], y[i]
        plt.annotate(str(y_val), (x_val, y_val), ha='center', va='bottom')

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Encode the plot image to base64
    plot_base64 = base64.b64encode(buffer.getvalue()).decode()

    return plot_base64


@app.route('/')
def index():
    file_path = r'C:\Users\srikanth\Desktop\sales_charts\simn6065.xlsx'  
    data = read_excel_data(file_path)
    plot_base64 = generate_line_plot(data)
    return render_template('index2.html', plot_base64=plot_base64)

if __name__ == '__main__':
    app.run(debug=True)