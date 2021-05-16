combine:
	cat all.txt banned.txt | sort -u > all+.txt
	cat all+.txt banned.txt | sort | uniq -u > available.txt
	for e in $$(cat banned_classes.txt); do sed -i "/^$$e::/d" available.txt; done

clean:
	rm all+.txt available.txt
