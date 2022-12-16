## AutoMail

This projects aims to provide the functionality to send emails to multiple users at a time.

The User needs to Authenticate his account for this task to be able to send emails from his account.
To do that follow the instructions <a href="https://www.febooti.com/products/automation-workshop/tutorials/enable-google-app-passwords-for-smtp.html">here </a>

The following fields at available for the users to send the Message.
<ul>
  <li><b>Sender email</b> - Email from which emails need to be sent</li>
  <li><b>Sender password</b> - App password that was set while follwong the instrucions above</li>
  <li><b>Sender Name</b> - Username which appears to the receiver</li>
  <li><b>Receiver Email</b> -This is the email-id(s) which will receive the email.
         Instead of typing one email id at a time, a csv file containing email-ids in the first columns can also be uploaded. 
          All the email-ids in the csv file will be sent the email seperately.</li>
  
  <li><b>Subject</b> - Subject of the Email</li>
  <li><b>Attachments</b> - Any attachments which needs to be sent</li>
  <li><b>Message Body</b> - The Email Body. It accepts text in the form of HTML document, therefore any html (email) can be sent with this
                              message.</li>

  
</ul>

After sending the Message the header displays total successful emails and a success report is downloded in text format specifying which emails were successful.
  
 ### Installation
 
 <b><h4>Cloning the Repo in your local machine</h4></b>
  <ul>
  <li> Clone this repo<code>git clone git@github.com:Pranay-Pandey/AutoMail.git</code></li>
  <li> Go inside the repo<code>cd AutoMail</code> </li>
  <li> You can create a virtual environment<code>python3 -m venv .env</code> </li>
  <li> Activate this environment with <code> source .env/bin/activate</code> </li>
  <li> Download the requirements <code>pip install -r requirements.txt</code></li>
  <li> Run the server <code>python manage.py runserver</code></li>
  </ul>
  
