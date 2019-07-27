# SecureDocuments
Secure Documents consists of a webform (form.html), a Perl CGI script (index.cgi) as middleware and a shell script (rerender.sh) doing the actual conversion.

# Eliminating the Malicious Document Attack Vector

The risk of opening documents from untrusted sources was known to the IT-Sec community for a long time. 
Defending against this attack vector is no trivial task. 
Safely accessin or printing untrusted documents involves physically carrying the docs onto an isolated (not attached to the (internal) network) machine that boots off a Live-DVD or simmilar.
This method is not convenient when you are running a business and have to open countless invoices per month. 
In this use case there is no need for editing the documents, just reading or printing them often suffices.

This is where SecureDocuments can help:
These scripts use GhostScript and ImageMagick to render a pdf file (input pdf) into images, then repackaging the images into a pdf simmilar to the input pdf.

# Supportes File Formats
This version of SecureDocuments works with PDF and PS. 
Due to the high CPU cycles demanded by the rerendering, color is rendered into greyscale.

# Platforms
SecureDocuments works on BSD and on Linux.

## Cost / Benefit
Advantages:
 * Guaranteed free of malicious code
 * Rendering rerendered documents probably takes fewer CPU cycles 

Disadvantages:
 * Larger file
 * Forms do no longer work
 * Selecting text / copying text does not work

