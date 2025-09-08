#!/usr/bin/perl
use strict;
use warnings;

# first, create your message
use Email::MIME;
my $message = Email::MIME->create(
  header_str => [
    From    => 'avvboy@gmail.com',
    To      => 'a_boy@live.com',
    Subject => 'Happy birthday!',
  ],
  attributes => {
    encoding => 'quoted-printable',
    charset  => 'UTF-8',
  },
  body_str => "Happy birthday to you!\n",
);

# send the message
use Email::Sender::Simple qw(sendmail);
sendmail($message);