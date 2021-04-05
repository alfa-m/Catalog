
# MARKDOWN

------------------------------------

### TABLE OF CONTENT

+ [REFERENCE](#reference)
+ [HEADERS](#headers)
+ [LISTS & PARAGRAPHS](#lists-&-paragraphs)
+ [CODE](#code)
+ [LINKS](#links)
+ [EMPHASIS](#emphasis)
+ [BLOCK-QUOTES](#block-quotes)
+ [TABLES](#tables)

<!-- --><br/>



------------------------------------

### REFERENCE

- [Website][web]


- [Markdown Guide][guide]
	- [Basic Syntax][g-basic]


- [Cheatsheet][cheat]


[web]:https://daringfireball.net/projects/markdown/ "Daring Fireball: Markdown"
[guide]:https://www.markdownguide.org/ "Markdown Guide"
[g-basic]:https://www.markdownguide.org/basic-syntax/ "Basic Syntax"
[cheat]:https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet "Markdown Cheatsheet"
<!-- --><br/>



Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>



------------------------------------

### HEADERS

- Make Headers.  
  Up to 6 different levels are possible:

```markdown
# Header level 1
```
```markdown
## Header level 2
```
```markdown
### Header level 3
```
```markdown
#### Header level 4
```
```markdown
##### Header level 5
```
```markdown
###### Header level 6
```
<!-- --><br/>



Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>


------------------------------------

### LISTS & PARAGRAPHS

> :warning: **WARNING :**
>
> > In these examples, leading (at the begining) and trailing (at the end) SPACES are shown with dots (`.`).
> > Those dots should NOT be included.
> > When writing Markdown, use spaces instead.
>
> <!-- --><br/>


- To add a end of line, use ´line break´ from ´html´:

```markdown
<br/>
```

```markdown
<!-- --><br/>
```
<!-- --><br/>


- By default, when there is a line break a new paragraph starts.  
  A blank line is needed between paragraphs.  
  To force a line break (without blank line) use two trailing SPACES:

```
text..
```
<!-- --><br/>


- Ordered List and sub-List (the actual numbers don´t matter, they´re automatic):

```
1. text
2. text
3. text
..1. text
..2. text
..3. text
```
<!-- --><br/>


- Unordered List and sub-List:

```
* text
- text
+ text
..* text
..- text
..+ text
```
<!-- --><br/>


- Unless the paragraph is in a list, don’t indent paragraphs with spaces or tabs.  
  To add another paragraph in a list, insert a blank line after the list item,  
  or use two trailing SPACES to force a line break,  
  then indent the new paragraph with at least one leading SPACE:

```
- text..
.text
..text
...text
```
<!-- --><br/>



Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>



------------------------------------

### CODE

- To insert inline Code one or two backtick accents ( `` ` `` or ``` `` ```):

```markdown
text `code` text
```
```markdown
text ``code ` code`` text
```
<!-- --><br/>


- To insert a Block of Code use three (or more) backticks,  
  or three tilde accents (`~`),  
  or indent the lines with four leading SPACE or one tab:

~~~
```
code
```
~~~
~~~
````
code
````
~~~
```
~~~
code
~~~
```
```
    code
```
<!-- --><br/>


- To insert a Block of Code with syntax highlighting type the name of the language after the top three backticks:

~~~
```language
code
```
~~~
<!-- --><br/>



Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>



------------------------------------

### LINKS

- URL and URL in angle brackets will automatically get turned into links:

```markdown
https://url.com
```
```markdown
<url>
```
<!-- --><br/>


- Make a inline text link (without the angle brackets):

```markdown
[ text ](url)
```
```markdown
[ text ](path)
```
<!-- --><br/>


- Make a inline text link with Title (hover to see):

```markdown
[ text ](url "title")
[ text ](path "title")
```
<!-- --><br/>


- Define a Link Reference.  
  This definition won´t be rendered. The Reference will.
  The Reference can be used multiple times on the file.
  The definition of the URL can be defined before or after the Reference itself:

```markdown
[ reference ]:url
```
```markdown
[ reference ]:url "title"
```
```markdown
[ reference ]:path
```
```markdown
[ reference ]:path "title"
```
<!-- --><br/>


- Make a Reference:

```markdown
[ reference ]
```
```markdown
[ text ][ reference ]
```
<!-- --><br/>


- Make a link to a Header on the file.  
  The name of the Header must be right, but letter case don´t matter.  
  You can´t have spaces adjacent to the parentheses.  
  If the Header name has spaces you may use hyphens (`-`) instead.  
  If more then one Header have the same name, their link should be numbered:

```markdown
[ text ](#<name-of-the-header>)
[ text ](#<name-of-the-header>-1)
[ text ](#<name-of-the-header>-2)
```
<!-- --><br/>


- Generate a Table of Content from a Markdown file:  
  [Table of Content](https://ecotrust-canada.github.io/markdown-toc/ "Table of contents generated with markdown-toc")
<!-- --><br/>



Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>



------------------------------------

### EMPHASIS

- _Italic_ (a.k.a. Emphasis):

```
_text_
```
```
*text*
```
<!-- --><br/>


- **Bold** (a.k.a. Strong Emphasis):

```
**text**
```
```
__text__
```
<!-- --><br/>


- Combined (many combinations possible):

```
**text    _text_**
```
```
** *text* **
```
<!-- --><br/>


- ~~Scratch~~ (a.k.a. Strikethrough):

```
~~text~~
```
<!-- --><br/>



Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>


------------------------------------

### BLOCK-QUOTES

- Make a block-quote:

```
> text
```
```
> text
>
> text
```
<!-- --><br/>


- Make nested block-quote:

```
> text
>> text
>>> text
>>>> text
>
> text
```
<!-- --><br/>


- Make a Warning Message with Emoji:

```
> :warning: text
```
<!-- --><br/>


- Emoji Table:  
  [Emojis](https://gist.github.com/rxaviers/7360908)
<!-- --><br/>



Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>



------------------------------------

### TABLES

- Tables aren't part of the core Markdown spec, but they are part of GFM (Github Flavored Markdown):

```markdown
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
```
<!-- --><br/>



- Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>





------------------------------------



------------------------------------



------------------------------------



------------------------------------

### TOPIC

> :warning: **WARNING :**
>
>> Warning
>
<!-- --><br/>


- Command Explanation:

`command`

`alternative command`
<!-- --><br/>


- Command Explanation:

`command`
<!-- --><br/>



##### SUBTOPIC

- Command Explanation:

`command`
<!-- --><br/>



> ##### Examples
>
>> `code`
>
>
<!-- --><br/>



- Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>



------------------------------------



------------------------------------



------------------------------------



------------------------------------



------------------------------------



------------------------------------
