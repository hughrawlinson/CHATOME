#!/opt/local/bin/perl

@lines;
$prev;
$break = 1;
$n = 0;
print "|| SYSTEM UP ||\n";
print "|| BE AWARE THAT 'reset' IS A RESERVED KEYWORD ||\n";


sub the_loop{
	#if ($input != @lines[$n][0] || $n !> scalar(@lines)){
	#
	#}
}

while (1) {
	$input = <STDIN>;
	if ($input eq "reset"){
	}
	else{
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
}