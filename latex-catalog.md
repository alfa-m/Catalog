
# LaTeX

This is a guide for ![][latex] commands.
<!-- --><br/>

> **Notes:**
>
>> You can start at [Basics](#basics).
>>

<!-- --><br/>


------------------------------------

### TABLE OF CONTENT

+ [TERMINOLOGY](#terminology)
+ [PACKAGES](#packages)
+ [REFERENCES](#references)
+ [BASICS](#basics)
+ [USE PACKAGES](#use-packages)
+ [CONFIGURATIONS](#configurations)
	* [NUMBERING](#numbering)
	* [HYPHENATION](#hyphenation)
+ [ALL CLASSES](#all-classes)
	* [SECTIONING](#sectioning)
	* [PARAGRAPH INDENTATION](#paragraph-indentation)
+ [TITLE & TABLE OF CONTENTS](#title--table-of-contents)
+ [LISTS](#lists)
+ [SYMBOLS](#symbols)
+ [BASIC FORMATING](#basic-formating)
	* [FONTS](#fonts)
	* [ALIGN](#align)
+ [MATH](#math)
	* [EQUATIONS DELIMITERS](#equations-delimiters)
	* [TEXT WITHIN EQUATIONS](#text-within-equations)
	* [SUB/SUPERSCRIP & FRACTIONS](#subsuperscrip--fractions)
	* [CALCULUS](#calculus)
	* [HATS AND ACCENTS](#hats-and-accents)
	* [MULTIPLE EQUATIONS](#multiple-equations)
	* [CASES { DEFINITION](#cases--definition)
	* [CROSSED REFERENCE](#crossed-reference)
	* [MATH FONTS](#math-fonts)
	* [OPERATORS](#operators)
	* [SYMBOLS](#symbols-1)
+ [LINKS](#links)
+ [ARTICLE CLASS](#article-class)
+ [BOOK CLASS](#book-class)
+ [HOMEWORK CLASS](#homework-class)
	* [QUESTIONS](#questions)
	* [QUESTION COUNTER](#question-counter)
<!-- --><br/>



------------------------------------

### TERMINOLOGY


| Term/Expression | Meaning |
| --------------: | :------ |
| `<description>` | To replace, or that will be replaced, according to description. |
| `...`           | Possible to repeated pattern. |
| `$`             | Some command to be used on the Terminal (shell). |
<!-- --><br/>
<!-- --><br/>



- Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>



------------------------------------

### PACKAGES

The packages **I** use.

| Source |    Package   | Description |
| :----: | -----------: | ----------- |
| pacman | texlive-most | (package group) |
| pacman |         kile | A user friendly TeX/LaTeX frontend for KDE. |
| online | [Overleaf][overleaf] | An online LaTeX editor that's easy to use.<br/>No installation, real-time collaboration, version control, hundreds of LaTeX templates, and more. |
<!-- --><br/>
<!-- --><br/>



- Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>


----------------------------------

### REFERENCES

- [LaTeX Wiki][wiki]

  - [LaTeX Mathematics Wiki][math]

<!-- --><br/>

- [Overleaf][overleaf]

  - [Overleaf Documentation][leaf-doc]
  
  - [Learn LaTeX in 30 minutes][30min]
  
  - [A quick guide to LaTeX][quick]
  
  - [Overleaf Templates][templates]
  
  - [Complete list of Math Symbols][math-symb]
  
  - [Hyperlinks][hyperlinks]

<!-- --><br/>

- [ABNTEX2][abnt2]

  - [Por onde começar?][onde]

- [A Cool Slide][cool]


- I should learn how to use [this][kbibtex]
<!-- --><br/>
<!-- --><br/>



- Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>


[wiki]:https://en.wikibooks.org/wiki/LaTeX "LaTeX Wiki"
[math]:https://en.wikibooks.org/wiki/LaTeX/Mathematics

[overleaf]:https://www.overleaf.com/ "Overleaf"
[leaf-doc]:https://www.overleaf.com/learn
[30min]:https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes
[quick]:https://www.overleaf.com/latex/templates/a-quick-guide-to-latex/fghqpfgnxggz
[templates]:https://www.overleaf.com/latex/templates
[math-symb]:https://www.overleaf.com/learn/latex/List_of_Greek_letters_and_math_symbols
[hyperlinks]:https://pt.overleaf.com/learn/latex/Hyperlinks


[abnt2]:https://www.abntex.net.br/
[onde]:https://github.com/abntex/abntex2/wiki/PorOndeComecar
[cool]:https://pt.slideshare.net/smarzaro/latex-bsico-i " LaTeX Básico I "
[kbibtex]:https://apps.kde.org/en/kbibtex "KBibTeX"

[latex]:https://latex.codecogs.com/gif.latex?\text{\LaTeX}

------------------------------------

### BASICS

To make comments use `%`.

| Tool      | Shortcut         | Action |
| :-------- | :--------------: | ------ |
| Kile      | [`CTRL`] + [`/`] | Comment current or selected lines. |
| TexStudio | [`CTRL`] + [`T`] | Comment current or selected lines. |
<!-- --><br/>
<!-- --><br/>


A ![][latex] file starts by defining the Class of document.
Different Classes of Documents have different commands and properties.
<!-- --><br/>

- Define Class of the Document:
```latex
\documentclass[<option>, ..., <option>]{<class>}
```
<!-- --><br/>

- Classes:
  - [Article](#article-class)
  - [Book](#book-class)
  - Report
  - Letter
  - ...

- _Some_ Options:
| Options          | Description |
| :--------------: | :---------- |
| `<number>p`      | Font size (default= 10). |
| `onecolumn`      | One column each page (default). |
| `twocolumn`      | Two column each page. |
| `oneside`        | On printing uses only one side of the page.<br/>Default for ´article´ and ´report´. |
| `twoside`      | On printing uses the two sides of the page.<br/>Default for ´book´. |
| `titlepage`      | Has a page for the Title.<br/>Default for ´book´ and ´report´. |
| `notitlepage`    | Doesn´t has a page for the Title.<br/>Default for ´article´. |
| `openright`      | A new Chapter starts on a new right-page.<br/>Default for ´book´. |
| `openany`        | A new Chapter starts on any new page.<br/>Default for ´report´. |
| `letterpaper`    | Type of paper. (default) |
| `a4paper`        | Type of paper. |
| `a5paper`        | Type of paper. |
| `b5paper`        | Type of paper. |
| `executivepaper` | Type of paper. |
<!-- --><br/>


After the Class of the Document has been defined, some [packages](#use-packages) can be imported and some [configurations](configurations) set.

After that, it can start the Document.
To do that, use the ´document´ _environment_.

- Begin and End Document:
  Inside this environment the all the document content is typed.
  Many commands are also available.
  Some commands are for all Classes of Documents, some are exclusive to some Classes.

```latex
\begin{document}

    <content>

\end{document}
```
<!-- --><br/>
<!-- --><br/>



- From now on, the commands listed on the following sections (with exception of [Use Packages](#use-packages) and [Configurations](#configurations)) are meant to be used inside the ´document´ environment.



<!-- --><br/>
<!-- --><br/>



- Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>



------------------------------------

### USE PACKAGES


- Use a package:

```latex
\usepackage[<options>]{<package>}
```
<!-- --><br/>


- Some useful packages:
  - Change language of _automatic text_ to pt-br (eg. chapters, sections):
  ```latex
  \usepackage[brazil]{babel}
  ```
  - Proper read of accentuation and cedilla on the input file:
  ```latex
  \usepackage[utf8]{inputenc}
  ```
    OR if using a encoding other than utf-8:
  ```latex
  \usepackage[latin1]{inputenc}
  ```
  - Proper mapping of accentuation and cedilla to the output document:
  ```latex
  \usepackage[T1]{fontenc}
  ```
  - Use the Latin Moder font:
  ```latex
  \usepackage{lmodern}
  ```
<!-- --><br/>
<!-- --><br/>



- Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>



------------------------------------

### CONFIGURATIONS
<!-- --><br/>

Commands have main parameters in braces ´{ }´ and optional parameters in brackets ´[ ]´.
<!-- --><br/>


- Input a Tex file (only processes the file):

```latex
\input{<tex-file>}
```
<!-- --><br/>


- Include a Tex file (generates file´s pages):

```latex
\include{<tex-file>}
```
<!-- --><br/>
<!-- --><br/>



##### NUMBERING


- To suppress page numbering:

```latex
\pagenumbering{gobble}
```
<!-- --><br/>


- To switch on page numbering with Arabic Numbers:

```latex
\pagenumbering{arabic}
```
<!-- --><br/>


- To switch on page numbering with Roman Numbers:

```latex
\pagenumbering{roman}
```
```latex
\pagenumbering{Roman}
```
<!-- --><br/>


- To switch on page numbering with Letters:

```latex
\pagenumbering{alph}
```
```latex
\pagenumbering{Alph}
```
<!-- --><br/>


- Set till which depth of sections are numbered:

```latex
\setcounter{secnumdepth}{<depth>}
```
- Set till which depth of sections are included on the Table of Contents:

```latex
\setcounter{tocdepth}{<depth>}
```
| depth | description |
| :---: | ----------- |
| 0     | Numbering until Chapter |
| 1     | Numbering until Section |
| 2     | Numbering until Subsection (default) |
| 3     | Numbering until Subsubsection |
| 4     | Numbering until Paragraph |
| 5     | Numbering until Subparagraph |
<!-- --><br/>





##### HYPHENATION

- Teach LaTeX how to hyphenate a word or to never hyphenate it:

```latex
\hyphenation{ hy-phe-na-te }
```
```latex
\hyphenation{ neverHyphenate }
```
```latex
\hyphenation{ hy-phe-na-te neverHyphenate }
```
<!-- --><br/>
<!-- --><br/>



- Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>



------------------------------------

### ALL CLASSES

These are commands available on any Class.
<!-- --><br/>

##### SECTIONING

LaTeX numbers Sections, Subsections, Chapters, Parts, etc, automatically.
<!-- --><br/>


- Create new Section, Subsections and Subsubsections:

```latex
\section{<title>}
```
```latex
\subsection{<title>}
```
```latex
\subsubsection{<title>}
```
<!-- --><br/>


- Create unnumbered Sections:

```latex
\section*{<title>}
```
```latex
\subsection*{<title>}
```
```latex
\subsubsection*{<title>}
```
<!-- --><br/>


- Create titled Paragraphs and Subparagraphs:

```latex
\paragraph{<title>}
```
```latex
\subparagraph{<title>}
```
<!-- --><br/>



##### PARAGRAPH INDENTATION

For LaTeX to identify paragraphs, it is needed an empty line between then.
<!-- --><br/>


- Make the next paragraph to NOT be indented:

```latex
\noindent
```
<!-- --><br/>


- Or just give a ´new line´ at the end of the previous paragraph.
  It is wrong to have a _blank line_ after ´new line´.

```latex
\\
```
```latex
\newline
```
<!-- --><br/>


- To indent the very first line after a new Section use the package:

```latex
\usepackage{indentfirst}
```
<!-- --><br/>


- To get the text to a new page:

```latex
\newpage
```
<!-- --><br/>
<!-- --><br/>



- Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>




------------------------------------

### TITLE & TABLE OF CONTENTS

- Define Author:

```latex
\author{<name>}
```
<!-- --><br/>


- Define Title of the Document:

```latex
\title{<title>}
```
<!-- --><br/>


- Define the Date:

```latex
\date{<text>}
```
```latex
\date{\today}
```
```latex
\date{}
```
<!-- --><br/>


- Generate Title:

```latex
\maketitle
```
<!-- --><br/>


- Generate Table of Contents:

```latex
\tableofcontents
```
<!-- --><br/>
<!-- --><br/>



- Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>



------------------------------------

### LISTS

- To create a unordered List use the ´itemize´ environment and put the ´item´s inside:

```latex
\begin{itemize}
    \item <text>
    \item <text>
    ...
\end{itemize}
```
<!-- --><br/>


- To create an ordered List use the ´enumerate´ environment and put the ´item´s inside:

```latex
\begin{enumerate}
    \item <text>
    \item <text>
    ...
\end{enumerate}
```
<!-- --><br/>



- Nested Lists.  
  You can insert a list inside another list.  
  Including mixed types.

```latex
\begin{enumerate}
    \item <text>
    \item <text>
    
    \begin{enumerate}
        \item <text>
        \item <text>
        ...
    \end{enumerate}
    ...
\end{enumerate}
```
<!-- --><br/>
<!-- --><br/>



- Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>



------------------------------------

### SYMBOLS


- Reserverd Symbols:

```latex
$, &, #, _, {, }, %
```
<!-- --><br/>

- To include reserverd symbols on the text they need to be preceded by the escape character ´\´:

```latex
\$, \&, \#, \_, \{, \}, \%
```
<!-- --><br/>
<!-- --><br/>



- To open quotes use backtick accents ``` ` ```  or ``` `` ```.  
  To close quotes use apostrophe `'` or `''`.
<!-- --><br/>
<!-- --><br/>



- Type of dashes:

|  Code  | Rendered Symbol Description  |
| :----: | :-------------- |
| `-`    | Hyphen |
| `--`   | Simple dash |
| `---`  | Indent |
<!-- --><br/>
<!-- --><br/>



- Ellipsis ´...´:

```latex
\dots
```
<!-- --><br/>


- Write today´s date:

```latex
\today
```
<!-- --><br/>


- Write this ![][latex] stylized thingy:

```latex
\LaTeX
```
<!-- --><br/>
<!-- --><br/>



- Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>





------------------------------------

### BASIC FORMATING


- Bold:

```latex
\textbf{<text>}
```
<!-- --><br/>

| Tool      | Shortcut for **Bold** |
| :-------: | :-------------------: |
| Kile      | [`ALT`] + [`SHIFT`] + [`B`] |
| TexStudio | [`CTRL`] + [`B`] |
<!-- --><br/>


- Italic (_Emphasis_):

```latex
\textit{<text>}
```
```latex
\emph{<text>}
```
<!-- --><br/>

| Tool      | Shortcut for _Italic_ |
| :-------: | :-------------------: |
| Kile      | [`ALT`] + [`SHIFT`] + [`I`] |
| TexStudio | [`CTRL`] + [`I`] |
<!-- --><br/>


- Underline:

```latex
\undeline{<text>}
```
<!-- --><br/>
<!-- --><br/>



##### FONTS

- Some Fonts:
  - Romman Font:
  ```latex
  \textrm{<text>}
  ```
  - Type Writer (good for code):
  ```latex
  \texttt{<text>}
  ```
  - Sans Serif:
  ```latex
  \textsf{<text>}
  ```
  - Small Caps:
  ```latex
  \textsc{<text>}
  ```
<!-- --><br/>


- Font sizes:

```latex
\tiny{<text>}
```
```latex
\scriptsize{<text>}
```
```latex
\footnotesize{<text>}
```
```latex
\small{<text>}
```
```latex
\normalize{<text>}
```
```latex
\large{<text>}
```
```latex
\Large{<text>}
```
```latex
\LARGE{<text>}
```
```latex
\huge{<text>}
```
```latex
\Huge{<text>}
```
<!-- --><br/>
<!-- --><br/>



##### ALIGN

- Align left (default):

```latex
\begin{flushleft}
    <text>
\end{flushleft}
```
<!-- --><br/>


- Centralize:

```latex
\begin{center}
    <text>
\end{center}
```
<!-- --><br/>


- Align right:

```latex
\begin{flushright}
    <text>
\end{flushright}
```
<!-- --><br/>
<!-- --><br/>



- Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>



------------------------------------

### MATH

- [LaTeX Mathematics Wiki][math]


- Many commands in this section use the package ´amsmath´ and, for the fonts section, ´amssymb´:

```latex
\usepackage{amsmath}
\usepackage{amssymb}
```
<!-- --><br/>
<!-- --><br/>



##### EQUATIONS DELIMITERS

- The way Equations are displayed depends on the delimiters.  
  Delimiters are not rendered.  
  Also, most commands in this section are specific for within Equations.  
  You **CANNOT** use empty lines within Equations.  
  Use only one Equation per environment.

  - In-line Equations:
  ```latex
  $  <equation>  $
  ```
  ```latex
  \(  <equation>  \)
  ```
  ```latex
  \begin{math}  <equation>  \end{math}
  ```

  - Displayed Numbered Equations:
  ```latex
  \begin{equation}
      <equation>
  \end{equation}
  ```
  ```latex
  $$  <equation>  $$
  ```
  ```latex
  \[  <equation>  \]
  ```
  ```latex
  \begin{displaymath}
      <equation>
  \end{displaymath}
  ```

  - Displayed unumbered Equations:
  ```latex
  \begin{equation*}
      <equation>
  \end{equation*}
  ```
<!-- --><br/>


- Parentheses and brackets on Equations can be directly typed.  
  Pipes ´| |´ can also be typed directly.  
  Double pipes ´||   ||´ and Braces ´{ }´ need to be escaped.  
  Fot angle brackets ´⟨ ⟩´ use the command ´langle´.

| Code                 | Rendered Symbol |
| :------------------: | :---: |
| `(    )`             | (    )  |
| `[    ]`             | [    ]  |
| `|    |`             | \|    \|  |
| `\|    \| `          | \|\|   \|\|  |
| `\{    \}`           | {    }  |
| `\langle    \langle` | ⟨    ⟩  |
<!-- --><br/>


- To add parentheses and brackets resized dynamically use:

```latex
\left(    \right)
```
```latex
\left[    \right]
```
<!-- --><br/>


- To add parentheses and brackets resized dynamically look [here](https://www.overleaf.com/learn/latex/Brackets_and_Parentheses#Reference_guide) ~~cause I´m lazy~~.
<!-- --><br/>
<!-- --><br/>



##### TEXT WITHIN EQUATIONS

- To add a text inside a equation:

```latex
\text{ <text> }
```
```latex
\textrm{ <text> }
```
```latex
\texttt{ <text> }
```
```latex
\textit{ <text> }
```
```latex
\textbf{ <text> }
```
<!-- --><br/>


- To add space inside a Equation (ascending order):

| Code     | Rendered Symbol Description |
| :------: | :--- |
| `\!`     | Less than the default. |
| `\,`     ||
| `\:`     ||
| `\;`     ||
| `\ `     | Equal to space in normal text.<br/>(space after the backslash!) |
| `\quad`  | Equal the space of the current font size. |
| `\qquad` | Twice of `\quad`. |
<!-- --><br/>
<!-- --><br/>



##### SUB/SUPERSCRIP & FRACTIONS

- To write SubScript:

```latex
<base>_<subscript>
```
```latex
<base>_{ <subscript> }
```
<!-- --><br/>

- To write SuperScrip (eg. exponents):

```latex
<base>^<superscrip>
```
```latex
<base>^{ <superscrip> }
```
<!-- --><br/>

- To write SubScript and SuperScrip:

```latex
<base>_{ <subscript> }^{ <superscrip> }
```
<!-- --><br/>


- To write fractions:

```latex
\frac{ <numerator> }{ <denominator> }
```
```latex
\tfrac{ <numerator> }{ <denominator> }
```
```latex
^<numerator>/_<denominator>
```
<!-- --><br/>
<!-- --><br/>



##### CALCULUS

- To write a Integral:

```latex
\int_{ <lower> }^{ <upper> }  <equation>  \,dx
```
<!-- --><br/>


- To write double/triple Integrals:

```latex
\int_{ <lower> }  <equation>  \,du
```
```latex
\iint_{ <lower> }  <equation>  \,du\,dv
```
```latex
\iiint_{ <lower> }  <equation>  \,du\,dv\,dw
```
<!-- --><br/>


- To write close line/surface Integrals:

```latex
\oint_{ <lower> }  <equation>  \,ds
```
```latex
\oiint_{ <lower> }  <equation>  \,ds
```
<!-- --><br/>


- To write Sums and Products:

```latex
\sum_{ <lower> }^{ <upper> }  <equation>
```
```latex
\prod_{ <lower> }^{ <upper> }  <equation>
```
<!-- --><br/>


- To write Limits:

```latex
\lim_{ <variable> \to <value> }  <equation>
```
<!-- --><br/>
<!-- --><br/>



##### HATS AND ACCENTS

- To add a hat to a letter **in text-mode**:

```latex
\^{ <letter> }
```
<!-- --><br/>


- To add a hat to a letter **in math-mode** (equation):

| Code                   | Rendered Symbol |
| :--------------------: | :-------------: |
| `\hat{x}`              | ![](https://latex.codecogs.com/gif.latex?\hat{x}) |
| `\widehat{xxx}`        | ![](https://latex.codecogs.com/gif.latex?\widehat{xxx}) |
| `\vec{x}`              | ![](https://latex.codecogs.com/gif.latex?\vec{x}) |
| `\overrightarrow{xxx}` | ![](https://latex.codecogs.com/gif.latex?\overrightarrow{xxx}) |
| `\dot{x}`              | ![](https://latex.codecogs.com/gif.latex?\dot{x}) |
| `\ddot{x}`             | ![](https://latex.codecogs.com/gif.latex?\ddot{x}) |
| `\acute{x}`            | ![](https://latex.codecogs.com/gif.latex?\acute{x}) |
| `\grave{x}`            | ![](https://latex.codecogs.com/gif.latex?\grave{x}) |
| `\bar{x}`              | ![](https://latex.codecogs.com/gif.latex?\bar{x}) |
| `\tilde{x}`            | ![](https://latex.codecogs.com/gif.latex?\tilde{x}) |
| `\check{x}`            | ![](https://latex.codecogs.com/gif.latex?\check{x}) |
| `\breve{x}`            | ![](https://latex.codecogs.com/gif.latex?\breve{x}) |
<!-- --><br/>


- To write a vector with SuperScrip (that doesn´t look crap):

```latex
\vec{ <letter> }^{ \, <superscrip> }
```
<!-- --><br/>
<!-- --><br/>



##### MULTIPLE EQUATIONS

- To align parts of different Equations use the package ´amsmath´:

```latex
\usepackage{amsmath}
```
<!-- --><br/>


- To display consecutive Equations, centered, use the ´gather´ environment.  
  The double backslash `\\` works as a newline character.

```latex
\begin{gather}
    <equation> \\
    <equation> \\
    ...
\end{gather}
```
```latex
\begin{gather*}
    <equation> \\
    <equation> \\
    ...
\end{gather*}
```
<!-- --><br/>


- To align a certain point of the Equations use the ´align´ environment.  
  Use the ampersand `&`, to set the vertical align points.

```latex
\begin{align}
    <pieces> & = <pieces> \\
    <pieces> & = <pieces> \\
    ...
\end{align}
```
```latex
\begin{align*}
    <pieces> & = <pieces> \\
    <pieces> & = <pieces> \\
    ...
\end{align*}
```
```latex
    \begin{align}
    <pieces> & = <pieces>      &  <pieces> & = <pieces> \\
    <pieces> & = <pieces>      &  <pieces> & = <pieces> \\
    ...
\end{align}
```
<!-- --><br/>


- To split a single Equations into smaller pieces, that will be aligned use the ´multline´ environment:

```latex
\begin{multline}
    <pieces> = & <pieces> \\
    & <pieces> \\
    & <pieces> \\
    ...
\end{multline}
```
```latex
\begin{multline*}
    <pieces> = & <pieces> \\
    & <pieces> \\
    & <pieces> \\
    ...
\end{multline*}
```
<!-- --><br/>


- To split a single Equations, within the ´equation´ environment, use the ´split´ environment:

```latex
\begin{equation}
    \begin{split}
        <pieces> = & <pieces> \\
        & <pieces> \\
        & <pieces> \\
        ...
    \end{split}
\end{equation}
```
<!-- --><br/>
<!-- --><br/>



##### CASES { DEFINITION

```latex
\begin{equation}
    <pieces> = 
    \begin{cases}
        <pieces>,    & <condition> \\
        <pieces>,    & <condition> \\
        <pieces>,    & <condition> \\
        ...
    \end{cases}
\end{equation}
```
<!-- --><br/>
<!-- --><br/>



##### CROSSED REFERENCE

- Create a Label that can be referenced.  
  Place it inside Displayed Numbered Equations.

```latex
\begin{equation} \label{ <label> }
    <equation>
\end{equation}
```
<!-- --><br/>


- Reference the Section number:

```latex
\ref{ <label> }
```
<!-- --><br/>
<!-- --><br/>



##### MATH FONTS

- Package ´amssymb´ or ´amsfonts´:

```latex
\usepackage{amssymb}
\usepackage{amsfonts}
```
<!-- --><br/>


- To make Mathematical **Symbols Bold**:

```latex
\pmb{ <math> }
```
```latex
\boldsymbol{ <math> }
```
<!-- --><br/>


- Capital letters-only font typefaces:
  - Calligraphic (curly):
  ```latex
  \mathcal{ <letters> }
  ```
  - Fraktur (MORE curly):
  ```latex
  \mathfrak{ <letters> }
  ```
  - Blackboard bold (those letters for sets):
  ```latex
  \mathbb{ <letters> }
  ```
<!-- --><br/>
<!-- --><br/>



##### OPERATORS

|        |        |         |           |        |        |
| :----: | :----: | :-----: | :-------: | :----: | :----: |
| `\exp` | `\sin` | `\sinh` | `\arcsin` | `\sec` | `\min` |
| `\ln`  | `\cos` | `\cosh` | `\arccos` | `\csc` | `\max` |
| `\log` | `\tan` | `\tanh` | `\arctan` | `\cot` | `    ` |
<!-- --><br/>
<!-- --><br/>



##### SYMBOLS

- List of Greek Letters:

|     Code      | Symbol |      |   Code    | Symbol |      |    Code    | Symbol |
| :-----------: | :----: | ---- | :-------: | :----: | ---- | :--------: | :----: |
|   `\alpha`    |   α    |      | `\kappa`  |   κ    |      |   `\tau`   |   τ    |
|    `\beta`    |   β    |      | `\lambda` |   λ    |      | `\upsilon` |   υ    |
|   `\gamma`    |   γ    |      | `\Lambda` |   Λ    |      | `\Upsilon` |   ϒ    |
|   `\Gamma`    |   Γ    |      |   `\mu`   |   μ    |      |   `\phi`   |   ϕ    |
|   `\delta`    |   δ    |      |   `\nu`   |   ν    |      | `\varphi`  |   φ    |
|   `\Delta`    |   Δ    |      |   `\xi`   |   ξ    |      |   `\Phi`   |   Φ    |
|  `\epsilon`   |   ϵ    |      |   `\Xi`   |   Ξ    |      |   `\chi`   |   χ    |
| `\varepsilon` |   ε    |      |   `\pi`   |   π    |      |   `\psi`   |   ψ    |
|    `\zeta`    |   ζ    |      |   `\Pi`   |   Π    |      |   `\Psi`   |   Ψ    |
|    `\eta`     |   η    |      |  `\rho`   |   ρ    |      |  `\omega`  |   ω    |
|   `\theta`    |   θ    |      | `\sigma`  |   σ    |      |  `\Omega`  |   Ω    |
|   `\Theta`    |   Θ    |      | `\Sigma`  |   Σ    |      |    `  `    |        |
|    `\iota`    |   ι    |      |   `  `    |        |      |    `  `    |        |
<!-- --><br/>
<!-- --><br/>



- List of Common Symbols:

|   Code    | Symbol |      |    Code    | Symbol |      |     Code     | Symbol |
| :-------: | :----: | ---- | :--------: | :----: | ---- | :----------: | :----: |
|   `\pm`   |   ±    |      | `\forall`  |   ∀    |      | `\therefore` |   ∴    |
| `\times`  |   x    |      |  `\infty`  |   ∞    |      |    `\neq`    |   ≠    |
|  `\div`   |   ÷    |      |   `\in`    |   ∈    |      |  `\approx`   |   ≈    |
|   `\%`    |   %    |      |  `\notin`  |   ∉    |      |   `\simeq`   |   ≃    |
|  `\leq`   |   ≤    |      | `\partial` |   ∂    |      |   `\cong`    |   ≅    |
|  `\geq`   |   ≥    |      |  `\nabla`  |   ∇    |      |    `\sim`    |   ∼    |
| `\sqrt{}` |   √    |      | `\exists`  |   ∃    |      |   `\cdot`    |   ⋅    |
|  `\circ`  |   ○    |      | `\nexists` |   ∄    |      |   `\cdots`   |   ⋯    |
<!-- --><br/>
<!-- --><br/>



- [Complete list of Math Symbols][math-symb]
<!-- --><br/>
<!-- --><br/>



- Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>


------------------------------------

### LINKS

- Use package ´hyperref´:

```latex
\usepackage{hyperref}
```
```latex
\usepackage[colorlinks=true]{hyperref}
```
```latex
\usepackage[colorlinks=true, <color-parameters> ]{hyperref}
```
<!-- --><br/>


- Optional color parameters for the ´hyperref´ package:
  - `linkcolor`
  - `anchorcolor`
  - `citecolor`
  - `filecolor`
  - `menucolor`
  - `runcolor`
  - `urlcolor`
  - `allcolors`
  - ...
<!-- --><br/>

|     Color     |      Default for ...      |
| :-----------: | :-----------------------: |
|   ` red  `    | `linkcolor` & `menucolor` |
|  `  black  `  |       `anchorcolor`       |
|  `  green  `  |        `citecolor`        |
|  `  cyan  `   | `filecolor` & `runcolor`  |
| `  magenta  ` |        `urlcolor`         |
|  `  blue  `   |                           |
<!-- --><br/>


- Create a URL link:

  ```latex
\url{ <url> }
  ```
  ```latex
\href{ <url> }{ <text> }
  ```
<!-- --><br/>


- Create a link to a file:

  ```latex
\href{ file:<path> }{ <text> }
  ```
  ```latex
\href{ file:./<relative-path> }{ <text> }
  ```
<!-- --><br/>


- [More info][hyperlinks].
<!-- --><br/>
<!-- --><br/>



- Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>




------------------------------------

### ARTICLE CLASS

-




------------------------------------

### BOOK CLASS

- Define Class Book:

```latex
\documentclass[10p]{book}
```
<!-- --><br/>

- Create new Part:

```latex
\part{<title>}
```
<!-- --><br/>


- Create new Chapter (available on books and reports):

```latex
\chapter{<title>}
```
<!-- --><br/>
<!-- --><br/>



- Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>



------------------------------------

### HOMEWORK CLASS

- Custom Class.  
  Get it from: <https://github.com/jez/latex-homework-class>

- The easiest way to use the template is copy the ´.cls´ file to the same directory as the LaTeX project.

- The author recommends to fork the repository then clone the fork.  
  If there are ever any updates, you can ´clone´.

```shell
$ git clone https://github.com/<your-username>/latex-homework-class
$ cd latex-homework-class
$ git remote add upstream https://github.com/jez/latex-homework-class
```
```shell
$ git pull upstream master
```
<!-- --><br/>



- Define Class:

```latex
\documentclass{homework}
```
<!-- --><br/>
<!-- --><br/>



##### QUESTIONS

- Create new automatically numbered Question:

```latex
\question
```
```latex
\question*{<title>}
```
```latex
\section{}
```
```latex
\section*{<title>}
```
<!-- --><br/>


- If questions gets separated from their bodies, force them to the next page:

```latex
\newpage
```
<!-- --><br/>


- To change the Question Type (word before the number), use:

```latex
\renewcommand{\questiontype}{<text>}
```
<!-- --><br/>


- To force the question number use:

```latex
\setcounter{questionCounter}{<number -1>}
```
<!-- --><br/>
<!-- --><br/>



##### QUESTION COUNTER

- Questions can be devided in Parts.  
  Question Part numbers are auto-incremented.  
  Even if interrupted, within the same question, all parts are continuously numbered.

- Use the ´alphaparts´ environment to list with letters.  
  Add the counters with ´\questionpart´ command:

```latex
\begin{alphaparts}
    \questionpart <text>
    \questionpart <text>
    ...
\end{alphaparts}

<text>

\begin{alphaparts}
    \questionpart <text>
    ...
\end{alphaparts}
```
<!-- --><br/>


- Use the ´arabicparts´ environment to list with numbers (includes the ´questionCounter´ number).  
  Add the counters with ´\questionpart´ command:

```latex
\begin{arabicparts}
    \questionpart <text>
    \questionpart <text>
    ...
\end{arabicparts}

<text>

\begin{arabicparts}
    \questionpart <text>
    ...
\end{arabicparts}
```
<!-- --><br/>
<!-- --><br/>



- Go back to [TABLE OF CONTENT](#table-of-content).
<!-- --><br/>



------------------------------------



------------------------------------



------------------------------------



------------------------------------



------------------------------------



------------------------------------



------------------------------------
