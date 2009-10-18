// This is a greasemonkey script which prints last.fm usernames (prepended with /user/)
// to the firebug console.
//
// It was written for the page http://www.last.fm/community/users/active
//
// Written Karl Pichotta, licensed under WTFPL: http://sam.zoy.org/wtfpl/


//method from http://www.dustindiaz.com/getelementsbyclass/
function getElementsByClass(searchClass,node,tag) {
    var classElements = new Array();
    if ( node == null ) node = document;
    if ( tag == null ) tag = '*';
    var els = node.getElementsByTagName(tag);
    var elsLen = els.length;
    var pattern = new RegExp("(^|\\s)"+searchClass+"(\\s|$)");
    for (i = 0, j = 0; i < elsLen; i++) {
	if ( pattern.test(els[i].className) ) {
	    classElements[j] = els[i];
	    j++;
	}
    }
    return classElements;
}

users = getElementsByClass('userContainer');
var re = new RegExp("/user/(([A-Za-z0-9]|-|_)*)");
for(var i = 0; i < users.length; i++) {
    var matches = re.exec(users[i].innerHTML);
    if(matches != null) console.log(matches[0]);
}
