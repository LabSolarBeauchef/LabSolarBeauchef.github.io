/*
 Highcharts JS v6.0.3 (2017-11-14)
 Data module

 (c) 2012-2017 Torstein Honsi

 License: www.highcharts.com/license
*/
(function(w){"object"===typeof module&&module.exports?module.exports=w:w(Highcharts)})(function(w){(function(n){var w=n.win.document,t=n.each,C=n.objectEach,D=n.pick,z=n.inArray,A=n.isNumber,E=n.splat,F=n.fireEvent,B,v;B=Array.prototype.some?function(a,b,d){Array.prototype.some.call(a,b,d)}:function(a,b,d){for(var f=0,e=a.length;f<e&&!0!==b.call(d,a[f],f,a);f++);};var x=function(a,b){this.init(a,b)};n.extend(x.prototype,{init:function(a,b){this.options=a;this.chartOptions=b;this.columns=a.columns||
this.rowsToColumns(a.rows)||[];this.firstRowAsNames=D(a.firstRowAsNames,!0);this.decimalRegex=a.decimalPoint&&new RegExp("^(-?[0-9]+)"+a.decimalPoint+"([0-9]+)$");this.rawColumns=[];this.columns.length?this.dataFound():(this.parseCSV(),this.parseTable(),this.parseGoogleSpreadsheet())},getColumnDistribution:function(){var a=this.chartOptions,b=this.options,d=[],f=function(a){return(n.seriesTypes[a||"line"].prototype.pointArrayMap||[0]).length},e=a&&a.chart&&a.chart.type,c=[],h=[],m=0,g;t(a&&a.series||
[],function(a){c.push(f(a.type||e))});t(b&&b.seriesMapping||[],function(a){d.push(a.x||0)});0===d.length&&d.push(0);t(b&&b.seriesMapping||[],function(b){var d=new v,u=c[m]||f(e),l=n.seriesTypes[((a&&a.series||[])[m]||{}).type||e||"line"].prototype.pointArrayMap||["y"];d.addColumnReader(b.x,"x");C(b,function(a,b){"x"!==b&&d.addColumnReader(a,b)});for(g=0;g<u;g++)d.hasReader(l[g])||d.addColumnReader(void 0,l[g]);h.push(d);m++});b=n.seriesTypes[e||"line"].prototype.pointArrayMap;void 0===b&&(b=["y"]);
this.valueCount={global:f(e),xColumns:d,individual:c,seriesBuilders:h,globalPointArrayMap:b}},dataFound:function(){this.options.switchRowsAndColumns&&(this.columns=this.rowsToColumns(this.columns));this.getColumnDistribution();this.parseTypes();!1!==this.parsed()&&this.complete()},parseCSV:function(a){function b(a,b,c,d){function e(b){k=a[b];p=a[b-1];n=a[b+1]}function f(a){r.length<q+1&&r.push([a]);r[q][r[q].length-1]!==a&&r[q].push(a)}function g(){G>y||y>H?(++y,l=""):(!isNaN(parseFloat(l))&&isFinite(l)?
(l=parseFloat(l),f("number")):isNaN(Date.parse(l))?f("string"):(l=l.replace(/\//g,"-"),f("date")),m.length<q+1&&m.push([]),c||(m[q][b]=l),l="",++q,++y)}var h=0,k="",p="",n="",l="",y=0,q=0;if(a.trim().length&&"#"!==a.trim()[0]){for(;h<a.length;h++){e(h);if("#"===k){g();return}if('"'===k)for(e(++h);h<a.length&&('"'!==k||'"'===p||'"'===n);){if('"'!==k||'"'===k&&'"'!==p)l+=k;e(++h)}else d&&d[k]?d[k](k,l)&&g():k===u?g():l+=k}g()}}function d(a){var b=0,d=0,f=!1;B(a,function(a,c){var e=!1,f,k,g="";if(13<
c)return!0;for(var h=0;h<a.length;h++){c=a[h];f=a[h+1];k=a[h-1];if("#"===c)break;else if('"'===c)if(e){if('"'!==k&&'"'!==f){for(;" "===f&&h<a.length;)f=a[++h];"undefined"!==typeof q[f]&&q[f]++;e=!1}}else e=!0;else"undefined"!==typeof q[c]?(g=g.trim(),isNaN(Date.parse(g))?!isNaN(g)&&isFinite(g)||q[c]++:q[c]++,g=""):g+=c;","===c&&d++;"."===c&&b++}});f=q[";"]>q[","]?";":",";c.decimalPoint||(c.decimalPoint=b>d?".":",",e.decimalRegex=new RegExp("^(-?[0-9]+)"+c.decimalPoint+"([0-9]+)$"));return f}function f(a,
b){var d,f,g=0,h=!1,l=[],m=[],k;if(!b||b>a.length)b=a.length;for(;g<b;g++)if("undefined"!==typeof a[g]&&a[g]&&a[g].length)for(d=a[g].trim().replace(/\//g," ").replace(/\-/g," ").split(" "),f=["","",""],k=0;k<d.length;k++)k<f.length&&(d[k]=parseInt(d[k],10),d[k]&&(m[k]=!m[k]||m[k]<d[k]?d[k]:m[k],"undefined"!==typeof l[k]?l[k]!==d[k]&&(l[k]=!1):l[k]=d[k],31<d[k]?f[k]=100>d[k]?"YY":"YYYY":12<d[k]&&31>=d[k]?(f[k]="dd",h=!0):f[k].length||(f[k]="mm")));if(h){for(k=0;k<l.length;k++)!1!==l[k]?12<m[k]&&"YY"!==
f[k]&&"YYYY"!==f[k]&&(f[k]="YY"):12<m[k]&&"mm"===f[k]&&(f[k]="dd");a=f.join("/");return(c.dateFormats||e.dateFormats)[a]?a:(F("invalidDateFormat"),n.error("Could not deduce date format"),"YYYY/mm/dd")}return"YYYY/mm/dd"}var e=this,c=a||this.options,h=c.csv,m;a=c.startRow||0;var g=c.endRow||Number.MAX_VALUE,G=c.startColumn||0,H=c.endColumn||Number.MAX_VALUE,u,l=0,r=[],q={",":0,";":0,"\t":0};m=this.columns=[];if(h){h=h.replace(/\r\n/g,"\n").replace(/\r/g,"\n").split(c.lineDelimiter||"\n");if(!a||0>
a)a=0;if(!g||g>=h.length)g=h.length-1;c.itemDelimiter?u=c.itemDelimiter:(u=null,u=d(h));for(var p=0,l=a;l<=g;l++)"#"===h[l][0]?p++:b(h[l],l-a-p);c.columnTypes&&0!==c.columnTypes.length||!r.length||!r[0].length||"date"!==r[0][1]||c.dateFormat||(c.dateFormat=f(m[0]));this.dataFound()}return m},parseTable:function(){var a=this.options,b=a.table,d=this.columns,f=a.startRow||0,e=a.endRow||Number.MAX_VALUE,c=a.startColumn||0,h=a.endColumn||Number.MAX_VALUE;b&&("string"===typeof b&&(b=w.getElementById(b)),
t(b.getElementsByTagName("tr"),function(a,b){b>=f&&b<=e&&t(a.children,function(a,e){("TD"===a.tagName||"TH"===a.tagName)&&e>=c&&e<=h&&(d[e-c]||(d[e-c]=[]),d[e-c][b-f]=a.innerHTML)})}),this.dataFound())},parseGoogleSpreadsheet:function(){var a=this,b=this.options,d=b.googleSpreadsheetKey,f=this.columns,e=b.startRow||0,c=b.endRow||Number.MAX_VALUE,h=b.startColumn||0,m=b.endColumn||Number.MAX_VALUE,g,n;d&&jQuery.ajax({dataType:"json",url:"https://spreadsheets.google.com/feeds/cells/"+d+"/"+(b.googleSpreadsheetWorksheet||
"od6")+"/public/values?alt\x3djson-in-script\x26callback\x3d?",error:b.error,success:function(b){b=b.feed.entry;var d,l=b.length,r=0,q=0,p;for(p=0;p<l;p++)d=b[p],r=Math.max(r,d.gs$cell.col),q=Math.max(q,d.gs$cell.row);for(p=0;p<r;p++)p>=h&&p<=m&&(f[p-h]=[],f[p-h].length=Math.min(q,c-e));for(p=0;p<l;p++)d=b[p],g=d.gs$cell.row-1,n=d.gs$cell.col-1,n>=h&&n<=m&&g>=e&&g<=c&&(f[n-h][g-e]=d.content.$t);t(f,function(a){for(p=0;p<a.length;p++)void 0===a[p]&&(a[p]=null)});a.dataFound()}})},trim:function(a,b){"string"===
typeof a&&(a=a.replace(/^\s+|\s+$/g,""),b&&/^[0-9\s]+$/.test(a)&&(a=a.replace(/\s/g,"")),this.decimalRegex&&(a=a.replace(this.decimalRegex,"$1.$2")));return a},parseTypes:function(){for(var a=this.columns,b=a.length;b--;)this.parseColumn(a[b],b)},parseColumn:function(a,b){var d=this.rawColumns,f=this.columns,e=a.length,c,h,m,g,n=this.firstRowAsNames,t=-1!==z(b,this.valueCount.xColumns),u=[],l=this.chartOptions,r,q=(this.options.columnTypes||[])[b],l=t&&(l&&l.xAxis&&"category"===E(l.xAxis)[0].type||
"string"===q);for(d[b]||(d[b]=[]);e--;)c=u[e]||a[e],m=this.trim(c),g=this.trim(c,!0),h=parseFloat(g),void 0===d[b][e]&&(d[b][e]=m),l||0===e&&n?a[e]=""+m:+g===h?(a[e]=h,31536E6<h&&"float"!==q?a.isDatetime=!0:a.isNumeric=!0,void 0!==a[e+1]&&(r=h>a[e+1])):(h=this.parseDate(c),t&&A(h)&&"float"!==q?(u[e]=c,a[e]=h,a.isDatetime=!0,void 0!==a[e+1]&&(c=h>a[e+1],c!==r&&void 0!==r&&(this.alternativeFormat?(this.dateFormat=this.alternativeFormat,e=a.length,this.alternativeFormat=this.dateFormats[this.dateFormat].alternative):
a.unsorted=!0),r=c)):(a[e]=""===m?null:m,0!==e&&(a.isDatetime||a.isNumeric)&&(a.mixed=!0)));t&&a.mixed&&(f[b]=d[b]);if(t&&r&&this.options.sort)for(b=0;b<f.length;b++)f[b].reverse(),n&&f[b].unshift(f[b].pop())},dateFormats:{"YYYY/mm/dd":{regex:/^([0-9]{4})[\-\/\.]([0-9]{1,2})[\-\/\.]([0-9]{1,2})$/,parser:function(a){return Date.UTC(+a[1],a[2]-1,+a[3])}},"dd/mm/YYYY":{regex:/^([0-9]{1,2})[\-\/\.]([0-9]{1,2})[\-\/\.]([0-9]{4})$/,parser:function(a){return Date.UTC(+a[3],a[2]-1,+a[1])},alternative:"mm/dd/YYYY"},
"mm/dd/YYYY":{regex:/^([0-9]{1,2})[\-\/\.]([0-9]{1,2})[\-\/\.]([0-9]{4})$/,parser:function(a){return Date.UTC(+a[3],a[1]-1,+a[2])}},"dd/mm/YY":{regex:/^([0-9]{1,2})[\-\/\.]([0-9]{1,2})[\-\/\.]([0-9]{2})$/,parser:function(a){var b=+a[3],b=b>(new Date).getFullYear()-2E3?b+1900:b+2E3;return Date.UTC(b,a[2]-1,+a[1])},alternative:"mm/dd/YY"},"mm/dd/YY":{regex:/^([0-9]{1,2})[\-\/\.]([0-9]{1,2})[\-\/\.]([0-9]{2})$/,parser:function(a){return Date.UTC(+a[3]+2E3,a[1]-1,+a[2])}}},parseDate:function(a){var b=
this.options.parseDate,d,f,e=this.options.dateFormat||this.dateFormat,c;if(b)d=b(a);else if("string"===typeof a){if(e)(b=this.dateFormats[e])||(b=this.dateFormats["YYYY/mm/dd"]),(c=a.match(b.regex))&&(d=b.parser(c));else for(f in this.dateFormats)if(b=this.dateFormats[f],c=a.match(b.regex)){this.dateFormat=f;this.alternativeFormat=b.alternative;d=b.parser(c);break}c||(c=Date.parse(a),"object"===typeof c&&null!==c&&c.getTime?d=c.getTime()-6E4*c.getTimezoneOffset():A(c)&&(d=c-6E4*(new Date(c)).getTimezoneOffset()))}return d},
rowsToColumns:function(a){var b,d,f,e,c;if(a)for(c=[],d=a.length,b=0;b<d;b++)for(e=a[b].length,f=0;f<e;f++)c[f]||(c[f]=[]),c[f][b]=a[b][f];return c},parsed:function(){if(this.options.parsed)return this.options.parsed.call(this,this.columns)},getFreeIndexes:function(a,b){var d,f=[],e=[],c;for(d=0;d<a;d+=1)f.push(!0);for(a=0;a<b.length;a+=1)for(c=b[a].getReferencedColumnIndexes(),d=0;d<c.length;d+=1)f[c[d]]=!1;for(d=0;d<f.length;d+=1)f[d]&&e.push(d);return e},complete:function(){var a=this.columns,
b,d=this.options,f,e,c,h,m=[],g;if(d.complete||d.afterComplete){for(c=0;c<a.length;c++)this.firstRowAsNames&&(a[c].name=a[c].shift());f=[];e=this.getFreeIndexes(a.length,this.valueCount.seriesBuilders);for(c=0;c<this.valueCount.seriesBuilders.length;c++)g=this.valueCount.seriesBuilders[c],g.populateColumns(e)&&m.push(g);for(;0<e.length;){g=new v;g.addColumnReader(0,"x");c=z(0,e);-1!==c&&e.splice(c,1);for(c=0;c<this.valueCount.global;c++)g.addColumnReader(void 0,this.valueCount.globalPointArrayMap[c]);
g.populateColumns(e)&&m.push(g)}0<m.length&&0<m[0].readers.length&&(g=a[m[0].readers[0].columnIndex],void 0!==g&&(g.isDatetime?b="datetime":g.isNumeric||(b="category")));if("category"===b)for(c=0;c<m.length;c++)for(g=m[c],e=0;e<g.readers.length;e++)"x"===g.readers[e].configName&&(g.readers[e].configName="name");for(c=0;c<m.length;c++){g=m[c];e=[];for(h=0;h<a[0].length;h++)e[h]=g.read(a,h);f[c]={data:e};g.name&&(f[c].name=g.name);"category"===b&&(f[c].turboThreshold=0)}a={series:f};b&&(a.xAxis={type:b},
"category"===b&&(a.xAxis.uniqueNames=!1));d.complete&&d.complete(a);d.afterComplete&&d.afterComplete(a)}},update:function(a,b){var d=this.chart;a&&(a.afterComplete=function(a){d.update(a,b)},n.data(a))}});n.Data=x;n.data=function(a,b){return new x(a,b)};n.wrap(n.Chart.prototype,"init",function(a,b,d){var f=this;b&&b.data?(f.data=new x(n.extend(b.data,{afterComplete:function(e){var c,h;if(b.hasOwnProperty("series"))if("object"===typeof b.series)for(c=Math.max(b.series.length,e.series.length);c--;)h=
b.series[c]||{},b.series[c]=n.merge(h,e.series[c]);else delete b.series;b=n.merge(e,b);a.call(f,b,d)}}),b),f.data.chart=f):a.call(f,b,d)});v=function(){this.readers=[];this.pointIsArray=!0};v.prototype.populateColumns=function(a){var b=!0;t(this.readers,function(b){void 0===b.columnIndex&&(b.columnIndex=a.shift())});t(this.readers,function(a){void 0===a.columnIndex&&(b=!1)});return b};v.prototype.read=function(a,b){var d=this.pointIsArray,f=d?[]:{},e;t(this.readers,function(c){var e=a[c.columnIndex][b];
d?f.push(e):f[c.configName]=e});void 0===this.name&&2<=this.readers.length&&(e=this.getReferencedColumnIndexes(),2<=e.length&&(e.shift(),e.sort(),this.name=a[e.shift()].name));return f};v.prototype.addColumnReader=function(a,b){this.readers.push({columnIndex:a,configName:b});"x"!==b&&"y"!==b&&void 0!==b&&(this.pointIsArray=!1)};v.prototype.getReferencedColumnIndexes=function(){var a,b=[],d;for(a=0;a<this.readers.length;a+=1)d=this.readers[a],void 0!==d.columnIndex&&b.push(d.columnIndex);return b};
v.prototype.hasReader=function(a){var b,d;for(b=0;b<this.readers.length;b+=1)if(d=this.readers[b],d.configName===a)return!0}})(w)});
