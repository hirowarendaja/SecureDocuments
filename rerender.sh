if [ $# -eq 2 ]
then
	MYCONVERT=`which convert`
	MYGS=`which gs`	
	MYWGET=`which wget`
	MYECHO=`which echo`
	MYMKDIR=`which mkdir`
	MYRM=`which rm`
	MYMV=`which mv`
        if [ -d "tempnew" ];
	then 
        	$MYECHO Dir tempnew already exists - other instance running?
        	exit 1
	fi
        $MYMKDIR tempnew
        $MYECHO $1 $2 $3>> ./urllog.txt
        cd tempnew
        $MYWGET "$1" -Otempfile.pdf
        $MYECHO quit | $MYGS -sDEVICE=pnggray -sOutputFile=f%d.png -r300 tempfile.pdf
        $MYCONVERT -density 300 ./f*.png -resize 50% "$2"
        $MYMV "$2" ../dl/
        cd ..
        $MYRM -rf ./tempnew
else
	$MYECHO "Please use $0 URL FILENAME, not $0 $1 $2!"
fi
