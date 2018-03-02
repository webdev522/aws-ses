import boto3
from botocore.exceptions import ClientError

def sendTemplate1(user, product):
  
  SENDER = "Sender Name <richard@sprismi.com>"

  RECIPIENT = "richard@sprismi.com"

  AWS_REGION = "us-west-2"

  SUBJECT = "Amazon SES Test (SDK for Python)"


  BODY_HTML = """
  <html>
  <head></head>
  <body style="box-sizing: border-box; padding: 0; margin: 0; background-image: linear-gradient(to bottom, #0086fc, #0086fc 300px, #f6f6f6 300px);">
    <div style="text-align:center;">
      <p style="margin-top: 35px; font-family: Arial; font-size: 30px; text-align: center; color: white;">Header</p>
    </div>
    <div style="max-width: 100%; width: 768px; background: white; margin: 0 auto; margin-top: 70px; border-radius: 6px; box-shadow: 0 3px 12px 0 rgba(103, 103, 103, 0.24), 0 0 2px 0 rgba(0, 0, 0, 0.12); box-sizing: border-box; padding: 60px;">
      <h1 style="margin-bottom: 60px; font-family: Arial; font-size: 30px; text-align: center; color: #2e4255;">
        Title1
      </h1>
      <p style="font-family: Arial;	font-size: 18px; line-height: 1.7;	text-align: left; margin-top: 50px">
        Hi <b>{}</b>,<br/>
        Thanks for reaching out to us we are delighted to know that you {} arrived in time
      </p>
    </div>
    <div style="text-align: center; margin: 0 auto; margin-top: 70px; margin-bottom: 20px; color: #a3a3a3; font-family: Arial; font-size: 18px; line-height: 24px;">
      Copyright © 2017, All rights reserved.<br/>
      This will be the footer for each of the emails
    </div>
  
  </body>
  </html>
              """.format(user, product)            

  CHARSET = "UTF-8"

  client = boto3.client('ses',region_name=AWS_REGION)

  try:
      response = client.send_email(
          Destination={
              'ToAddresses': [
                  RECIPIENT,
              ],
          },
          Message={
              'Body': {
                  'Html': {
                      'Charset': CHARSET,
                      'Data': BODY_HTML,
                  },
              },
              'Subject': {
                  'Charset': CHARSET,
                  'Data': SUBJECT,
              },
          },
          Source=SENDER,
      )
  
  except ClientError as e:
      print(e.response['Error']['Message'])
  else:
      print("Email sent! Message ID:"),
      print(response['ResponseMetadata']['RequestId'])


def sendTemplate2(user, surveyNo):
  
  SENDER = "Sender Name <richard@sprismi.com>"

  RECIPIENT = "richard@sprismi.com"

  AWS_REGION = "us-west-2"

  SUBJECT = "Amazon SES Test (SDK for Python)"


  BODY_HTML = """
  <html>
  <head></head>
  <body style="box-sizing: border-box; padding: 0; margin: 0; background-image: linear-gradient(to bottom, #0086fc, #0086fc 300px, #f6f6f6 300px);">
    <div style="text-align:center;">
      <p style="margin-top: 35px; font-family: Arial; font-size: 30px; text-align: center; color: white;">Header</p>
    </div>
    <div style="max-width: 100%; width: 768px; background: white; margin: 0 auto; margin-top: 70px; border-radius: 6px; box-shadow: 0 3px 12px 0 rgba(103, 103, 103, 0.24), 0 0 2px 0 rgba(0, 0, 0, 0.12); box-sizing: border-box; padding: 60px;">
      <h1 style="margin-bottom: 60px; font-family: Arial; font-size: 30px; text-align: center; color: #2e4255;">
        Title2
      </h1>
      <p style="font-family: Arial;	font-size: 18px; line-height: 1.7;	text-align: left; margin-top: 50px">
        Hi <b>{}</b>,<br/>
        thanks for being such a loyal customer, would you mind filling out survey number {}
      </p>
    </div>
    <div style="text-align: center; margin: 0 auto; margin-top: 70px; margin-bottom: 20px; color: #a3a3a3; font-family: Arial; font-size: 18px; line-height: 24px;">
      Copyright © 2017, All rights reserved.<br/>
      This will be the footer for each of the emails
    </div>
  
  </body>
  </html>
              """.format(user, surveyNo)            

  CHARSET = "UTF-8"

  client = boto3.client('ses',region_name=AWS_REGION)

  try:
      response = client.send_email(
          Destination={
              'ToAddresses': [
                  RECIPIENT,
              ],
          },
          Message={
              'Body': {
                  'Html': {
                      'Charset': CHARSET,
                      'Data': BODY_HTML,
                  },
              },
              'Subject': {
                  'Charset': CHARSET,
                  'Data': SUBJECT,
              },
          },
          Source=SENDER,
      )
  
  except ClientError as e:
      print(e.response['Error']['Message'])
  else:
      print("Email sent! Message ID:"),
      print(response['ResponseMetadata']['RequestId'])

# sendTemplate1("User1", "Product1")
sendTemplate2("User2", "12345")