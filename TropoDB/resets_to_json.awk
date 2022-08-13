BEGIN {print "{\n\t\"resets\":["}
(NR == 1) {
    print "\t\t{\"zone\":"$2",\"count\":"$1"}"
} 
(NR > 1) {
    print "\t\t,{\"zone\":"$2",\"count\":"$1"}"
} 
END {print "\t]\n}"}
