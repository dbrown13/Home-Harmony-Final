import os
import shutil

# Import smtplib for the actual sending function
import smtplib
# Import the email modules
from email.message import EmailMessage

SUPPORT_EMAIL = 'home.harmony4357@gmail.com'
SUPPORT_PASSWORD = 'H0meHarm0ny'

"""
    This function deletes all images from the database by user_id.
    Parameters:
        connection (Connection): The database connection to use.
        user_id (int): The id of the user whose images to delete.
    Returns:
        bool: True if all images were deleted successfully, False otherwise.
"""    
def delete_uploaded_images() -> None:
    current_directory = os.getcwd()
    dir_path = os.path.relpath('static/uploads', start=current_directory)
    print(f"relative path: {dir_path}")
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

def send_email(email, textfile):
# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
    print(f"email: {email}")
    print(f"textfile: {textfile}")
    with open(textfile) as fp:
        print(fp)
        # Create a text/plain message
        msg = EmailMessage()
        msg.set_content(fp.read())

    print(f"msg = {msg}")
    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'The contents of %s' % textfile
    msg['From'] = email
    msg['To'] = SUPPORT_EMAIL

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(SUPPORT_EMAIL, SUPPORT_PASSWORD)
    s.sendmail(email, SUPPORT_EMAIL, msg)
    s.quit()