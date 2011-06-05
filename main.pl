#!/opt/local/bin/perl

@lines;
$prev;
$break = 1;
$n = 0;
print "|| SYSTEM UP || \n";

sub the_loop{
	#write this code
	}

while (1) {
	$input = <STDIN>;
	chomp($input);
	if (scalar(@lines > 0)){
		the_loop();
	}
	else{
		@responses0;
		push(@responses0, $input);
		push(@lines, \@responses0);
		$prev = $input;
		print "$lines[0][0] \n";
	}
}