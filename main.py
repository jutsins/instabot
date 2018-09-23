import createMail
import createInsta

email = createMail.retrieve_email()
createInsta.create_account(email)
