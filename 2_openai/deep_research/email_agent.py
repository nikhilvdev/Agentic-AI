import os
from typing import Dict

import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content, To
from agents import Agent, function_tool

@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send an email with the Given Subject and HTML Body"""
    sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    from_email = Email('')
    to_email = Email('')
    content = Content('text/htrml', html_body)
    mail = Mail(from_email, subject, to_email, content).get()
    response = sg.client.mail.send.post(request_body=mail)
    print("Email response", response.status_code)


INSTRUCTIONS = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""

email_agent = Agent(
    name = "Email Agent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model="gpt-5-mini"
)
