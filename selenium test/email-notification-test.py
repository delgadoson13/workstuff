import yagmail
yag = yagmail.SMTP('thisdayinpunkhistory@gmail.com', 'Pindjs2021!')
contents = ["This is the body of my email. You're welcome."]
email_dist_list = ['martindelgado1983@yahoo.com', 'martin.delgado@saisd.org']
for email in email_dist_list:
    yag.send(email, 'Testing from yagmail', contents)
