local p = {}
p.update = {}
p.month_index = {
	january = 1, feb = 2, february = 2, mar = 3, march = 3, apr = 4, april = 4,
	may = 5, jun = 6, june = 6, jul = 7, july = 7, aug = 8, august = 8,
	sep = 9, september = 9, oct = 10, october = 10, nov = 11, november = 11,
	dec = 12, december = 12
}
p.long_month = {
	"January", "February", "March", "April", "May", "June", 
	"July", "August", "September", "October", "November", "December"
}
p.short_month = {
	"Jan", "Feb", "Mar", "Apr", "May", "Jun", 
	"Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
}
return p