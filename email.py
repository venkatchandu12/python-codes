import boto3
import os
# write a code to get data from dynamodb



# Initialize SES client
ses_client = boto3.client('ses', region_name="us-east-1")  # Change region if needed

# Environment variables for sender and recipient
SENDER = os.getenv("SENDER_EMAIL", "venkatchandupvc1@gmail.com")
RECIPIENT = os.getenv("RECIPIENT_EMAIL", "venkatchandupvc1@gmail.com")

# Sample data to display in the table
VARIABLES = {
    "SENDER_EMAIL": SENDER,
    "RECIPIENT_EMAIL": RECIPIENT,
    "REGION_NAME": "us-east-1",
    "SUBJECT": "Test Email from AWS Lambda",
    "BODY": "Hello, this is a test email sent from AWS Lambda using SES."
}

# Function to generate HTML table
def generate_html_table(data):
    table_html = "<table border='1' style='border-collapse: collapse; width: 100%;'>"
    table_html += "<tr><th style='padding: 8px; background-color: #f2f2f2;'>Variable</th><th style='padding: 8px; background-color: #f2f2f2;'>Value</th></tr>"
    
    for key, value in data.items():
        table_html += f"<tr><td style='padding: 8px;'>{key}</td><td style='padding: 8px;'>{value}</td></tr>"
    
    table_html += "</table>"
    return table_html

def lambda_handler(event, context):
    try:
        # Generate HTML email body
        html_body = f"""
        <html>
        <body>
            <p>Hello,</p>
            <p>Here are the details:</p>
            {generate_html_table(VARIABLES)}
            <p>Thanks and Regards,</p>
            <p><b>ChatGPT</b></p>
        </body>
        </html>
        """

        # Send Email
        response = ses_client.send_email(
            Source=SENDER,
            Destination={'ToAddresses': [RECIPIENT]},
            Message={
                'Subject': {'Data': "Test Email with Table from AWS Lambda"},
                'Body': {
                    'Html': {'Data': html_body}  # Sending HTML email
                }
            }
        )
        
        print(f"Email sent! Message ID: {response['MessageId']}")
        return {"statusCode": 200, "body": f"Email sent! Message ID: {response['MessageId']}"}
    
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return {"statusCode": 500, "body": str(e)}
