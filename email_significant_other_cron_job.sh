crontab -l > email_significant_other
# Send significant other email at 11:00 a.m. every Sunday
echo "00 11 * * 0 /usr/local/bin/python3.7 ~/significant-other-reminders/email_significant_other_weekly_reminders.py" >> email_significant_other
crontab email_significant_other