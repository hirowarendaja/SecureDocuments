#!/usr/bin/perl
use CGI;
use strict;
my $cgi = new CGI();
if (! $cgi->param("u") ) {	#we're invoked directly, display the form and get out.
	print "Content-type: text/html\n\n";
	DisplayForm();
	exit;
}
my $pdfurl = $cgi->param('u');
my $pdfbasename = GetBasename($pdfurl);
my $returnpath = "./dl/$pdfbasename";
if (-e $returnpath) {
	print "Target file already exists <a href=\"$returnpath\"> here</a>!";
	exit;}
my $response = `./rerender.sh "$pdfurl" "$pdfbasename"`;
if (-e $returnpath) {	# return converted file
	print "Content-type: application/pdf\n
	Content-Disposition: attachment; filename=\"$pdfbasename\"\n";
	open (PDFFILE, "<$returnpath") or die "Could not open file $!";
	while(<PDFFILE>) {
   		print "$_";
   	}
} else { 		# Display error messages
	print "Content-type: text/html\n\n";
	print "<html><head><title>Secure DocumentsPDF</title></head><body>";
	print $response;
	print "Something went wrong while cleaning the file on $pdfurl";
}

### Subroutines

# GetBasename - delivers filename portion of a URI
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

# DisplayForm - spits out HTML to display our input form.
sub DisplayForm {
	open (HTMLFORM, "<form.html") or die "Couldn't open file $!";
	while(<HTMLFORM>) {
   		print "$_";
      	}
}
