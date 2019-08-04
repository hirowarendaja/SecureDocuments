#!/usr/bin/perl
use CGI;
use strict;
my $targetdir = "./dl"
if (-d $targetdir) {
	my $cgi = new CGI();
	if (! $cgi->param("u") ) {	#we're invoked directly, display the form and get out.
		print "Content-type: text/html\n\n";
		DisplayForm();
		exit;
	}
	my $pdfurl = $cgi->param('u');
	$pdfurl =~ s/(\")/%22/g;
	$pdfurl =~ s/( )|(\\r)|(\\n)|(\\)//g;
	my $pdfbasename = GetBasename($pdfurl);
	my $returnpath = $targetdir+"/"+$pdfbasename;
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
		print "<p><h2>Something went wrong while cleaning the file on $pdfurl</h2></body></html>";
	}
} else {
	print "Content-type: text/html\n\n";
	print "<html><head><title>Directory missing</title></head><body><h1>The Directory &quot;dl&quot; is missing, please inform the administrator!</h1></body></html>";
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

# DisplayForm - spits out HTML to display the input form.
sub DisplayForm {
	open (HTMLFORM, "<form.html") or die "Couldn't open file $!";
	while(<HTMLFORM>) {
   		print "$_";
      	}
}
