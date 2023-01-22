for i in $(find . -type d); do # Not recommended, will break on whitespace
[ -f $i/__init__.py ] || touch $i/__init__.py
   
done
