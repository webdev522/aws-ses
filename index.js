const AWS = require('aws-sdk');
const striptags = require('striptags');
// const moment = require('moment');

// const ses = new AWS.SES({ region: 'us-east-1' });
const ses = new AWS.SES({ region: 'us-west-2' });

// const {
//   MAIL_SENDER_SUPPORT: 'richard@sprismi.com',
//   MAIL_SENDER_SALES: senderSales,
//   MAIL_SENDER_BILLING: senderBilling,
//   MAIL_SENDER_NOTIFICATIONS: senderNotifications,
//   MAIL_SENDER_TITLE: senderTitle,
//   MAIL_SITE_LINK: siteLink
// } = process.env;

const sendMail = ({
  to,
  subject,
  body,
  from
}) => {
  return new Promise((resolve, reject) => {
    const params = {
      Destination: {
        ToAddresses: (() => {
          if (typeof to === 'string') {
            return [to];
          }
          return to;
        })()
      },
      Message: {
        Body: {
          Html: {
            Charset: 'UTF-8',
            Data: body
          },
          Text: {
            Charset: 'UTF-8',
            Data: striptags(body)
          }
        },
        Subject: {
          Charset: 'UTF-8',
          Data: subject
        }
      },
      Source: from
    };

    ses.sendEmail(params, (err, data) => {
      if (err) {
        reject(err);
      }
      resolve(data);
    });
  });
};

// send verification mail
const sendSignupVerification = (firstName, lastName, email, code) => {
  sendMail({
    to: `${email}`,
    subject: 'Email Verification',
    // from: `Richard <support@pulsesyndicate.com>`,
    from: `Richard <richard@sprismi.com>`,
    body: `
      <body style="box-sizing: border-box; padding: 0; margin: 0; background-image: linear-gradient(to bottom, #0086fc, #0086fc 450px, #f6f6f6 450px);">
        <div style="text-align:center;">
          <a href="https://google.com">
            <img src="https://s3.us-east-2.amazonaws.com/ps-app-bucket/pulsepro/logo.png" style="width: 255px;  height: 118px; margin-top: 35px"/>
          </a>
        </div>
        <div style="max-width: 100%; width: 768px; background: white; margin: 0 auto; margin-top: 70px; border-radius: 6px; box-shadow: 0 3px 12px 0 rgba(103, 103, 103, 0.24), 0 0 2px 0 rgba(0, 0, 0, 0.12); box-sizing: border-box; padding: 60px;">
          <h1 style="margin-bottom: 60px; font-family: Arial; font-size: 30px; text-align: center; color: #2e4255;">
            Email Confirmation
          </h1>
          <p style="font-family: Arial;	font-size: 18px; line-height: 1.7;	text-align: left; margin-top: 50px">
            Dear <b>${firstName} ${lastName}</b>,<br/>
            You have successfully created a PulseSyndicate account.
            <br/><br/>
            Please click on the link below to verify your email address and complete your registration.
          </p>
          <div style="text-align: center; margin-top: 50px;">
            <a href="https://google.com" style="text-decoration: none; width: 400px; display:block; margin: 0 auto; background: #0ebe4a; color: white; font-family: Arial;
                                                                                font-size: 20px;
                                                                                font-weight: bold; height: 60px; border-radius: 30px; line-height: 60px;">
              VERIFY YOUR EMAIL ADDRESS
            </a>
          </div>
          <p style="font-family: Arial;	font-size: 18px; line-height: 1.7;	text-align: center; margin-top: 30px; margin-bottom: 0px">
            or copy and paste this link into your browser:
          </p>
          <a href="https://google.com" style="text-align:center; display:block;">https://google.com</a>
        </div>
        <div style="text-align: center; margin: 0 auto; margin-top: 70px; margin-bottom: 20px; color: #a3a3a3; font-family: Arial; font-size: 18px; line-height: 24px;">
          Copyright © 2017 Pulse Sydicate, All rights reserved.<br/>
          51 W 84th St APT 2, New York, New York 10024, USA
        </div>
      </body>
    `
  });
};

sendSignupVerification("web", "Dev", "webdev522@gmail.com", "xyz");