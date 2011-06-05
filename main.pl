#!/opt/local/bin/perl

@lines;
$break = 1;
$n = 0;
print "|| SYSTEM UP ||\n";

sub the_loop{
	#write this code
	}

while (1) {
	$input = <STDIN>;
	print '\n';
	chomp($input);
	if (scalar(@lines > 0)){
		the_loop();
	}
	else{
		push @{ $lines[0] = @responses0};
		@lines[0][0] = $input;
		$prev = @lines[0][0];
		print @lines[0][0] . '\n';
	}
}