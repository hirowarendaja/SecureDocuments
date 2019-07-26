if [ $# -eq 3 ]                                                                        
then                                                                                 
if [ -d "tempnew" ];                                                           
then.                                                                                  
echo Dir tempnew already exists - other instance running?                      
exit 1                                                                         
fi                                                                                     
mkdir tempnew                                                                  
echo $1 $2 $3>> ./urllog.txt                                                   
cd tempnew                                                                     
/usr/local/bin/curl $1 -o$2                                                    
echo quit | /usr/local/bin/gs -sDEVICE=pnggray -sOutputFile=f%d.png -r300 $2   
/usr/local/bin/convert convert -density 300 ./f*.png -resize 50% [DocSec]$2    
mv [DocSec]$2 ../dl/                                                           
cd ..                                                                          
rm -rf ./tempnew                                                               
fi 
