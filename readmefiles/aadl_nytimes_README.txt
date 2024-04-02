# AADL NYTimes Bookmarklet

The [Ann Arbor District Library (AADL)](https://aadl.org/) offers free digital access to [the New York Times](https://www.nytimes.com/) for members. However, it can be a bit of a pain to access.

To make it easier, you can **add this link as a browser bookmark**: <a href="javascript:void(window.location.href = window.location.href.replace(/https:\/\/www.nytimes.com\//, 'https://www-nytimes-com.research.aadl.org/'));">📰 Access through AADL</a>. You can do this by:

- Select and drag the link into your bookmarks bar,
- right click the link and use the option to add a bookmark, or
- find an option to add a bookmarklet manually, copy the code from the link above, and paste it as the URL.

![An animation of a user dragging a bookmark to the bookmark bar](add_bookmarklet.gif)

Then, any time you are on a New York Times page (including one that is restricted), you can click the bookmark link to access it.

![An animation of a user clicking the bookmark while on a New York Times page](using_extension.gif)


## How does it work?

When you click the link, a short JavaScript snippet gets run to navigate to access that page through the AADL. The code runs the code at the end of the page, (which simply replaces the "www.nytimes.com" domain with "www-nytimes-com.research.aadl.org"). More specifically, clicking the link runs the following code:
```javascript
window.location.href = window.location.href.replace(/https:\/\/www.nytimes.com\//, "https://www-nytimes-com.research.aadl.org/");
```

## Credit

The explanation of how to add the bookmarklet is taken from a page describing [another (very useful) bookmarklet from Michigan Libraries](https://www.lib.umich.edu/find-borrow-request/access-online-resources/remote-access/using-browser-bookmark).
