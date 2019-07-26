#!/usr/bin/perl
use CGI;
use strict;
#use Digest::MD5 qw(md5 md5_hex md5_base64);

my $cgi = new CGI();

if (! $cgi->param("u") ) {
#we're invoked directly, display the form and get out.
	print "Content-type: text/html\n\n";
#	 print "<html><head><title>Secure Documents</title><meta http-equiv=\"refresh\" content=\"0; url=/\" /></head><body></body></html>";
	exit;
}

my $pdfurl = $cgi->param('u');
#$pdfurl =~ s/([^^A-Za-z0-9\-_.!~*'()])/ sprintf "%%%0x", ord $1 /eg;

my $pdfbasename = GetBasename($pdfurl);

my $returnpath = "./dl/$pdfbasename";

if (-e $returnpath) {
	print "Target file already exists!";
	exit;}
my $response = `./rerender.sh "$pdfurl" "$pdfbasename" 123`;
if (-e $returnpath) {
# return converted file
print "Content-type: application/pdf\n
Content-Disposition: attachment; filename=\"$pdfbasename\"\n";
open (PDFFILE, "<$returnpath") or die "Couldn't open file $!";
while(<PDFFILE>) {
   print "$_";
   }

} else {
print "Content-type: text/html\n\n";
print "<html><head><title>Secure DocumentsPDF</title></head><body>";
print $response;
print "Something went wrong while cleaning the file on $pdfurl";
}



##############################################
# Subroutines
##############################################

#
# GetBasename - delivers filename portion of a fullpath.
#
sub GetBasename {
	my $fullname = shift;

	my(@parts);
	# check which way our slashes go.
	if ( $fullname =~ /(\\)/ ) {
		@parts = split(/\\/, $fullname);
	} else {
		@parts = split(/\//, $fullname);
	}

	return(pop(@parts));
}

#
# DisplayForm - spits out HTML to display our upload form.
#
sub DisplayForm {
open (HTMLFORM, "<form.html") or die "Couldn't open file $!";
while(<HTMLFORM>) {
   print "$_";

      }
}
