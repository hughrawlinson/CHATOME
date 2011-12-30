#!/opt/local/bin/perl

@lines;
$prev;
$break = 1;
$n = 0;
$mbreak = 1;
print "|| SYSTEM UP ||\n";
print "|| BE AWARE THAT 'reset', 'save', 'load' AND 'quit' ARE RESERVED KEYWORDS ||\n";


sub the_loop{
	#if ($input != @lines[$n][0] || $n !> scalar(@lines)){
	#
	#}
}

sub save(@lines, @responses){

}

sub load{

}

while ($mbreak == 1) {
	$input = <STDIN>;
	chomp($input);
	if ($input eq "reset"){
		print "|| has been reset ||";
		system("clear");
	}
	elsif ($input eq "quit"){
		$mbreak = 2;
	}
	elsif ($input eq "save"){
		save();
	}
	elsif ($input eq "load"){
		load();
	}
	else{
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