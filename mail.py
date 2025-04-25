import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "mail.pratesis.com"
port = 587
sender_email = "sinno@pratesis.com"
receiver_email = "pfebrian@gmail.com"
password = "Bangka_2024!"

# Buat email
message = MIMEMultipart("alternative")
message["Subject"] = "Test Email via SMTP Pratesis"
message["From"] = sender_email
message["To"] = receiver_email

# Konten email
text = """\
Hi,
Ini adalah email uji coba kirim SMTP via Python.
"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       Ini adalah <b>email uji coba</b> kirim SMTP via Python.<br>
    </p>
  </body>
</html>
"""

# Tambahkan konten ke pesan
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

# Kirim email
try:
    server = smtplib.SMTP(smtp_server, port, timeout=10)
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("✅ Email berhasil dikirim ke", receiver_email)
    server.quit()
except Exception as e:
    print("❌ Gagal mengirim email:", e)
