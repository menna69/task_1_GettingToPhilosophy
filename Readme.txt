Task 1 Getting to Philosophy,
importing the necessary libraries for the task. time to add sleep period so as to avoid heavy load on wikipedia, urllib to deal with urls, bs4 for extracting text from html files using BeautifulSoup.
add the starting link and the target link we want to end up at.
define a function get_first_link to find the first link in a web page and hold it.
define a crawling_func to stop when target url is reached, end if too many searches took place without getting to the target url, we assigned maximum search of 25, avoid entering loops by ending the search if a url is repeated.
create an array to hold all visited links till we reach the required philosophy link.
in case a web page contains no urls a message is sent to user and search ends.
  