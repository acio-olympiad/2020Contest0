for f in ../data/*.in; do
if ! ./sub4 < $f; then
break
else
	echo "$f pass"
fi
done
