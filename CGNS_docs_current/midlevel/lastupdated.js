
function makeArray() {
for (i = 0; i < makeArray.arguments.length; i++) 
  this[i + 1] = makeArray.arguments[i]; 
}

var modifiedMonth = new makeArray('January','February','March','April',
                                  'May','June','July','August','September',
                                  'October','November','December');

var modifiedDate = new Date(document.lastModified);

function modifiedDay(day) { 
      if (day == 0) return 'Sunday'; 
else  if (day == 1) return 'Monday';
else  if (day == 2) return 'Tuesday'; 
else  if (day == 3) return 'Wednesday';
else  if (day == 4) return 'Thursday'; 
else  if (day == 5) return 'Friday';
else                return 'Saturday'; }

function modifiedDateSuffix(date) { 
     if (date == 1 || date == 21 || date == 31) return 'st'; 
else if (date == 2 || date == 22)               return 'nd';  
else if (date == 3 || date == 23)               return 'rd'; 
else                                            return 'th'; }

function getCorrectedYear(year) {
    year = year - 0;
    if (year < 70) return (2000 + year);
    if (year < 1900) return (1900 + year);
    return year;
}

document.write('Last Updated: ' + modifiedDay(modifiedDate.getDay()) + ', ' + 
                                    modifiedMonth[modifiedDate.getMonth() + 1] + ' ' + 
                                    modifiedDate.getDate() + 
                                    modifiedDateSuffix(modifiedDate.getDate()) + ', ' + 
                                    getCorrectedYear(modifiedDate.getFullYear()));
