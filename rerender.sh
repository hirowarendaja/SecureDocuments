if [ $# -eq 3 ]
  then
        if [ -d "tempnew" ];
then 
        echo Dir tempnew already exists - other instance running?
        exit 1
fi
        mkdir tempnew
        echo $1 $2 $3>> ./urllog.txt
        cd tempnew
        /usr/local/bin/wget "$1" -Otempfile.pdf
        echo quit | /usr/local/bin/gs -sDEVICE=pnggray -sOutputFile=f%d.png -r300 tempfile.pdf
        /usr/local/bin/convert -density 300 ./f*.png -resize 50% "[DocSec]$2"
        mv "[DocSec]$2" ../dl/
        cd ..
        rm -rf ./tempnew
else
echo "Please use $0 URL FILENAME 123 not $1 $2 $3"
fi
