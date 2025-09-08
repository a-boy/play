use strict;
use warnings;
use Net::SMTP;

my $smtp_server = 'smtp.outlook.com';
my $port = 465; # Or 465 for SMTPS, 25 for plain SMTP
my $username = 'a_boy';
my $password = '';
my $sender = 'a_boy@live.com';
my $recipient = 'avvboy@gmail.com';
my $subject = 'Test Email from Perl';
my $body = 'This is a test email sent using Net::SMTP in Perl.';

my $smtp = Net::SMTP->new(
    $smtp_server,
    Port => $port,
    Debug => 1, # Set to 1 for debugging output
    SSL => 1, # Use if connecting with SMTPS (implicit SSL)
    # StartTLS => 1, # Use if connecting with STARTTLS (explicit TLS)
) or die "Could not connect to SMTP server: $!";

# Authenticate if required
$smtp->auth($username, $password) or die "Authentication failed: $!";

# Send the email
$smtp->mail($sender) or die "Could not set sender: $!";
$smtp->to($recipient) or die "Could not set recipient: $!";
$smtp->data() or die "Could not initiate data transfer: $!";
$smtp->datasend("From: $sender\r\n");
$smtp->datasend("To: $recipient\r\n");
$smtp->datasend("Subject: $subject\r\n");
$smtp->datasend("\r\n"); # End of headers
$smtp->datasend("$body\r\n");
$smtp->dataend() or die "Could not end data transfer: $!";

$smtp->quit();
print "Email sent successfully.\n";