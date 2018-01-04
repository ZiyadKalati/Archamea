# Archamea

archamea.pythonanywhere.com

A basic django-powered website just for practice. It's a wiki site that allows for account
creation and loggin in and out. When creating an account an email is sent to you with a link
to activate that account. Only then can you log in. When logged in you can edit and/or
create articles.

/*************************** Problems Being Fixed *************************************/

It's so incomplete because unexpected obstacles kept popping up. Here are the things I'm
currently looking to fix:

1) Serving Media Files In Production.

  All the uploaded files are not currently displayed. Normally you configure a dedicated
  server to do this like Apache, but I'm trying to do it inefficiently on the same
  server right now for simplicity's sake.
  
2) Sending Activation Emails Automatically
  
  Even though you can create an account, it won't send an email right away. The emails
  sit in a queue, and then have to be manually sent out.
  
  To play around with the website as it is you can use:
  
      Username: archamea
      Password: helloItsMe

3) Fixing Buttons On Home Page

  They stopped working when I changed the css from custom to bootstrap. Before the list of
  articles would be replaced by a fade in transition of a new list of articles.
  
  There were also button to the right that disappeared. They were made in javascript, and
  allowed for the user to view more than one list of articles simultaneously. The new list
  or lists would slide into view, and the width of the current list would shrink.
