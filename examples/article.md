# Level of Markdown support in Medium

![Headline Image](http://web.archive.org/web/0if_/http:/http://placekitten.com/1200/900)
**TODO**: *Still have question - how could I show it as headliner?*

according to https://blog.medium.com/accepted-markup-for-medium-s-publishing-api-a4367010924e
this https://daringfireball.net/projects/markdown/syntax should work

but ... the level of support Markdown here is medium :D.
So lets check all features one by one:


# HEADERS

# This is an H1

## This is an H2

### This is an H3 (DOESN'T WORK)

#### This is an H4 (DOESN'T WORK)

##### This is an H5 (DOESN'T WORK)

###### This is an H6 (DOESN'T WORK)

# BLOCKQUOTES

> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
>
> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
> id sem consectetuer libero luctus adipiscing.


> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
id sem consectetuer libero luctus adipiscing.

## (DOESN'T WORK)

> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.


> ## This is a header.
>
> 1.   This is the first list item.
> 2.   This is the second list item.
>
> Here's some example code:
>
>     return shell_exec("echo $input | $markdown_script");

# LISTS

*   Red
*   Green
*   Blue

+   Red
+   Green
+   Blue

-   Red
-   Green
-   Blue

1.  Bird
2.  McHale
3.  Parish

1.  Bird
1.  McHale
1.  Parish

3. Bird
1. McHale
8. Parish


*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
    viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
    Suspendisse id sem consectetuer libero luctus adipiscing.


*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
viverra nec, fringilla in, laoreet vitae, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
Suspendisse id sem consectetuer libero luctus adipiscing.


## (DOESN'T WORK)

1.  This is a list item with two paragraphs. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  Suspendisse id sem consectetuer libero luctus adipiscing.


*   This is a list item with two paragraphs.

    This is the second paragraph in the list item. You're
only required to indent the first line. Lorem ipsum dolor
sit amet, consectetuer adipiscing elit.

*   Another item in the same list.


*   A list item with a blockquote:

    > This is a blockquote
    > inside a list item.



*   A list item with a code block:

        <code goes here>

# List Hierarchy (DOESN'T WORK)

- A first level
    - A second level
    - B second level
- B first level
    - C second level
        - A third level
        - B third level


# CODE BLOCKS


This is a normal paragraph:

    This is a code block.


Here is an example of AppleScript:

    tell application "Foo"
        beep
    end tell


    <div class="footer">
        &copy; 2004 Foo Corporation
    </div>


# HORIZONTAL RULES

## 1

* * *

## 2

***

## 3

*****

## 4

- - -

## 5

---------------------------------------


# SPAN ELEMENTS

This is [an example](http://example.com/ "Title") inline link.

[This link](http://example.net/) has no title attribute.

This is [an example][id] reference-style link.

[id]: http://example.com/  "Optional Title Here"

## (DOESN'T WORK)
I get 10 times more traffic from [Google] [1] than from
[Yahoo] [2] or [MSN] [3].

  [1]: http://google.com/        "Google"
  [2]: http://search.yahoo.com/  "Yahoo Search"
  [3]: http://search.msn.com/    "MSN Search"


## WORK

I get 10 times more traffic from [Google][] than from
[Yahoo][] or [MSN][].

  [google]: http://google.com/        "Google"
  [yahoo]:  http://search.yahoo.com/  "Yahoo Search"
  [msn]:    http://search.msn.com/    "MSN Search"


# EMPHASIS

*single asterisks*

_single underscores_

**double asterisks**

__double underscores__


# CODE

Use the `printf()` function.

``There is a literal backtick (`) here.``

# IMAGES

![Alt text](http://web.archive.org/web/0if_/http://placekitten.com/200/300)

![Alt text](http://web.archive.org/web/0if_/http://placekitten.com/300/300 "Optional title")


# MISCELLANEOUS

<http://hyzhak.github.io/>

<address@example.com>

