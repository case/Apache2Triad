#!C:/apache2triadpath/perl/bin/perl.exe

print "Content-type: text/html\n\n";

$file = 'count.txt';

$foobar = 0;
open(FILE,"<$file") or die "cant read $file";
$foobar = <FILE>;
close(FILE);
$foobar += 1;
open(FILE,">$file") or die "cant write $file";
print FILE $foobar;
close(FILE);
print "$foobar";
exit;
